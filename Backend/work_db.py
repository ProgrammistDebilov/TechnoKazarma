import sqlite3 as sql3

def sign_up(options):
    con = sql3.connect('installs.db')
    cur = con.cursor()

    name = options[0]
    surname = options[1]
    login = options[2]
    password = options[3]
    role = options[4]
    width = options[5]
    length = options[6]

    if role == 'Инсталятор':
        role = 'i'
    elif role == 'Диспетчер':
        role = 'd'
    row = cur.execute(f'SELECT * FROM users WHERE login = {login}')

    if row:
        return 0 #логин занят
    else:
        cur.execute(
            f'INSERT INTO users (name, surname, login, password, role) VALUES({name}, {surname}, {login}, {password}, {role});')
        if role == 'i':
            cur.execute(
                f'INSERT INTO installers (name, surname, username, alacrity) VALUES({name}, {surname}, {login}, {password}, 1, {width}, {length});')
        con.commit()
        return 1

def sign_in(options):
    con = sql3.connect('installs.db')
    cur = con.cursor()

    login = options[0]
    pasword = options[1]

    row = cur.execute(f'SELECT * FROM users WHERE login = {login} AND WHERE password = {pasword}')

    if row:
       return 1#верные данные
    else:
        return 0#неверные данные



def add_order(adress, installer):
    con = sql3.connect('installs.db')
    cur = con.cursor()

    cur.execute(f'INSERT INTO orders (adress, installer) VALUES ({adress}, {installer})')

    con.commit()