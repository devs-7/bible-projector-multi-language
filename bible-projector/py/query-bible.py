import sqlite3


def interpretarPesquisa(pesquisa=''):
    pesquisa = pesquisa.replace(':', ' ')
    pesquisa = pesquisa[::-1].replace(' ', ':', 2)[::-1]
    pesquisa = pesquisa.split(':')

    return pesquisa


def pesquisar(pesquisa):
    versao = 'ara'

    pesquisa = interpretarPesquisa(pesquisa)
    livro = pesquisa[0]
    capitulo = pesquisa[1]
    versiculo = pesquisa[2]

    livro = '%' + livro + '%'
    capitulo = str(capitulo)
    versiculo = str(versiculo)
    cursor.execute("select * from %s where livro like '%s' and capitulo = %s and versiculo = %s"
                   % (versao, livro, capitulo, versiculo))

    pesquisa = cursor.fetchall()
    send = []
    send.append(pesquisa[0][0] + ' ' +
                str(pesquisa[0][1]) + ':' + str(pesquisa[0][2]))
    send.append(pesquisa[0][3])

    return send


connection = sqlite3.connect('data/biblia.db')
cursor = connection.cursor()

print(pesquisar('gên 1 2'))
