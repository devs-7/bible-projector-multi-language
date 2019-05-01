function toggleFullScreen() {
    if (!document.webkitFullscreenElement) {
        document.documentElement.webkitRequestFullscreen(Element.ALLOW_KEYBOARD_INPUT);
    }
    else {
        document.webkitExitFullscreen();
    }
}

function aplicarAlteracoes(texto = '') {
    texto = texto.replace(/{/g, '<span style="color: red">');
    texto = texto.replace(/}/g, '</span>');

    return texto;
}

function aplicarPreferencias() {
    fs.readFile('data/preferencias.json', 'utf-8', (erro, conteudo) => {
        const preferencias = JSON.parse(conteudo);
        texto.style.fontSize = Number(preferencias.fonte) + 'px';
    });
}

function getPreferencias() {
    const preferencias = JSON.parse(fs.readFileSync('data/preferencias.json', 'utf-8'));
    return preferencias;
}

function setPreferencias(preferencias) {
    fs.writeFile('data/preferencias.json', JSON.stringify(preferencias), () => { });
}

function aumentarFonte(sinal) {
    const preferencias = getPreferencias();
    switch (sinal) {
        case '+':
            preferencias.fonte += 5;
            break;

        case '-':
            preferencias.fonte -= 5;
            break;
    }
    setPreferencias(preferencias);
}

function avancarVerso(sentido) {
    fs.readFile('data/preferencias.json', 'utf-8', (erro, conteudo) => {
        let preferencias = JSON.parse(conteudo);
        let { livro, capitulo, versiculo } = preferencias.textoAtual;

        switch (sentido) {
            case '>':
                if (!!queryTexto(biblia, livro, capitulo, Number(versiculo) + 1)) {
                    versiculo++;
                }
                break;

            case '<':
                if (versiculo > 1) {
                    versiculo--;
                }
                break;
        }

        preferencias.textoAtual.versiculo = versiculo;
        preferencias.textoAtual.texto = queryTexto(biblia, livro, capitulo, versiculo) + getRepresentacao(livro, capitulo, versiculo);
        setPreferencias(preferencias);
    });
}

document.addEventListener('keydown', e => {
    if (e.keyCode == 27) { // ESC
        window.close();
    }

    if (e.keyCode == 116) { // F5
        toggleFullScreen();
    }

    if (e.keyCode == 40) { // Seta para baixo
        aumentarFonte('-');
    }

    if (e.keyCode == 38) { // Seta para cima
        aumentarFonte('+');
    }

    if (e.keyCode == 37 || e.keyCode == 120 || e.keyCode == 34) { // Seta para esquerda, F9 e PageDown
        avancarVerso('<');
    }

    if (e.keyCode == 39 || e.keyCode == 121 || e.keyCode == 33) { // Seta para direita, F10 e PageUp
        avancarVerso('>');
    }
});

const fs = require('fs');
const electron = require('electron');
const { screen } = require('electron');
const texto = document.querySelector('p');
let biblia = fs.readFileSync('data/bibles/' + getPreferencias().versao + '.txt', 'utf-8');

const displays = screen.getAllDisplays();

setInterval(() => {
    texto.innerHTML = aplicarAlteracoes(getPreferencias().textoAtual.texto);
    aplicarPreferencias(texto);
}, 10);