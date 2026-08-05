'use strict';

const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('missionMap', {
  listScenarios: () => ipcRenderer.invoke('scenario:list'),
  chooseScenario: () => ipcRenderer.invoke('scenario:open-dialog'),
  loadScenario: (filePath) => ipcRenderer.invoke('scenario:load', filePath),
  saveScenarioEdits: (filePath, edits) => ipcRenderer.invoke('scenario:save-edits', filePath, edits),
  getMapsKey: () => ipcRenderer.invoke('maps-key:get'),
  setMapsKey: (key) => ipcRenderer.invoke('maps-key:set', key),
  onScenarioChanged: (callback) => {
    const listener = (_event, filePath) => callback(filePath);
    ipcRenderer.on('scenario:changed', listener);
    return () => ipcRenderer.removeListener('scenario:changed', listener);
  },
});
