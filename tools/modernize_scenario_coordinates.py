"""Clone a legacy GCBH scenario using v0.2.1 latitude/longitude positions."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


POSITION = re.compile(
    r"^(?P<prefix>\s*unit\.SetPosition\()"
    r"(?P<longitude>[-+\d.eE]+)(?P<separator>\s*,\s*)"
    r"(?P<latitude>[-+\d.eE]+)(?P<suffix>\s*,\s*[^\r\n]+\))\s*$",
    re.MULTILINE,
)


def modernize(source: str) -> tuple[str, int]:
    if source.startswith("# Scenario version: 0.2.1"):
        raise ValueError("Source already declares the v0.2.1 coordinate convention.")

    def swap(match: re.Match[str]) -> str:
        return (
            f"{match.group('prefix')}{match.group('latitude')}"
            f"{match.group('separator')}{match.group('longitude')}{match.group('suffix')}"
        )

    converted, count = POSITION.subn(swap, source)
    if count == 0:
        raise ValueError("No legacy unit.SetPosition calls were found.")
    converted = "# Scenario version: 0.2.1\n" + converted
    return converted, count


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()

    if args.destination.exists():
        raise FileExistsError(f"Refusing to overwrite {args.destination}")
    converted, count = modernize(args.source.read_text(encoding="utf-8"))
    args.destination.write_text(converted, encoding="utf-8", newline="\n")
    print(f"Converted {count} positions into {args.destination}")


if __name__ == "__main__":
    main()
