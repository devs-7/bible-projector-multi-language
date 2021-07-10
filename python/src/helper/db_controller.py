import sqlite3


def get_connection():
    return sqlite3.connect('data/bible.db')


def get_cursor():
    return get_connection().cursor()


def query(sql):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(sql)
    dados = cursor.fetchall()
    connection.close()
    return dados


def query_dict(tabela, colunas, where=None):
    sql_colunas = ''
    for c in colunas:
        sql_colunas += c + ','
    sql_colunas = sql_colunas[0:len(sql_colunas) - 1]

    linhas = query(f'''
        SELECT {sql_colunas} FROM {tabela} {'WHERE ' + where if where != None else ''}
    ''')

    dicionario_array = []
    for linha in linhas:
        dicionario = {}
        for n in range(len(colunas)):
            dicionario[colunas[n]] = linha[n]
        dicionario_array.append(dicionario)

    return dicionario_array


def query_id(tabela, colunas, id):
    result = query_dict(tabela, colunas, f'id = {id}')
    if len(result) > 0:
        return result[0]
    else:
        return None
