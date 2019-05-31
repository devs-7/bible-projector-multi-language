const electron = require('electron');
const { app, BrowserWindow } = electron;

function createWindow() {
    let win = new BrowserWindow({
        title: 'Bíblia projector',
        width: 800, height: 600,
        autoHideMenuBar: true,
        icon: './data/icon.png',
        minWidth: 600, minHeight: 500,
        show: false
    });

    win.maximize();

    win.loadFile('windows/index.html');

    win.once('ready-to-show', () => {
        win.show();
    });

    win.once('close', () => {
        process.exit();
    });
}

app.once('ready', createWindow);