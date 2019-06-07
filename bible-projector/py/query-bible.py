# coding=UTF-8

import base64
import sqlite3
from unicodedata import normalize
import sys


def isInt(s):
    try:
        int(s)
        return True
    except:
        return False


def removerAcentos(texto):
    return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')


def adicionarEspacoNomeLivro(x=''):
    for n in range(len(x)):
        if x[n] != ' ' and not isInt(x[n]):
            break
        else:
            if isInt(x[n]) and x[n + 1] != ' ' and not isInt(x[n + 1]):
                x = list(x)
                x.insert(n + 1, ' ')
                break
    return ''.join(x)


def interpretarPesquisa(pesquisa=''):
    try:
        referencia = ''
        referencia = pesquisa.replace(':', ' ')
        while referencia.find('  ') > -1:
            referencia = referencia.replace('  ', ' ')
        if referencia[0] == ' ':
            referencia = referencia[1:]
        if referencia[-1] == ' ':
            referencia = referencia[0:-1]
        referencia = referencia[::-1].replace(' ', ':', 2)[::-1]
        referencia = adicionarEspacoNomeLivro(referencia)
        referencia = referencia.split(':')

        if isInt(referencia[1]) and isInt(referencia[2]):
            return ['referencia'] + referencia
        else:
            return ['texto'] + [pesquisa]
    except:
        return ['texto'] + [pesquisa]


def pesquisarPorReferencia(versao, livro, capitulo, versiculo):
    sigla = removerAcentos(livro)
    livro = '%' + sigla + '%'
    capitulo = str(capitulo)
    versiculo = str(versiculo)

    cursor.execute("select livro, capitulo, versiculo, texto from %s where sigla = '%s' and capitulo = %s and versiculo = %s"
                   % (versao, sigla, capitulo, versiculo))

    resultado = cursor.fetchone()

    if resultado == None:
        cursor.execute("select livro, capitulo, versiculo, texto from %s where livroSemAcento like '%s' and capitulo = %s and versiculo = %s"
                       % (versao, livro, capitulo, versiculo))
        resultado = cursor.fetchone()

    return [resultado]


def pesquisarPorTexto(versao, pesquisa):
    pesquisa = '%' + pesquisa + '%'
    cursor.execute("select * from %s where textoSemAcento like '%s'" %
                   (versao, removerAcentos(pesquisa)))

    return cursor.fetchall()


def pesquisar(pesquisa):
    versao = 'ara'

    pesquisa = interpretarPesquisa(pesquisa)
    send = []

    if pesquisa[0] == 'referencia':
        livro = pesquisa[1]
        capitulo = pesquisa[2]
        versiculo = pesquisa[3]
        return pesquisarPorReferencia(versao, livro, capitulo, versiculo)
    else:
        return pesquisarPorTexto(versao, pesquisa[1])


connection = sqlite3.connect('data/biblia.db')
cursor = connection.cursor()

pesquisa = sys.argv[1]
q = pesquisar(pesquisa.lower())

message = ''

for n in range(len(q[0])):
    message += str(q[0][n])

    if n < len(q[0]) - 1:
         message += '<@#$&>'

message = base64.b64encode(message.encode('utf-8')).decode('utf-8')
print(message)