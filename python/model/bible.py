import helper.db_controller as db
from helper.strings import normalizar
from model.db_class import DbClass

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
    q_split = normalizar(q)
    q_split = q.replace(':', ' ')
    while q_split.__contains__('  '):
        q_split = q_split.replace('  ', ' ')
    q_split = q_split.split(' ')

    if len(q_split) >= 3:
        ver: str = q_split.pop()
        cap: str = q_split.pop()
        liv: str = ' '.join(q_split)

        if not cap.isnumeric() or not ver.isnumeric():
            ver = 'null'
            cap = 'null'
            liv = 'null'
    else:
        ver = 'null'
        cap = 'null'
        liv = 'null'

    result_query = db.query(f"""
        {SQL_SELECT}
        WHERE
        livros._sigla like '{liv}' AND
        textos.capitulo = '{cap}' AND
        textos.versiculo = '{ver}' AND
        versoes.versao LIKE '{versao}'
    """)

    if len(result_query) == 0:
        result_query = db.query(f"""
            {SQL_SELECT}
            WHERE
            livros._nome LIKE '%{liv}%' AND
            textos.capitulo = '{cap}' AND
            textos.versiculo = '{ver}' AND
            versoes.versao LIKE '{versao}'
        """)

    if (len(result_query) == 0):
        result_query = db.query(f"""
            {SQL_SELECT}
            WHERE
            textos.texto LIKE '%{q.replace(' ', '%')}%' AND
            versoes.versao LIKE '{versao}'
            ORDER BY livros.id, textos.capitulo, textos.versiculo
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


class Bible(DbClass):
    def __init__(self, versao="ARA", ref: dict = None):
        self.liv = None
        self.cap = None
        self.ver = None
        self.text = None
        self.versao = versao
        self.listener = None
        self.historico = []
        self.ocorrencias = []

        if ref is not None:
            self.set_ref(ref)

    def set_ref(self, ref):
        self.set_valores_dict(ref)

    def ref(self):
        return {
            'liv': self.liv,
            'cap': self.cap,
            'ver': self.ver,
            'text': self.text,
            'versao': self.versao
        }

    def run_listener(self):
        if self.listener is not None:
            self.listener(self.ref())

    def query(self, q):
        ocorrencias = query(q, self.versao)
        if ocorrencias is not None:
            self.set_valores_dict(ocorrencias[0])
            self.historico.append(self.ref())
            self.ocorrencias = ocorrencias
            self.run_listener()
        else:
            self.set_valores_dict(self.historico[-1])
        return ocorrencias

    def next(self):
        self.ver += 1
        self.query(self.referencia())

    def back(self):
        self.ver -= 1
        self.query(self.referencia())

    def referencia(self):
        return format_reference({
            'liv': self.liv,
            'cap': self.cap,
            'ver': self.ver
        })
