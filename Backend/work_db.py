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
        role = 'a'

    cur.execute(
        f'INSERT INTO users (name, surname, login, password, role) VALUES({name}, {surname}, {login}, {password}, {role});')
