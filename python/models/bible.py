import helper.db_controller as db
from helper.strings import normalizar

def query_one(q):
    q = query(q)
    if q is not None:
        return q[0]
    else:
        return None


def query(q):
    q = q.replace(':', ' ')
    q = normalizar(q)
    q = q.split(' ')
    ver = q.pop()
    cap = q.pop()
    liv = ' '.join(q)

    result_query = db.query(add_join(f"""
                    livros._sigla like '{liv}'
                    AND
                    textos.capitulo = {cap}
                    AND
                    textos.versiculo = {ver}
                """))
    if len(result_query) == 0:
        result_query = db.query(add_join(f"""
                        livros._nome like '%{liv}%'
                        AND
                        textos.capitulo = {cap}
                        AND
                        textos.versiculo = {ver}
                    """))

    if len(result_query) > 0:
        lista = []
        for n in result_query:
            lista.append({
                'liv': n[0],
                'cap': n[1],
                'ver': n[2],
                'text': n[3],
            })
        return lista

    else:
        return None


def add_join(s):
    return f"""
        SELECT livros.nome, textos.capitulo, textos.versiculo, textos.texto 
        FROM textos
        JOIN livros on textos.id_livro = livros.id
        WHERE 
    """ + s
