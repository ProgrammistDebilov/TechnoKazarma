import sqlite3 as sql3

con = sql3.connect('installs.db')
cur = con.cursor()

# cur.execute('CREATE TABLE users ('
#             'id INTEGER PRIMARY KEY AUTOINCREMENT, '
#             'name TEXT, '
#             'surname TEXT, '
#             'login TEXT, '
#             'password TEXT, '
#             'role TEXT)')

# cur.execute('DROP TABLE installers')

# cur.execute('CREATE TABLE installers ('
#             'id INTEGER PRIMARY KEY AUTOINCREMENT, '
#             'name TEXT, '
#             'surname TEXT, '
#             'username TEXT, '
#             'alacrity INTEGER, '
#             'FOREIGN KEY (username)  REFERENCES users (login))')

# cur.execute('CREATE TABLE orders ('
#             'id INTEGER PRIMARY KEY AUTOINCREMENT, '
#             'width TEXT, '
#             'length TEXT, '
#             'installer INTEGER, '
#             'FOREIGN KEY (installer) REFERENCES installers (id))')

# cur.execute(f'INSERT INTO users (name, surname, login, password, role) VALUES("Иван", "Иванов", "klop22", "123", "installer");')


con.commit()

