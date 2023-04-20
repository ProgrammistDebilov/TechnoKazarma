import sqlite3 as sql3

con = sql3.connect('Installs.db')
cur = con.cursor()
#
# cur.execute('CREATE TABLE users ('
#             'id INTEGER PRIMARY KEY AUTOINCREMENT, '
#             'login TEXT, '
#             'password TEXT, '
#             'role TEXT)')

# cur.execute('DROP TABLE installers')
# cur.execute('DROP TABLE users')
# cur.execute('DROP TABLE orders')

# cur.execute('CREATE TABLE installers ('
#             'id INTEGER PRIMARY KEY AUTOINCREMENT, '
#             'username TEXT, '
#             'alacrity INTEGER, '
#             'width TEXT, '
#             'length TEXT)')
#
# cur.execute('CREATE TABLE orders ('
#             'id INTEGER PRIMARY KEY AUTOINCREMENT, '
#             'adress TEXT, '
#             'installer INTEGER, '
#             'state INTEGER, '
#             'start_time TEXT, '
#             'end_time TEXT, '
#             'comment TEXT)')

print('Users')
cur.execute(f'SELECT * FROM users')
print(cur.fetchall())

print('Installers')
cur.execute('SELECT * FROM installers')
print(cur.fetchall())

# cur.execute('DELETE FROM users WHERE id = 5 OR id = 6 OR id = 7')
con.commit()



con.commit()

