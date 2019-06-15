import sqlite3
from unicodedata import normalize

nomeLivros = [
    'Gênesis', 'Êxodo', 'Levítico',
    'Números', 'Deuteronômio', 'Josué',
    'Juízes', 'Rute', '1 Samuel',
    '2 Samuel', '1 Reis', '2 Reis',
    '1 Crônicas', '2 Crônicas', 'Esdras',
    'Neemias', 'Ester', 'Jó',
    'Salmos', 'Provérbios', 'Eclesiastes',
    'Cantares de Salomão', 'Isaías', 'Jeremias',
    'Lamentações', 'Ezequiel', 'Daniel',
    'Oséias', 'Joel', 'Amós',
    'Obadias', 'Jonas', 'Miquéias',
    'Naum', 'Habacuque', 'Sofonias',
    'Ageu', 'Zacarias', 'Malaquias',
    'Mateus', 'Marcos', 'Lucas',
    'João', 'Atos dos Apóstolos', 'Romanos',
    '1 Coríntios', '2 Coríntios', 'Gálatas',
    'Efésios', 'Filipenses', 'Colossenses',
    '1 Tessalonicenses', '2 Tessalonicenses', '1 Timóteo',
    '2 Timóteo', 'Tito', 'Filemon',
    '1 Pedro', '2 Pedro', '1 João',
    '2 João', '3 João', 'Hebreus',
    'Tiago', 'Judas', 'Apocalipse'
]

siglasLivros = ['gn', 'ex', 'lv', 'nm', 'dt', 'js', 'jz', 'rt', '1 sm',
                '2 sm', '1 ss', '2 ss', '1 cr', '2 cr', 'ed', 'ne', 'et', 'jo', 'sl', 'pv', 'ec',
                'ct', 'is', 'jr', 'lm', 'ez', 'dn', 'os', 'jl', 'am', 'ob', 'jn', 'mq', 'na',
                'hc', 'sf', 'ag', 'zc', 'ml', 'mt', 'mc', 'lc', 'jo', 'at', 'rm', '1 co', '2 co',
                'gl', 'ef', 'fp', 'cl', '1 ts', '2 ts', '1 tm', '2 tm', 'tt', 'fm', '1 pe', '2 pe',
                '1 jo', '2 jo', '3 jo', 'hb', 'tg', 'jd', 'ap']


def removerAcentos(texto):
    return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')


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
            livroSemAcento = removerAcentos(livro)
            textoSemAcento = removerAcentos(texto)
            sigla = siglasLivros[nomeLivros.index(livro)]
            cursor.execute("insert into %s(sigla, livro, capitulo, versiculo, texto, livroSemAcento, textoSemAcento) values('%s', '%s', %d, %d, '%s', '%s', '%s')" % (
                versao, sigla, livro, int(capitulo), int(versiculo), texto, livroSemAcento, textoSemAcento))
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
    'create table if not exists ara(sigla varchar, livro varchar, capitulo integer, versiculo integer, texto varchar, livroSemAcento varchar, textoSemAcento varchar)')

insertBibleInDatabase('ara', 'data/bibles/ara-py.txt')
