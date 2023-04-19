import sqlite3 as sql3
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "Installs.db")
def sign_up(options):
    con = sql3.connect(db_path)
    cur = con.cursor()
    login = options[0]
    password = options[1]
    role = options[2]
    width = 0
    length = 0
    if role == 'Инсталятор':
        role = 'i'
        width = options[3]
        length = options[4]
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
                f'INSERT INTO installers (username, alacrity, width, length) VALUES({login}, 1, {width}, {length});')
        con.commit()
        return 1

def sign_in(options):
    con = sql3.connect(db_path)
    cur = con.cursor()

    login = options[0]
    pasword = options[1]

    cur.execute(f'SELECT * FROM users WHERE login = "{login}" AND password = "{pasword}"')
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

    cur.execute('SELECT * FROM installers')

    availible_installs = cur.fetchall()
    print(availible_installs)
    return availible_installs

if __name__ == '__main__':
    # options = [123, 123]
    # options_all = [123, 123, 'Инсталятор', 'test', 'test']
    # sign_in(options)
    # sign_up(options_all)
    return_aval_in()
