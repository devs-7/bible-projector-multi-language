import sqlite3


def insertBibleInDatabase(versao, local):
    bible = open(local, 'r', encoding='UTF-8')
    livro = ''
    capitulo = 0
    versiculo = 0
    cont = 0

    print('Instalando versão "%s"...' % versao)

    for linha in bible:
        if linha.find('[') > -1:
            linha = linha.replace('[', '')
            linha = linha.replace(']', '')
            linha = linha.replace('\n', '')
            linha = linha.split(':')
            livro = linha[0]
            capitulo = linha[1]
            versiculo = linha[2]
        else:
            texto = linha.replace('\n', '')
            cursor.execute("insert into %s(livro, capitulo, versiculo, texto) values('%s', %d, %d, '%s')" % (
                versao, livro, int(capitulo), int(versiculo), texto))
            cont += 1
            if cont == 1000:
                cont = 0
                connection.commit()
    connection.commit()

    print('A versão "%s" foi instalada com sucesso.' % versao)
    bible.close()


connection = sqlite3.connect('data/biblia.db')
cursor = connection.cursor()

cursor.execute(
    'create table if not exists ara(livro varchar, capitulo integer, versiculo integer, texto varchar)')

insertBibleInDatabase('ara', 'data/bibles/ara-py.txt')
