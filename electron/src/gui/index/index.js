// Bibliotecas
const electron = require('electron');
const fs = require('fs');
const path = require('path');
const remote = electron.remote;
const BrowserWindow = remote.BrowserWindow;
const screen = electron.screen;

// Recupera componentes
const pesquisarButton = document.getElementById('pesquisarButton');
const projetarButton = document.getElementById('projetarButton');
const atualizarButton = document.getElementById('atualizarButton');
const ajudaButton = document.getElementById('ajudaButton');
const pesquisarTexto = document.getElementById('pesquisarTexto');
const tamanhoFonteTexto = document.getElementById('tamanhoFonte');
const preview = document.getElementById('textoSelecionado');
const historico = document.getElementById('historico');
const capituloDiv = document.getElementById('capitulo');
const ultimaPesquisa = document.getElementById('ultimaPesquisa');
const versoes = document.getElementById('versoes');
const win = remote.getCurrentWindow();

var preferencias;

let winProjetor = null
preview.value = path.join(__dirname, '/../projetor/projetor.html')

// Cria objeto projetor
const projetor = {
    criarTela() {
        winProjetor = new BrowserWindow({
            title: 'Projetor',
            width: 800, height: 600,
            autoHideMenuBar: true,
            icon: __dirname + '../../../assets/img/icon.png',
            show: false
        });

        winProjetor.loadFile(path.join(__dirname, '/../projetor/projetor.html'));
        winProjetor.setFullScreen(true);

        if (screen.getAllDisplays().length > 1) {
            winProjetor.setPosition(window.innerWidth, 0);
        }

        winProjetor.once('closed', () => {
            this.criarTela();
        });
    },

    projetar() {
        // winProjetor.showInactive()
        winProjetor.show()
    },

    fechar() {
        winProjetor.destroy();
    }
}

function salvarPreferencias(texto = preview.value) {
    const preferences_json = JSON.stringify({
        fonte: Number(tamanhoFonteTexto.value),
        versao: versoes.value
    });

    fs.writeFile(path.join(__dirname, '/../../../data/preferencias.json'), preferences_json, e => {
        if (!!e) preview.value = 'Erro ao salvar modificações.';
    });

    localStorage.setItem('preferences', preferences_json);
    localStorage.setItem('texto', texto);
}

function ajuda() {
    const winAjuda = new BrowserWindow({
        title: 'Ajuda',
        width: 800, height: 600,
        autoHideMenuBar: true,
        icon: '../../../assets/img/icon.png',
        show: false
    });

    winAjuda.loadFile('../ajuda/ajuda.html');

    winAjuda.once('ready-to-show', () => {
        winAjuda.show();
    });
}

function avancarVerso() {
    try {
        bible.next();
        preview.value = bible.getVerso();
        atualizarButton.click();
    } catch (e) {
        preview.value = e.message;
    }
}

function voltarVerso() {
    try {
        bible.prev();
        preview.value = bible.getVerso();
        atualizarButton.click();
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
    bible.pesquisarReferencia(pesquisa);

    if (bible.isNotVoid()) {
        ultimaPesquisa.innerHTML = bible.getRepresentacao(false);
        pesquisarTexto.value = bible.getRepresentacao(false);
        preview.value = bible.getVerso();

        if (projetar) {
            salvarPreferencias();
            atualizarHistorico();
        }

        capituloDiv.innerHTML = '';

        bible.capituloForEach((verso, isAtual, n) => {
            if (isAtual) {
                capituloDiv.innerHTML += `<span style="color: rgb(20, 66, 165)">${n} ${verso}</span><br>`;
            } else {
                capituloDiv.innerHTML += `${n} ${verso}<br>`;
            }
        });
    }
}

// Listeners

pesquisarButton.onclick = () => pesquisar(true);
atualizarButton.onclick = () => salvarPreferencias();
tamanhoFonteTexto.onchange = () => salvarPreferencias();
projetarButton.onclick = projetor.projetar;
ajudaButton.onclick = ajuda;

versoes.onchange = function () {
    bible = new Bible(versoes.value);
}

pesquisarTexto.addEventListener('keypress', e => {
    if (e.keyCode == 10) {
        pesquisar(false);
    }

    if (e.keyCode == 13) {
        pesquisar(true);
    }
});

document.addEventListener('keydown', e => {
    if (e.keyCode == 115) pesquisarTexto.select(); // F4
    if (e.keyCode == 116) projetor.projetar(); // F5
    if (e.keyCode == 117) salvarPreferencias(); // F6
    if (e.keyCode == 119) { } // F8
    if (e.keyCode == 120 || e.keyCode == 34) voltarVerso(); // F9 e PageDown
    if (e.keyCode == 121 || e.keyCode == 33) avancarVerso(); // F10 e PageUp
    if (e.keyCode == 112) ajuda(); // F1
    if (e.keyCode == 27) projetor.fechar(); // ESC
});

win.once('close', () => {
    fs.writeFileSync('./Histórico.txt', historico.value);
});

try {
    preferencias = JSON.parse(fs.readFileSync(path.join(__dirname, '/../../../data/preferencias.json'), 'utf-8'));
}
catch {
    const preferencias_json = fs.readFileSync(path.join(__dirname, '/../../../data/preferencias.json'));
    fs.writeFileSync(path.join(__dirname, '/../../../data/preferencias.json'), preferencias_json);
    preferencias = JSON.parse(preferencias_json);
}

var bible = new Bible(preferencias.versao);
tamanhoFonteTexto.value = preferencias.fonte;
versoes.value = preferencias.versao;

projetor.criarTela();