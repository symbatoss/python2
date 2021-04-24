import sqlite3

connection = sqlite3.connect("db.sqlite3")
cursor = connection.cursor()

class Students:
    def __init__(self, name, surname, id):
        self.name = name
        self.surname = surname
        self.id = id
    def add(self):
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO Students values (?, ?, ?)",
                       (self.name, self.surname, self.id))
        connection.commit()


student1 = Students("Kanykei", "Asanova", 1)
student1.add()
student2 = Students("Arkadiy", "Son", 2)
student2.add()




