const { app, BrowserWindow } = require('electron');

function createWindow() {
    // Create the browser window.
    let win = new BrowserWindow({ title: 'Bíblia projector', width: 800, height: 600, autoHideMenuBar: true, icon: './data/icon.png' });

    // and load the index.html of the app.
    win.loadFile('index.html');
}

app.on('ready', createWindow);