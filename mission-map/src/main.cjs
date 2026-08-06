'use strict';

const { app, BrowserWindow, dialog, ipcMain, safeStorage } = require('electron');
const fs = require('node:fs');
const fsp = require('node:fs/promises');
const http = require('node:http');
const path = require('node:path');
const { parseScenario } = require('./scenario-parser.cjs');
const { saveScenarioEdits } = require('./scenario-editor.cjs');
const { selectTheater } = require('./theater-selector.cjs');

const APP_PORT = 43117;
const APP_HOST = '127.0.0.1';
const PROJECT_ROOT = path.resolve(__dirname, '..', '..');
const SCENARIO_ROOT = path.join(PROJECT_ROOT, 'scenarios');
const THEATER_ROOT = path.join(PROJECT_ROOT, 'theaters');
const RENDERER_ROOT = path.join(__dirname, '..', 'renderer');

let mainWindow;
let localServer;
let scenarioWatcher;
let watchedScenarioPath = '';

const hasSingleInstanceLock = app.requestSingleInstanceLock();
if (!hasSingleInstanceLock) app.quit();

function settingsPath() {
  return path.join(app.getPath('userData'), 'settings.json');
}

async function readSettings() {
  try {
    return JSON.parse(await fsp.readFile(settingsPath(), 'utf8'));
  } catch {
    return {};
  }
}

async function writeSettings(settings) {
  await fsp.mkdir(path.dirname(settingsPath()), { recursive: true });
  await fsp.writeFile(settingsPath(), `${JSON.stringify(settings, null, 2)}\n`, 'utf8');
}

async function getMapsKey() {
  const settings = await readSettings();
  if (!settings.mapsKey) return '';
  if (!safeStorage.isEncryptionAvailable()) return '';
  try {
    return safeStorage.decryptString(Buffer.from(settings.mapsKey, 'base64'));
  } catch {
    return '';
  }
}

async function setMapsKey(key) {
  const value = String(key || '').trim();
  if (!value) {
    await writeSettings({ ...(await readSettings()), mapsKey: '' });
    return { saved: true, encrypted: false };
  }
  if (!safeStorage.isEncryptionAvailable()) {
    return { saved: false, encrypted: false, error: 'OS-backed encryption is unavailable; the key was not saved.' };
  }
  const settings = await readSettings();
  settings.mapsKey = safeStorage.encryptString(value).toString('base64');
  await writeSettings(settings);
  return { saved: true, encrypted: true };
}

function isScenarioPath(filePath) {
  return typeof filePath === 'string' && path.extname(filePath).toLowerCase() === '.py';
}

async function loadScenario(filePath) {
  if (!isScenarioPath(filePath)) throw new Error('Select a Python scenario file.');
  const source = await fsp.readFile(filePath, 'utf8');
  const scenario = parseScenario(source, filePath);
  const theaterFiles = (await fsp.readdir(THEATER_ROOT)).filter((name) => name.toLowerCase().endsWith('.json'));
  const theaters = await Promise.all(theaterFiles.map(async (name) => (
    JSON.parse(await fsp.readFile(path.join(THEATER_ROOT, name), 'utf8'))
  )));
  return { scenario, theater: selectTheater(scenario, theaters) };
}

function watchScenario(filePath) {
  scenarioWatcher?.close();
  scenarioWatcher = null;
  watchedScenarioPath = filePath;
  if (!isScenarioPath(filePath)) return;
  let debounce;
  scenarioWatcher = fs.watch(filePath, () => {
    clearTimeout(debounce);
    debounce = setTimeout(() => {
      mainWindow?.webContents.send('scenario:changed', watchedScenarioPath);
    }, 250);
  });
}

function contentType(filePath) {
  return ({
    '.html': 'text/html; charset=utf-8',
    '.js': 'text/javascript; charset=utf-8',
    '.css': 'text/css; charset=utf-8',
    '.svg': 'image/svg+xml',
  })[path.extname(filePath)] || 'application/octet-stream';
}

function startLocalServer() {
  return new Promise((resolve, reject) => {
    localServer = http.createServer(async (request, response) => {
      try {
        const requestPath = new URL(request.url, `http://${APP_HOST}`).pathname;
        const relativePath = requestPath === '/' ? 'index.html' : decodeURIComponent(requestPath.slice(1));
        const filePath = path.resolve(RENDERER_ROOT, relativePath);
        if (!filePath.startsWith(`${RENDERER_ROOT}${path.sep}`) && filePath !== path.join(RENDERER_ROOT, 'index.html')) {
          response.writeHead(403).end('Forbidden');
          return;
        }
        const body = await fsp.readFile(filePath);
        response.writeHead(200, {
          'Content-Type': contentType(filePath),
          'Cache-Control': 'no-store',
          'Content-Security-Policy': [
            "default-src 'self'",
            "script-src 'self' https://maps.googleapis.com https://maps.gstatic.com",
            "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com",
            "font-src 'self' https://fonts.gstatic.com",
            "img-src 'self' data: blob: https://*.googleapis.com https://*.gstatic.com https://*.google.com https://*.ggpht.com",
            "connect-src 'self' https://maps.googleapis.com https://maps.gstatic.com https://*.googleapis.com",
            "worker-src 'self' blob:",
          ].join('; '),
        });
        response.end(body);
      } catch {
        response.writeHead(404).end('Not found');
      }
    });
    localServer.once('error', reject);
    localServer.listen(APP_PORT, APP_HOST, resolve);
  });
}

function registerIpc() {
  ipcMain.handle('scenario:list', async () => {
    const entries = await fsp.readdir(SCENARIO_ROOT, { withFileTypes: true });
    return entries
      .filter((entry) => entry.isFile() && entry.name.toLowerCase().endsWith('.py'))
      .map((entry) => ({ name: entry.name, path: path.join(SCENARIO_ROOT, entry.name) }))
      .sort((left, right) => left.name.localeCompare(right.name));
  });
  ipcMain.handle('scenario:open-dialog', async () => {
    const result = await dialog.showOpenDialog(mainWindow, {
      title: 'Open GCBH scenario',
      defaultPath: SCENARIO_ROOT,
      properties: ['openFile'],
      filters: [{ name: 'GCBH Python scenarios', extensions: ['py'] }],
    });
    return result.canceled ? '' : result.filePaths[0];
  });
  ipcMain.handle('scenario:load', async (_event, filePath) => {
    const result = await loadScenario(filePath);
    watchScenario(filePath);
    return result;
  });
  ipcMain.handle('scenario:save-edits', async (_event, filePath, edits) => {
    if (!isScenarioPath(filePath)) throw new Error('Coordinate edits can only be saved to Python scenarios.');
    if (path.resolve(filePath) !== path.resolve(watchedScenarioPath)) {
      throw new Error('The scenario changed before saving; reload it and try again.');
    }
    return saveScenarioEdits(filePath, edits);
  });
  ipcMain.handle('maps-key:get', getMapsKey);
  ipcMain.handle('maps-key:set', (_event, key) => setMapsKey(key));
}

async function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1500,
    height: 930,
    minWidth: 1080,
    minHeight: 700,
    backgroundColor: '#071019',
    title: 'GCBH Mission Map',
    webPreferences: {
      preload: path.join(__dirname, 'preload.cjs'),
      nodeIntegration: false,
      contextIsolation: true,
      sandbox: true,
    },
  });
  mainWindow.webContents.setWindowOpenHandler(() => ({ action: 'deny' }));
  mainWindow.webContents.on('will-navigate', (event, targetUrl) => {
    if (!targetUrl.startsWith(`http://${APP_HOST}:${APP_PORT}/`)) event.preventDefault();
  });
  await mainWindow.loadURL(`http://${APP_HOST}:${APP_PORT}/`);
}

app.on('second-instance', () => {
  if (!mainWindow) return;
  if (mainWindow.isMinimized()) mainWindow.restore();
  mainWindow.focus();
});

if (hasSingleInstanceLock) app.whenReady().then(async () => {
  registerIpc();
  await startLocalServer();
  await createWindow();
  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit();
});

app.on('before-quit', () => {
  scenarioWatcher?.close();
  localServer?.close();
});
