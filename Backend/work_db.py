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
        # print('логин занят')
        return 0 #логин занят
    else:
        cur.execute(f'INSERT INTO users (login, password, role) VALUES("{str(login)}", "{str(password)}", "{str(role)}");')
        # print("норм")
        if role == 'i':
            cur.execute(
                f'INSERT INTO installers (username, alacrity, width, length) VALUES("{str(login)}", 1, "{width}", "{length}");')
            # print("норм инсталятор")
        con.commit()
        return 1

def sign_in(options):
    con = sql3.connect(db_path)
    cur = con.cursor()

    login = options[0]
    pasword = options[1]

    cur.execute(f'SELECT * FROM users WHERE login = "{str(login)}" AND password = "{str(pasword)}"')
    row = cur.fetchall()

    if row:
        # print('круто')
        return 1#верные данные
    else:
        # print('не круто')
        return 0#неверные данные

def add_order(adress):
    con = sql3.connect(db_path)
    cur = con.cursor()

    cur.execute(f'INSERT INTO orders (adress, state) VALUES ("{str(adress)}", -1)')

    con.commit()

def start_order(installer,id, start_time):
    con = sql3.connect(db_path)
    cur = con.cursor()
    # id = return_id(adress)
    cur.execute(f'UPDATE orders SET state = 0, installer = "{str(installer)}", start_time = "{str(start_time)}" WHERE id = "{id}"')
    con.commit()
    cur.execute(f'UPDATE installers SET alacrity = 0 WHERE username = "{str(installer)}"')
    con.commit()
    # print('good')

def finish_order(installer, end_time):
    con = sql3.connect(db_path)
    cur = con.cursor()
    cur.execute(f'SELECT id FROM orders WHERE installer = {str(installer)} AND state = 0')
    id = cur.fetchall()[0][0]
    # print(id)
    cur.execute(f'UPDATE orders SET state = 1, end_time = {str(end_time)} WHERE installer = {str(installer)} and id = {id}')
    con.commit()

    cur.execute(f'UPDATE installers SET alacrity = 1 WHERE username = {str(installer)}')
    con.commit()


def return_orders():
    con = sql3.connect(db_path)
    cur = con.cursor()

    cur.execute(f'SELECT * FROM orders')
    orders_all_db = cur.fetchall()
    orders = []
    for x in orders_all_db:
        order_d = {'id' : x[0], 'adress' : x[1], 'installer' : x[2], 'state' : x[3], 'start_time' : x[4], 'end_time' : x[5]}
        orders.append(order_d)
    # print(orders)
    return orders

def return_orders_n():
    con = sql3.connect(db_path)
    cur = con.cursor()

    cur.execute(f'SELECT * FROM orders WHERE state = -1')
    orders_db = cur.fetchall()
    orders = []
    for order in orders_db:
        # print(order)
        order_d = {'id' : order[0], 'adress' : order[1]}
        orders.append(order_d)
    # print(orders)
    return orders
def return_aval_in():
    con = sql3.connect(db_path)
    cur = con.cursor()

    cur.execute('SELECT username FROM installers WHERE alacrity = 1')
    installs = cur.fetchall()

    availible_installs = []
    for i in installs:
        availible_installs.append(i[0])

    print(availible_installs)
    return availible_installs


def return_location(login):
    con = sql3.connect(db_path)
    cur = con.cursor()

    cur.execute(f'SELECT width, length FROM installers WHERE username = "{str(login)}"')
    loc = cur.fetchall()[0]
    con.commit()
    return loc

def return_role(login):
    con = sql3.connect(db_path)
    cur = con.cursor()

    cur.execute(f'SELECT role FROM users WHERE login = "{str(login)}"')
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
    con = sql3.connect(db_path)
    cur = con.cursor()

    cur.execute(f'UPDATE installers SET width = {width}, length = {length} WHERE username = {str(login)}')
    con.commit()

def return_installers():
    con = sql3.connect(db_path)
    cur = con.cursor()

    cur.execute(f'SELECT username, alacrity, width, length FROM installers')
    installers_db = cur.fetchall()
    installers = []
    for i in installers_db:
        installer_d = {'login' : i[0], 'alacrity' : i[1], 'width' : i[2], 'length' : i[3]}
        installers.append(installer_d)

    return installers




def return_id(adress):
    con = sql3.connect(db_path)
    cur = con.cursor()

    cur.execute(f'SELECT id FROM orders WHERE adress = "{str(adress)}" AND state = -1')
    id = cur.fetchall()[0][0]

    return id






options = [123, 123]
options_all = ['fgh', 'inst1', 'Инсталятор', 234.543, 8739.432]

if __name__ == '__main__':
    # sign_in(options)
    # sign_up(options_all)
    # return_aval_in()
    # add_order('ул. Путина 36')
    # print(return_location('fgh'))
    # return_role('123')
    # insert_location(123, 23.5, 45.432)
    # finish_order(123, '18.20')
    # print(return_installers())
    start_order(123, 'ул. Путина 36', 14.50)
    # return_orders()
    # return_orders_n()