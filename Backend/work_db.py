import sqlite3 as sql3

def sign_up(options):
    con = sql3.connect('Installs.db')
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
    cur.execute(f'SELECT * FROM users WHERE login = {login}')
    row = cur.fetchall()

    if row:
        return 0 #логин занят
    else:
        cur.execute(f'INSERT INTO users (login, password, role) VALUES({login}, {password}, "{role}");')
        if role == 'i':
            cur.execute(
                f'INSERT INTO installers (username, alacrity, adress) VALUES({login}, 1, "{addres}");')
        con.commit()
        return 1

def sign_in(options):
    con = sql3.connect('Installs.db')
    cur = con.cursor()

    login = options[0]
    pasword = options[1]

    cur.execute(f'SELECT * FROM users WHERE login = {login} AND password = "{pasword}"').fetchall()
    row = cur.fetchall()

    if row:
        return 1#верные данные
    else:
        return 0#неверные данные




def add_order(adress, installer):

    con = sql3.connect('Installs.db')
    cur = con.cursor()
    alacrity = cur.execute(f'SELECT alacrity FROM installers WHERE username = {installer}').fetchall()
    if alacrity == 1:
        cur.execute(f'INSERT INTO orders (adress, installer) VALUES ({adress}, {installer})')

    con.commit()


def return_aval_in():
    con = sql3.connect('Installs.db')
    cur = con.cursor()
    cur.execute('SELECT username FROM installers WHERE alacrity = 1')
    availible_installs = cur.fetchall()

    return availible_installs


options = [123, 123]
options_all = [123, 123, 'Инсталятор', 'test']
sign_in(options)
