
const electron = require('electron')
const path = require('path')
const remote = electron.remote
const BrowserWindow = remote.BrowserWindow
const screen = electron.screen

class BrowserWindowController {
    constructor(path, props) {
        this.win = null
        this.create(path, props)
    }

    create(path, props) {
        this.win = new BrowserWindow(Object.assign({
            title: 'Title',
            width: 800, height: 600,
            autoHideMenuBar: true,
            icon: path.join(__dirname, '/../../assets/img/icon.png'),
            show: false
        }, props))

        this.win.loadFile(path.join(__dirname, path))
    }
}

class Ajuda extends BrowserWindowController {
    constructor() {
        super('/../gui/ajuda/ajuda.html')
    }
}

function projetor() {
    const win = new BrowserWindow({
        title: 'Projetor',
        width: 800, height: 600,
        autoHideMenuBar: true,
        icon: path.join(__dirname, '/../../assets/img/icon.png'),
        show: false
    })

    win.loadFile(path.join(__dirname, '/../gui/projetor/projetor.html'))
    win.setFullScreen(true)

    if (screen.getAllDisplays().length > 1) {
        win.setPosition(window.innerWidth, 0)
    }

    return win
}

module.exports = { Ajuda, projetor }