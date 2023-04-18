import sqlite3 as sql3

def sign_up(options):
    con = sql3.connect('installs.db')
    cur = con.cursor()

    name = options[0]
    surname = options[1]
    login = options[2]
    password = options[3]
    role = options[4]
    if role == 'инсталятор':
        role = 'i'
    elif role == 'диспетчер':
        role = 'd'
    row = cur.execute(f'SELECT * FROM users WHERE login = {login}')

    if row:
        print('Не не не, этот логин уже используется')
    else:
        cur.execute(
            f'INSERT INTO users (name, surname, login, password, role) VALUES({name}, {surname}, {login}, {password}, {role});')

    con.commit()

def sign_in(options):
    con = sql3.connect('installs.db')
    cur = con.cursor()

    login = options[0]
    pasword = options[1]

    row = cur.execute(f'SELECT * FROM users WHERE login = {login} AND WHERE password = {pasword}')

    if row:
       print('good')
    else:
        print('bad')
