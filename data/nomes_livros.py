from unidecode import unidecode

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

sql = ''
for l in livros:
    sql += "insert into livros (nome, _nome) values ('%s', '%s');\n" % (l, unidecode(l))

with open('sql/insert_livros.sql', 'w') as file:
    file.write(sql)