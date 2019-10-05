def ultima_ocorrencia(string, ocorrencia):
    for n in range(1, len(string) + 1):
        if string[-n] == ocorrencia:
            return len(string) - n
    return None


def get_liv_cap_ver(ref):
    ref = ref.replace('[', '').replace(']', '')
    ref = ref.split(':')
    return ref


livros = [
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


def get_id_liv(liv):
    for n in range(len(livros)):
        if livros[n] == liv:
            return n + 1


sql = ''
with open('bibles_txt/ara_py.txt', encoding='utf-8') as file:
    def readline():
        return file.readline().replace('\n', '')

    while True:
        ref = readline()
        text = readline()
        if text == '' or ref == '':
            break
        else:
            ref = get_liv_cap_ver(ref)
            liv = ref[0]
            cap = ref[1]
            ver = ref[2]
            sql += ("INSERT INTO textos (id_versao, id_livro, capitulo, versiculo, texto) VALUES (%s, %s, %s, %s, '%s');\n" %
            (1, get_id_liv(liv), cap, ver, text))

with open('sql/insert_textos_ara.sql', 'w') as file:
    file.write(sql)
input('Pressione enter para continuar...')
