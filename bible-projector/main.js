const electron = require('electron');
const { app, BrowserWindow } = electron;

function createWindow() {
    // Create the browser window.
    const { width, height } = electron.screen.getPrimaryDisplay().size;

    let win = new BrowserWindow({
        title: 'Bíblia projector',
        width: 800, height: 600,
        autoHideMenuBar: true,
        icon: './data/icon.png',
        minWidth: 600, minHeight: 500
    });

    win.maximize();

    // and load the index.html of the app.
    win.loadFile('index.html');
}

app.on('ready', createWindow);