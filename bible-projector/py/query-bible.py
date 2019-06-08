# coding=UTF-8

import base64
import sqlite3
from unicodedata import normalize
import sys


def removerAcentos(texto):
    return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')


def pesquisar(pesquisa, versao='ara'):
    def select():
        cursor.execute("select * from %s where textoSemAcento like '%s'" %
                       (versao, removerAcentos(pesquisa)))
        return cursor.fetchall()

    pesquisa = '%' + pesquisa + '%'
    resultado = select()

    if len(resultado) == 0:
        pesquisa = pesquisa.replace(' ', '%')
        resultado = select()

    if len(resultado) == 0:
        return None
    else:
        return resultado


connection = sqlite3.connect('data/biblia.db')
cursor = connection.cursor()

pesquisa = sys.argv[1]
q = pesquisar(pesquisa.lower())
message = ''

if q != None:
    for n in range(len(q[0])):
        message += str(q[0][n])

        if n < len(q[0]) - 1:
            message += '<@#$&>'

    message = base64.b64encode(message.encode('utf-8')).decode('utf-8')

print(message)
