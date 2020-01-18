const electron = require('electron');
const { app, BrowserWindow, Menu } = electron;

function createWindow() {
    let win = new BrowserWindow({
        title: 'Bible projector',
        width: 800, height: 600,
        autoHideMenuBar: true,
        icon: './assets/img/icon.png',
        minWidth: 600, minHeight: 500,
        show: false,
        webPreferences: {
            nodeIntegration: true,
            devTools: true
        }
    });

    win.maximize();
    win.setMenuBarVisibility(false);

    win.loadFile('./src/gui/main/main.html');

    win.once('ready-to-show', () => {
        win.show();
    });

    win.once('close', () => {
        app.quit();
    });
}

app.once('ready', () => {
    createWindow();

    // Menu.setApplicationMenu(null)
});