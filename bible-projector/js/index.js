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

var livro;
var capitulo;
var versiculo;
var biblia;

const fs = require('fs');

function salvarPreferencias(livro, capitulo, versiculo, texto) {
    const preferencias = {
        fonte: Number(tamanhoFonteTexto.value),
        textoAtual: {
            livro: livro,
            capitulo: Number(capitulo),
            versiculo: Number(versiculo),
            texto: texto
        },
        versao: versoes.value
    }

    fs.writeFile('data/preferencias.json', JSON.stringify(preferencias), erro => {
        if (erro) {
            preview.value = 'Erro ao enviar texto para o projetor.';
        }
    });
}

function projetar() {
    window.open('projetar.html', 'Projetor', 'fullscreen=no');
}

function ajuda() {
    window.open('ajuda.html', 'Ajuda');
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

function atualizar() {
    salvarPreferencias(livro, capitulo, versiculo, preview.value);
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
    function pesquisaEncontrada(livro, capitulo, versiculo, texto) {
        ultimaPesquisa.innerHTML = `${livro} ${capitulo}:${versiculo}`;
        preview.value = texto + getRepresentacao(livro, capitulo, versiculo);
        if (projetar) {
            atualizar();
            atualizarHistorico();
        }
    }

    if (!!pesquisa) {
        let referencia = interpretarPesquisa(pesquisa);
        livro = referencia.livro;
        capitulo = referencia.capitulo;
        versiculo = referencia.versiculo;

        if (!!livro && !!capitulo && !!versiculo) pesquisarTexto.value = `${livro} ${capitulo}:${versiculo}`;

        let texto = queryTexto(biblia, livro, capitulo, versiculo);

        if (texto != null) pesquisaEncontrada(livro, capitulo, versiculo, texto);
        else {
            const query = queryBible(biblia, pesquisa);

            if (!query) {
                if (projetar) {
                    preview.value = '';
                    atualizar();
                }
                preview.value = 'Texto inexistente';
            }
            else {
                livro = query.livro;
                capitulo = query.capitulo;
                versiculo = query.versiculo;
                texto = query.texto;
                pesquisaEncontrada(livro, capitulo, versiculo, texto);
            }
        }
    }
}

pesquisarButton.onclick = () => pesquisar(true);
atualizarButton.onclick = atualizar;
tamanhoFonteTexto.onchange = salvarPreferencias;
projetarButton.onclick = projetar;
ajudaButton.onclick = ajuda;

versoes.onchange = function () {
    biblia = fs.readFileSync('data/bibles/' + versoes.value + '.txt', 'utf-8');
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
    if (e.keyCode == 116) projetar(); // F5
    if (e.keyCode == 117) atualizar(); // F6
    if (e.keyCode == 119) { } // F8
    if (e.keyCode == 120 || e.keyCode == 34) voltarVerso(); // F9 e PageDown
    if (e.keyCode == 121 || e.keyCode == 33) avancarVerso(); // F10 e PageUp
    if (e.keyCode == 112) ajuda(); // F1
});

const preferencias = JSON.parse(fs.readFileSync('data/preferencias.json', 'utf-8'));
tamanhoFonteTexto.value = preferencias.fonte;
biblia = fs.readFileSync('data/bibles/' + preferencias.versao + '.txt', 'utf-8');
versoes.value = preferencias.versao;