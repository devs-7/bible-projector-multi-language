const electron = require('electron')
const fs = require('fs')
const path = require('path')
const remote = electron.remote
const BrowserWindow = remote.BrowserWindow
const screen = electron.screen

const Bible = require('../../models/bible')
const browserWindowControllers = require('../../helper/browser_windows_controllers')

const pesquisarButton = document.getElementById('pesquisarButton')
const projetarButton = document.getElementById('projetarButton')
const atualizarButton = document.getElementById('atualizarButton')
const ajudaButton = document.getElementById('ajudaButton')
const pesquisarTexto = document.getElementById('pesquisarTexto')
const tamanhoFonteTexto = document.getElementById('tamanhoFonte')
const preview = document.getElementById('textoSelecionado')
const historico = document.getElementById('historico')
const capituloDiv = document.getElementById('capitulo')
const ultimaPesquisa = document.getElementById('ultimaPesquisa')
const versoes = document.getElementById('versoes')
const corPadrao = document.getElementById('corPadrao')

const win = remote.getCurrentWindow()

localStorage.setItem('preferences', recuperarPreferencias())

function teste() {
    const Bible = require('../../models/bible_sqlite')
    const bible = new Bible()
    bible.query()
}
teste()

var preferencias = JSON.parse(localStorage.getItem('preferences'))
var bible = new Bible(preferencias.versao)

function main() {
    var ajudaBrowserWindow = new browserWindowControllers.Ajuda()
    var projetorBrowserWindow = new browserWindowControllers.Projetor()

    pesquisarButton.onclick = () => pesquisar(true)
    atualizarButton.onclick = () => bible.atualizarTextoLocalStorage(preview.value)
    tamanhoFonteTexto.onchange = () => salvarPreferencias()
    corPadrao.onchange = () => salvarPreferencias()
    projetarButton.onclick = () => projetorBrowserWindow.showInactive()
    ajudaButton.onclick = () => ajudaBrowserWindow.show()

    versoes.onchange = function () {
        bible = new Bible(versoes.value)
    }

    pesquisarTexto.addEventListener('keypress', e => {
        if (e.keyCode == 10) {
            pesquisar(false);
        }

        if (e.keyCode == 13) {
            pesquisar(true);
        }
    });

    preview.addEventListener('keypress', e => {
        switch (e.keyCode) {
            case 16:
                const indexStart = preview.selectionStart
                const indexEnd = preview.selectionEnd
                const text = preview.value
                const start = text.substring(0, indexStart)
                const end = text.substring(indexEnd)
                const half = `{${preferencias.cor}:${text.substring(indexStart, indexEnd)}}`
                preview.value = start + half + end
                atualizarButton.click()
                break
        }
    })

    document.addEventListener('keydown', e => {
        if (e.keyCode == 115) pesquisarTexto.select() // F4
        if (e.keyCode == 116) projetorBrowserWindow.showInactive() // F5
        if (e.keyCode == 117) atualizarButton.click() // F6
        if (e.keyCode == 119) { } // F8
        if (e.keyCode == 120 || e.keyCode == 34) voltarVerso() // F9 e PageDown
        if (e.keyCode == 121 || e.keyCode == 33) avancarVerso() // F10 e PageUp
        if (e.keyCode == 112) ajudaBrowserWindow.show() // F1
        if (e.keyCode == 27) projetorBrowserWindow.close() // ESC
    })

    win.once('close', () => {
        fs.writeFileSync('./Histórico.txt', historico.value);
    })

    tamanhoFonteTexto.value = preferencias.fonte
    versoes.value = preferencias.versao
    corPadrao.value = preferencias.cor
}

function recuperarPreferencias() {
    const conteudo = fs.readFileSync(path.join(__dirname, '/../../../data/preferencias.json'), 'utf-8')
    return conteudo
}

function salvarPreferencias() {
    preferencias = {
        fonte: tamanhoFonteTexto.value,
        versao: versoes.value,
        cor: corPadrao.value
    }
    const preferenciasJSON = JSON.stringify(preferencias)
    localStorage.setItem('preferences', preferenciasJSON)

    fs.writeFile(path.join(__dirname, '/../../../data/preferencias.json'), preferenciasJSON, erro => {
        if (erro) throw erro
    })
}

function avancarVerso() {
    try {
        bible.next()
        preview.value = bible.getVerso()
        atualizarButton.click()
    } catch (e) {
        preview.value = e.message
    }
}

function voltarVerso() {
    try {
        bible.prev()
        preview.value = bible.getVerso()
        atualizarButton.click()
    } catch (e) {
        preview.value = e.message;
    }
}

function atualizarHistorico() {
    let textos = [];
    textos = historico.value.split('\n');
    textos.push(ultimaPesquisa.innerHTML);

    // Removendo elementos repetidos e inválidos
    textos = textos.filter((elemento, indice) => {
        return textos.indexOf(elemento) == indice && !!elemento;
    });

    // Atualização da caixa de texto
    let temp = '';
    textos.forEach(texto => {
        temp += texto + '\n';
    });
    temp = temp.substring(0, temp.length - 1);

    historico.value = temp;
}

function pesquisar(projetar = true, pesquisa = pesquisarTexto.value) {
    bible.pesquisarReferencia(pesquisa)

    if (bible.isNotVoid()) {
        ultimaPesquisa.innerHTML = bible.getRepresentacao(false)
        pesquisarTexto.value = bible.getRepresentacao(false)
        preview.value = bible.getVerso()

        if (projetar) {
            salvarPreferencias()
            atualizarHistorico()
        }

        capituloDiv.innerHTML = ''

        bible.capituloForEach((verso, isAtual, n) => {
            if (isAtual) {
                capituloDiv.innerHTML += `<span style="color: rgb(20, 66, 165)">${n} ${verso}</span><br>`
            } else {
                capituloDiv.innerHTML += `${n} ${verso}<br>`
            }
        })
    }
}

main()