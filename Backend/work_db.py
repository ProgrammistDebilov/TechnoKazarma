import sqlite3 as sql3

def sign_up(options):
    con = sql3.connect('installs.db')
    cur = con.cursor()
    print(options)
    login = options[0]
    password = options[1]
    role = options[2]
    addres = 0

    if role == 'Инсталятор':
        role = 'i'
        addres = options[3]
    elif role == 'Диспетчер':
        role = 'd'
    row = cur.execute(f'SELECT * FROM users WHERE login = {login}')

    if row:
        return 0 #логин занят
    else:
        cur.execute(
            f'INSERT INTO users (login, password, role) VALUES({login}, {password}, {role});')
        if role == 'i':
            cur.execute(
                f'INSERT INTO installers (username, alacrity) VALUES({login}, {password}, 1, {addres});')
        con.commit()
        return 1

def sign_in(options):
    con = sql3.connect('installs.db')
    cur = con.cursor()

    login = options[0]
    pasword = options[1]

    row = cur.execute(f'SELECT * FROM users WHERE login = {login} AND WHERE password = {pasword}').fetchall()

    if row:
        return 1#верные данные
    else:
        return 0#неверные данные




def add_order(adress, installer):

    con = sql3.connect('installs.db')
    cur = con.cursor()
    alacrity = cur.execute(f'SELECT alacrity FROM installers WHERE username = {installer}').fetchall()
    if alacrity == 1:
        cur.execute(f'INSERT INTO orders (adress, installer) VALUES ({adress}, {installer})')

    con.commit()