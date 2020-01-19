
const electron = require('electron')
const path = require('path')
const remote = electron.remote
const BrowserWindow = remote.BrowserWindow
const screen = electron.screen

class BrowserWindowController {
    constructor(filePath, props) {
        this.win = null
        this.create(filePath, props)
    }

    create(filePath, props) {
        this.win = new BrowserWindow(Object.assign({
            title: 'Title',
            width: 800, height: 600,
            autoHideMenuBar: true,
            icon: path.join(__dirname, '/../../assets/img/icon.png'),
            show: false
        }, props))

        this.win.loadFile(path.join(__dirname, filePath))

        this.win.once('closed', () => {
            this.create(filePath)
        })
    }

    show() {
        this.win.show()
    }

    showInactive() {
        this.win.showInactive()
    }

    close() {
        this.win.close()
    }
}

class Ajuda extends BrowserWindowController {
    constructor() {
        super('/../gui/ajuda/ajuda.html', { title: 'Ajuda' })
    }
}

class Projetor extends BrowserWindowController {
    constructor() {
        super('/../gui/projetor/projetor.html', { title: 'Projetor' })
    }

    create(filePath, props) {
        super.create(filePath, props)
        this.win.setFullScreen(true)

        if (screen.getAllDisplays().length > 1) {
            win.setPosition(window.innerWidth, 0)
        }
    }
}

module.exports = { Ajuda, Projetor }