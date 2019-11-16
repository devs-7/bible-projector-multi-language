import helper.db_controller as db

from datetime import date


def add(id_contato):
    today = date.today().__format__("%Y%m%d")
    connection = db.get_connection()
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO exibicoes (id_contato, data) VALUES ({id_contato}, {today})")
    connection.commit()

def count(id_contato):
    datas = db.query(f"SELECT data FROM exibicoes WHERE id_contato = {id_contato}")
    return len(datas)
