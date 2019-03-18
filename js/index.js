const pesquisarButton = document.getElementById('pesquisarButton');
const projetarButton = document.getElementById('projetarButton');
const atualizarButton = document.getElementById('atualizarButton');
const ajudaButton = document.getElementById('ajudaButton');
const pesquisarTexto = document.getElementById('pesquisarTexto');
const tamanhoFonteTexto = document.getElementById('tamanhoFonte');
const preview = document.getElementById('textoSelecionado');
const historico = document.getElementById('historico');
const ultimaPesquisa = document.getElementById('ultimaPesquisa');
const versoes = document.getElementById('versoes');

function salvarPreferencias(livro, capitulo, versiculo) {
    const preferencias = {
        fonte: Number(tamanhoFonteTexto.value),
        textoAtual: {
            livro: livro,
            capitulo: Number(capitulo),
            versiculo: Number(versiculo)
        },
        versao: versoes.value
    }

    fs.writeFile('data/preferencias.json', JSON.stringify(preferencias), erro => {
        if (erro) {
            alert('Erro ao salvar');
        }
    });
}

versoes.onchange = function () {
    biblia = fs.readFileSync('data/bibles/' + versoes.value + '.txt', 'utf-8');
}

tamanhoFonteTexto.onchange = function () {
    salvarPreferencias();
}

{ // Revelação do texto
    let livro;
    let capitulo;
    let versiculo;

    pesquisarButton.onclick = function () {
        let pesquisa;
        let indice;

        pesquisa = pesquisarTexto.value;

        while (pesquisa.indexOf('  ') != -1) { // Remover espaços múltiplos
            pesquisa = pesquisa.replace(/  /g, ' ');
        }

        indice = pesquisa.indexOf(' ');
        livro = pesquisa.substring(0, indice).replace(' ', '');
        livro = getLivro(livro);
        pesquisa = pesquisa.substring(indice + 1);

        indice = pesquisa.indexOf(' ');
        capitulo = pesquisa.substring(0, indice).replace(' ', '');
        versiculo = pesquisa.substring(indice + 1);

        ultimaPesquisa.innerHTML = `${livro} ${capitulo}:${versiculo}`;
        historico.value += ultimaPesquisa.innerHTML + '\n';
        let texto = queryTexto(biblia, livro, capitulo, versiculo);
        preview.value = texto != null ? texto + getRepresentacao(livro, capitulo, versiculo) : 'Texto inexistente';

        atualizarButton.click();
    }

    atualizarButton.onclick = function () {
        fs.writeFile('./data/texto.txt', preview.value, () => { });
        salvarPreferencias(livro, capitulo, versiculo);
    }

    function avancarVerso() {
        if (!queryTexto(biblia, livro, capitulo, Number(versiculo) + 1)) {
            preview.value = 'Não há versículos posteriores';
        }
        else {
            preview.value = queryTexto(biblia, livro, capitulo, ++versiculo) + getRepresentacao(livro, capitulo, versiculo);
            atualizarButton.click();
        }
    }

    function voltarVerso() {
        if (versiculo > 1) {
            preview.value = queryTexto(biblia, livro, capitulo, --versiculo) + getRepresentacao(livro, capitulo, versiculo);
            atualizarButton.click();
        }
        else {
            preview.value = 'Não há versículos anteriores';
        }
    }

    function adicionarVerso() { // Em processo............
        if (!queryTexto(biblia, livro, capitulo, Number(versiculo) + 1)) {
            preview.value = 'Não há versículos posteriores';
        }
        else {
            preview.value += '<br>' + queryTexto(biblia, livro, capitulo, ++versiculo) + getRepresentacao(livro, capitulo, versiculo);
            atualizarButton.click();
        }
    }
}

projetarButton.onclick = function () {
    window.open('projetar.html', 'big', 'fullscreen=no');
}

ajudaButton.onclick = function () {
    window.open('ajuda.html');
}

pesquisarTexto.addEventListener('keydown', e => {
    if (e.keyCode == 13) {
        pesquisarButton.click();
    }
});

document.addEventListener('keydown', e => {
    if (e.keyCode == 115) { // F4
        pesquisarTexto.select();
    }

    if (e.keyCode == 116) { // F5
        projetarButton.click();
    }

    if (e.keyCode == 117) { // F6
        atualizarButton.click();
    }

    if (e.keyCode == 119) { // F8
        //adicionarVerso();
    }

    if (e.keyCode == 120 || e.keyCode == 34) { // F9 e PageDown
        voltarVerso();
    }

    if (e.keyCode == 121 || e.keyCode == 33) { // F10 e PageUp
        avancarVerso();
    }

    if (e.keyCode == 112) { // F1
        ajudaButton.click();
    }
});

// Ao iniciar
const fs = require('fs');

let biblia = fs.readFileSync('data/bibles/ara.txt', 'utf-8');
tamanhoFonteTexto.value = JSON.parse(fs.readFileSync('data/preferencias.json', 'utf-8')).fonte;