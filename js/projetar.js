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

function getPreferencias() {
    const preferencias = JSON.parse(localStorage.getItem('preferences'));
    return preferencias;
}

function aplicarPreferencias() {
    const preferencias = getPreferencias();
    texto.style.fontSize = Number(preferencias.fonte) + 'px';
}

const texto = document.querySelector('p');

setInterval(() => {
    texto.innerHTML = aplicarAlteracoes(getPreferencias().textoAtual.texto);
    aplicarPreferencias(texto);
}, 10);