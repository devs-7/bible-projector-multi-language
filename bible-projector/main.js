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
        minWidth: 600, minHeight: 500,
        show: false
    });

    win.maximize();

    win.loadFile('index.html');

    win.once('ready-to-show', () => {
        win.show();
    });

    win.once('close', () => {
        process.exit();
    });
}

app.on('ready', createWindow);