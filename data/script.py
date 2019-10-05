import sqlite3

connection = sqlite3.connect('bible.db')
cursor = connection.cursor()

cursor.execute('select * from livros')