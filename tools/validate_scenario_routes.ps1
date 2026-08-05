	param(
	    [Parameter(Mandatory = $true)]
	    [string]$ScenarioPath,

	    [string]$TheaterPath = '',

    [double]$SegmentStepDeg = 0.01,

    [double]$SnapSearchRadiusDeg = 0.40,

    [double]$SnapStepDeg = 0.01
)

	$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($TheaterPath)) {
    $TheaterPath = Join-Path $PSScriptRoot '..\theaters\hormuz_mvp.json'
}

function Get-JsonFile {
    param([string]$Path)
    Get-Content -Raw $Path | ConvertFrom-Json
}

function Test-PointInPolygon {
    param(
        [double]$Lon,
        [double]$Lat,
        [object[]]$Polygon
    )

    $inside = $false
    $j = $Polygon.Count - 1
    for ($i = 0; $i -lt $Polygon.Count; $i++) {
        $xi = [double]$Polygon[$i][0]
        $yi = [double]$Polygon[$i][1]
        $xj = [double]$Polygon[$j][0]
        $yj = [double]$Polygon[$j][1]

        $intersects = (($yi -gt $Lat) -ne ($yj -gt $Lat)) -and
            ($Lon -lt (($xj - $xi) * ($Lat - $yi) / (($yj - $yi) + 1.0e-12) + $xi))

        if ($intersects) {
            $inside = -not $inside
        }
        $j = $i
    }

    return $inside
}

function Test-IsSafeWater {
    param(
        [double]$Lon,
        [double]$Lat,
        [object]$Theater
    )

    foreach ($poly in $Theater.safe_water_polygons) {
        if (Test-PointInPolygon -Lon $Lon -Lat $Lat -Polygon $poly.points) {
            return $true
        }
    }
    return $false
}

function Get-ApproxDistanceDeg {
    param(
        [double]$Lon1,
        [double]$Lat1,
        [double]$Lon2,
        [double]$Lat2
    )

    $dx = ($Lon2 - $Lon1) * [Math]::Cos((($Lat1 + $Lat2) * 0.5) * [Math]::PI / 180.0)
    $dy = ($Lat2 - $Lat1)
    return [Math]::Sqrt(($dx * $dx) + ($dy * $dy))
}

function Find-NearestSafeWaterPoint {
    param(
        [double]$Lon,
        [double]$Lat,
        [object]$Theater,
        [double]$MaxRadiusDeg,
        [double]$StepDeg
    )

    if (Test-IsSafeWater -Lon $Lon -Lat $Lat -Theater $Theater) {
        return [pscustomobject]@{
            lon = $Lon
            lat = $Lat
            distance_deg = 0.0
        }
    }

    $best = $null
    for ($radius = $StepDeg; $radius -le $MaxRadiusDeg; $radius += $StepDeg) {
        for ($dx = -$radius; $dx -le $radius; $dx += $StepDeg) {
            foreach ($dy in @(-$radius, $radius)) {
                $candLon = $Lon + $dx
                $candLat = $Lat + $dy
                if (Test-IsSafeWater -Lon $candLon -Lat $candLat -Theater $Theater) {
                    $dist = Get-ApproxDistanceDeg -Lon1 $Lon -Lat1 $Lat -Lon2 $candLon -Lat2 $candLat
                    if (($null -eq $best) -or ($dist -lt $best.distance_deg)) {
                        $best = [pscustomobject]@{
                            lon = [Math]::Round($candLon, 6)
                            lat = [Math]::Round($candLat, 6)
                            distance_deg = [Math]::Round($dist, 6)
                        }
                    }
                }
            }
        }

        for ($dy = (-$radius + $StepDeg); $dy -lt $radius; $dy += $StepDeg) {
            foreach ($dx in @(-$radius, $radius)) {
                $candLon = $Lon + $dx
                $candLat = $Lat + $dy
                if (Test-IsSafeWater -Lon $candLon -Lat $candLat -Theater $Theater) {
                    $dist = Get-ApproxDistanceDeg -Lon1 $Lon -Lat1 $Lat -Lon2 $candLon -Lat2 $candLat
                    if (($null -eq $best) -or ($dist -lt $best.distance_deg)) {
                        $best = [pscustomobject]@{
                            lon = [Math]::Round($candLon, 6)
                            lat = [Math]::Round($candLat, 6)
                            distance_deg = [Math]::Round($dist, 6)
                        }
                    }
                }
            }
        }

        if ($null -ne $best) {
            return $best
        }
    }

    return $null
}

function Test-SegmentSafe {
    param(
        [double]$Lon1,
        [double]$Lat1,
        [double]$Lon2,
        [double]$Lat2,
        [object]$Theater,
        [double]$StepDeg
    )

    $distance = Get-ApproxDistanceDeg -Lon1 $Lon1 -Lat1 $Lat1 -Lon2 $Lon2 -Lat2 $Lat2
    $steps = [Math]::Max(1, [Math]::Ceiling($distance / $StepDeg))

    for ($i = 0; $i -le $steps; $i++) {
        $t = $i / $steps
        $lon = $Lon1 + (($Lon2 - $Lon1) * $t)
        $lat = $Lat1 + (($Lat2 - $Lat1) * $t)
        if (-not (Test-IsSafeWater -Lon $lon -Lat $lat -Theater $Theater)) {
            return [pscustomobject]@{
                ok = $false
                hit_lon = [Math]::Round($lon, 6)
                hit_lat = [Math]::Round($lat, 6)
                sample_index = $i
                sample_count = $steps
            }
        }
    }

    return [pscustomobject]@{
        ok = $true
    }
}

function Get-IsSurfaceClass {
    param(
        [string]$ClassName,
        [object]$Theater
    )

    return $Theater.surface_classes -contains $ClassName
}

function Parse-ScenarioSurfaceTracks {
    param(
        [string]$Path,
        [object]$Theater
    )

    $lines = Get-Content $Path
    $units = @()
    $currentClass = $null
    $currentUnit = $null
    $currentSurface = $false
    $currentWaypoints = @()
    $currentPos = $null
    $currentPosLine = $null

    foreach ($i in 0..($lines.Count - 1)) {
        $line = $lines[$i]

        if ($line -match "unit\.className = '([^']+)'") {
            if ($null -ne $currentUnit -and $currentSurface) {
                $units += [pscustomobject]@{
                    unit_name = $currentUnit
                    class_name = $currentClass
                    position = $currentPos
                    position_line = $currentPosLine
                    waypoints = $currentWaypoints
                }
            }
            $currentClass = $matches[1]
            $currentUnit = $null
            $currentSurface = Get-IsSurfaceClass -ClassName $currentClass -Theater $Theater
            $currentWaypoints = @()
            $currentPos = $null
            $currentPosLine = $null
            continue
        }

        if ($line -match "unit\.unitName = '([^']+)'") {
            $currentUnit = $matches[1]
            continue
        }

        if ($currentSurface -and $line -match "unit\.SetPosition\(([0-9\.\-]+), ([0-9\.\-]+), ([0-9\.\-]+)\)") {
            $currentPos = [pscustomobject]@{
                lon = [double]$matches[1]
                lat = [double]$matches[2]
                alt = [double]$matches[3]
            }
            $currentPosLine = $i + 1
            continue
        }

        if ($currentSurface -and $line -match "UI\.add_waypoint_advanced\(([0-9\.\-]+), ([0-9\.\-]+), ([0-9\.\-]+), ([0-9\.\-]+)\)") {
            $currentWaypoints += [pscustomobject]@{
                lat = [double]$matches[1]
                lon = [double]$matches[2]
                alt = [double]$matches[3]
                speed = [double]$matches[4]
                line = $i + 1
            }
        }
    }

    if ($null -ne $currentUnit -and $currentSurface) {
        $units += [pscustomobject]@{
            unit_name = $currentUnit
            class_name = $currentClass
            position = $currentPos
            position_line = $currentPosLine
            waypoints = $currentWaypoints
        }
    }

    return $units
}

$scenario = (Resolve-Path $ScenarioPath).Path
$theater = Get-JsonFile -Path (Resolve-Path $TheaterPath).Path
$units = Parse-ScenarioSurfaceTracks -Path $scenario -Theater $theater

$issues = @()

foreach ($unit in $units) {
    if ($null -ne $unit.position) {
        $startOk = Test-IsSafeWater -Lon $unit.position.lon -Lat $unit.position.lat -Theater $theater
        if (-not $startOk) {
            $snap = Find-NearestSafeWaterPoint -Lon $unit.position.lon -Lat $unit.position.lat -Theater $theater -MaxRadiusDeg $SnapSearchRadiusDeg -StepDeg $SnapStepDeg
            $issues += [pscustomobject]@{
                type = 'start_position'
                unit_name = $unit.unit_name
                class_name = $unit.class_name
                line = $unit.position_line
                lon = $unit.position.lon
                lat = $unit.position.lat
                suggestion = $snap
            }
        }
    }

    $prevLon = $unit.position.lon
    $prevLat = $unit.position.lat
    $wpIndex = 0
    foreach ($wp in $unit.waypoints) {
        $wpIndex += 1
        $wpOk = Test-IsSafeWater -Lon $wp.lon -Lat $wp.lat -Theater $theater
        if (-not $wpOk) {
            $snap = Find-NearestSafeWaterPoint -Lon $wp.lon -Lat $wp.lat -Theater $theater -MaxRadiusDeg $SnapSearchRadiusDeg -StepDeg $SnapStepDeg
            $issues += [pscustomobject]@{
                type = 'waypoint'
                unit_name = $unit.unit_name
                class_name = $unit.class_name
                line = $wp.line
                waypoint_index = $wpIndex
                lon = $wp.lon
                lat = $wp.lat
                suggestion = $snap
            }
        }

        $segment = Test-SegmentSafe -Lon1 $prevLon -Lat1 $prevLat -Lon2 $wp.lon -Lat2 $wp.lat -Theater $theater -StepDeg $SegmentStepDeg
        if (-not $segment.ok) {
            $issues += [pscustomobject]@{
                type = 'segment_crossing'
                unit_name = $unit.unit_name
                class_name = $unit.class_name
                line = $wp.line
                waypoint_index = $wpIndex
                from_lon = $prevLon
                from_lat = $prevLat
                to_lon = $wp.lon
                to_lat = $wp.lat
                hit_lon = $segment.hit_lon
                hit_lat = $segment.hit_lat
            }
        }

        $prevLon = $wp.lon
        $prevLat = $wp.lat
    }
}

if ($issues.Count -eq 0) {
    Write-Output "PASS: no safe-water issues found in $scenario"
    exit 0
}

Write-Output "FAIL: safe-water issues found in $scenario"
foreach ($issue in $issues) {
    switch ($issue.type) {
        'start_position' {
            Write-Output ("[{0}] start off water at line {1}: {2} ({3}) lon={4} lat={5}" -f $issue.type, $issue.line, $issue.unit_name, $issue.class_name, $issue.lon, $issue.lat)
            if ($null -ne $issue.suggestion) {
                Write-Output ("  suggested safe point: lon={0} lat={1}" -f $issue.suggestion.lon, $issue.suggestion.lat)
            }
        }
        'waypoint' {
            Write-Output ("[{0}] waypoint {1} off water at line {2}: {3} ({4}) lon={5} lat={6}" -f $issue.type, $issue.waypoint_index, $issue.line, $issue.unit_name, $issue.class_name, $issue.lon, $issue.lat)
            if ($null -ne $issue.suggestion) {
                Write-Output ("  suggested safe point: lon={0} lat={1}" -f $issue.suggestion.lon, $issue.suggestion.lat)
            }
        }
        'segment_crossing' {
            Write-Output ("[{0}] segment to waypoint {1} crosses unsafe area at line {2}: {3} ({4}) hit near lon={5} lat={6}" -f $issue.type, $issue.waypoint_index, $issue.line, $issue.unit_name, $issue.class_name, $issue.hit_lon, $issue.hit_lat)
        }
    }
}

exit 1
