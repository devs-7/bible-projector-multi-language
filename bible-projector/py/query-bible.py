import sqlite3


def isInt(s):
    try:
        int(s)
        return True
    except:
        return False


def interpretarPesquisa(pesquisa=''):
    try:
        referencia = pesquisa.replace(':', ' ')
        referencia = referencia[::-1].replace(' ', ':', 2)[::-1]
        referencia = referencia.split(':')

        if isInt(referencia[1]) and isInt(referencia[2]):
            return ['referencia'] + referencia
        else:
            return ['texto'] + [pesquisa]
    except:
        return ['texto'] + [pesquisa]


def pesquisarPorReferencia(versao, livro, capitulo, versiculo):
    livro = '%' + livro + '%'
    capitulo = str(capitulo)
    versiculo = str(versiculo)
    cursor.execute("select * from %s where livro like '%s' and capitulo = %s and versiculo = %s"
                   % (versao, livro, capitulo, versiculo))

    return [cursor.fetchone()]


def pesquisarPorTexto(versao, pesquisa):
    pesquisa = '%' + pesquisa + '%'
    cursor.execute("select * from %s where texto like '%s'" %
                   (versao, pesquisa))

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

p = pesquisar('apoca 22 21')

for n in p:
    print(n)

# connection.create_collation()
