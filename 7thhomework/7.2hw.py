import sqlite3

connection = sqlite3.connect("db7.sqlite3")
cursor = connection.cursor()


class Cars:

    def __init__(self, mark, model, volume, year, color, id):
        self.id = id
        self.mark = mark
        self.model = model
        self.volume = volume
        self.year = year
        self.color = color

    def save(self):
        cursor.execute(f"INSERT INTO cars values (?, ?, ?, ?, ?, ?)",
                       (self.id, self.mark, self.model, self.volume, self.year, self.color))
        connection.commit()

    def link(self, cls):
        # cursor.execute(f"CREATE TABLE ref (car_id integer, retailer_id integer,"
        #                f"FOREIGN KEY (car_id) references cars(id), "
        #                f"FOREIGN KEY (retailer_id) references retailers (id))")
        cursor.execute(f"INSERT INTO ref values (1, 1)")
        cursor.execute(f"INSERT INTO ref values (2, 1)")
        connection.commit()


class Retailer:

    def __init__(self, name, address, id):
        self.name = name
        self.address = address
        self.id = id

    def save(self):
        try:
            cursor.execute(f"INSERT INTO retailers values (?, ?, ?)",
                           (self.name, self.address, self.id))
            connection.commit()

        except Exception:
            # CREATE TABLE
            cursor.execute("CREATE TABLE retailers (name TEXT, address TEXT, id INTEGER)")
            cursor.execute(f"INSERT INTO retailers values (?, ?, ?)",
                           (self.name, self.address, self.id))
            connection.commit()


car = Cars("Ford", "Mondeo", 1.8, 2003, 'gold', 1)
car.save()
car2 = Cars("Honda", "Bit", 0.5, 2009, 'white', 2)
car2.save()
r = Retailer("Honda Center", "Bishkek", 1)
car.link(r)
