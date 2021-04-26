import sqlite3

connection = sqlite3.connect("db7.sqlite3")
cursor = connection.cursor()
cursor.execute("CREATE TABLE car(id integer, mark text, model text, volume integer, year text, color text)")

connection.close()