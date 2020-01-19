function toggleFullScreen() {
    if (!document.webkitFullscreenElement) {
        document.documentElement.webkitRequestFullscreen(Element.ALLOW_KEYBOARD_INPUT)
    }
    else {
        document.webkitExitFullscreen()
    }
}

function getPreferencias() {
    return JSON.parse(localStorage.getItem('preferences'))
}

function getTexto() {
    let texto = localStorage.getItem('texto')
    texto = texto.replace(/{/g, '<span style="color: red">')
    texto = texto.replace(/}/g, '</span>')
    return texto
}

function aplicarPreferencias() {
    const preferencias = getPreferencias()
    texto.style.fontSize = Number(preferencias.fonte) + 'px'
}

document.addEventListener('keydown', e => {
    if (e.keyCode == 27) { // ESC
        window.close()
    }
})

const texto = document.querySelector('p')

setInterval(() => {
    texto.innerHTML = getTexto()
    aplicarPreferencias()
}, 10)