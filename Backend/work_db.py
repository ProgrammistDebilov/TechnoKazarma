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
    cur.execute(f'SELECT * FROM users WHERE login = "{str(login)}"')
    row = cur.fetchall()

    if row:
        print('логин занят')
        return 0 #логин занят
    else:
        cur.execute(f'INSERT INTO users (login, password, role) VALUES("{str(login)}", "{str(password)}", "{str(role)}");')
        print("норм")
        if role == 'i':
            cur.execute(
                f'INSERT INTO installers (username, alacrity, width, length) VALUES("{str(login)}", 1, "{width}", "{length}");')
            print("норм инсталятор")
        con.commit()
        return 1

def sign_in(options):
    con = sql3.connect(db_path)
    cur = con.cursor()

    login = options[0]
    pasword = options[1]

    cur.execute(f'SELECT * FROM users WHERE login = {str(login)} AND password = {str(pasword)}')
    row = cur.fetchall()

    if row:
        print('круто')
        return 1#верные данные
    else:
        print('не круто')
        return 0#неверные данные

def add_order(adress, installer):
    con = sql3.connect('Installs.db')
    cur = con.cursor()

    alacrity = cur.execute(f'SELECT alacrity FROM installers WHERE username = {installer}').fetchall()[0][0]
    if alacrity == 1:
        cur.execute(f'INSERT INTO orders (adress, installer) VALUES ("{str(adress)}", {str(installer)})')
    cur.execute(f'UPDATE installers SET alacrity = 0 WHERE username = {installer}')

    con.commit()



def finish_order(installer):
    con = sql3.connect('Installs.db')
    cur = con.cursor()

    cur.execute(f'DELETE * FROM orders WHERE installer = {installer}')
    con.commit()



def return_aval_in():
    con = sql3.connect('Installs.db')
    cur = con.cursor()

    cur.execute('SELECT username FROM installers WHERE alacrity = 1')
    installs = cur.fetchall()

    availible_installs = []
    for i in installs:
        availible_installs.append(i[0])

    print(availible_installs)
    return availible_installs


def return_location(login):
    con = sql3.connect('Installs.db')
    cur = con.cursor()

    cur.execute(f'SELECT width, length FROM installers WHERE username = "{str(login)}"')
    loc = cur.fetchall()[0]
    con.commit()
    print(loc)

def return_role(login):
    con = sql3.connect('Installs.db')
    cur = con.cursor()

    cur.execute(f'SELECT role FROM users WHERE login = {str(login)}')
    role = cur.fetchall()[0][0]
    print(role)
    if role == 'i':
        role_ru = 'Инсталятор'
    elif role == 'd':
        role_ru = 'Диспетчер'
    print(role_ru)
    con.commit()
    return role_ru

def insert_location(login, width, length):
    con = sql3.connect('Installs.db')
    cur = con.cursor()

    cur.execute(f'UPDATE installers SET width = {width}, length = {length} WHERE username = {str(login)}')
    con.commit()

options = [123, 123]
options_all = ['fgh', 'inst1', 'Инсталятор', 234.543, 8739.432]

if __name__ == '__main__':
    # sign_in(options)
    # sign_up(options_all)
    return_aval_in()
    add_order('ул. Путина 36', '123')
    return_location('fgh')
    # return_role('123')
    # insert_location(123, 23.567, 45.432)
