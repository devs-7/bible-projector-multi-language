import helper.db_controller as db
from helper.strings import normalizar

SQL_SELECT = """
    SELECT livros.nome, textos.capitulo, textos.versiculo, textos.texto, versoes.versao
    FROM textos
    JOIN livros ON textos.id_livro = livros.id
    JOIN versoes ON textos.id_versao = versoes.id
"""


def query_one(q, versao='ARA'):
    q = query(q, versao)
    if q is not None:
        return q[0]
    else:
        return None


def query(q, versao='ARA'):
    q = q.replace(':', ' ')
    while q.__contains__('  '):
        q = q.replace('  ', ' ')
    q = normalizar(q)
    q = q.split(' ')
    ver = q.pop()
    cap = q.pop()
    liv = ' '.join(q)

    result_query = db.query(f"""
        {SQL_SELECT}
        WHERE
        livros._sigla like '{liv}' AND
        textos.capitulo = {cap} AND
        textos.versiculo = {ver} AND
        versao like '{versao}'
    """)
    if len(result_query) == 0:
        result_query = db.query(f"""
            {SQL_SELECT}
            WHERE
            livros._nome like '%{liv}%' AND
            textos.capitulo = {cap} AND
            textos.versiculo = {ver}
        """)

    if len(result_query) > 0:
        lista = []
        for n in result_query:
            lista.append({
                'liv': n[0],
                'cap': n[1],
                'ver': n[2],
                'text': n[3],
                'versao': n[4]
            })
        return lista

    else:
        return None


def format_reference(ref: dict):
    return f"{ref['liv']} {ref['cap']}:{ref['ver']}"


class Bible:
    def __init__(self, versao="ARA"):
        self.versao = versao

    def query(self, q):
        return query(q, self.versao)

    def query_one(self, q):
        return query_one(q, self.versao)
