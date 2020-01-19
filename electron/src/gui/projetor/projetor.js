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

function configureColors(texto, textoNew = '', min = 0) {
    if (textoNew == '') {
        texto = texto.replace(/{b:/g, '{deepskyblue:')
        texto = texto.replace(/{r:/g, '{red:')
        texto = texto.replace(/{g:/g, '{green:')
        texto = texto.replace(/{y:/g, '{yellow:')
        texto = texto.replace(/}/g, '</span>')
        textoNew = texto
    }
    let index1 = texto.indexOf('{', min)
    let index2 = texto.indexOf(':', min)
    if (index1 > -1 && index2 > -1) {
        let s = texto.substring(index1, index2 + 1)
        const color = s.substring(1, s.length - 1)
        textoNew = textoNew.replace(s, `<span style="color: ${color}">`)
        return configureColors(texto, textoNew, index2 + 1)
    } else {
        return textoNew
    }
}

function getTexto() {
    let texto = localStorage.getItem('texto')
    texto = configureColors(texto)
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