import time

import flet as ft
import Backend.work_db as fdb
def main(page: ft.Page):
    def close_banner(e):
        page.banner.open = False
        page.update()

    def send_banner(message):
        page.banner = ft.Banner(
            bgcolor='#C62828',
            leading=ft.Image(src='favicon.png', fit=ft.ImageFit.CONTAIN, width=100),
            content=ft.Text(message, color=ft.colors.WHITE, size=25),
            actions=[
                ft.ElevatedButton('Закрыть', on_click=close_banner, color='#7C4DFF')
            ]
        )
        page.banner.open = True
        page.update()

    def is_exist_acc_change(e):
        if is_exist_acc.value:
            is_exist_acc.label = 'Я уже смешарик'
            enter_btn.text = 'Войти'
            try:
                login_content.remove(role_choose)
            except:
                pass
        else:
            is_exist_acc.label = 'Я ещё не смешарик'
            enter_btn.text = 'Зарегистрироваться'
            if role_choose not in login_content:
                login_content.insert(3,role_choose)

        page.update()

    def enter_btn_action(e):
        if is_exist_acc.value: #логин
            brak = False #ошибки при заполнение


            ###проверки на зполнение
            if login.value == '':
                login.error_text = 'Вы забыли заполнить'
                login.update()
                brak = True
            else:
                login.error_text = None
                login.update()
            if password.value == '':
                password.error_text = 'У вас обязан быть пароль'
                password.update()
                brak = True
            else:
                password.error_text = None
                password.update()



            if not brak:
                ok = fdb.sign_in((login.value,password.value))
                if not ok:
                    send_banner('Неверный логин/пароль')
                if ok:
                    close_banner('')
                    page.go('/soft')

        else:#регистрация
            brak = False

            ###проверки на заполнение
            if login.value == '':
                login.error_text = 'Вы забыли заполнить'
                login.update()
                brak = True
            else:
                login.error_text = None
                login.update()
            if password.value == '':
                password.error_text = 'У вас обязан быть пароль'
                password.update()
                brak = True
            else:
                password.error_text = None
                password.update()
            if role_choose.value == None:
                role_choose.error_text = 'Роль обязательна'
                role_choose.update()
                brak = True
            else:
                role_choose.error_text = None
                role_choose.update()


            if not brak:
                ok = fdb.sign_up((login.value,password.value,role_choose.value))
                password.value = ''
                login.value = ''
                role_choose.value = None
                if not ok:
                    send_banner('Логин уже занят')
                if ok:
                    close_banner('')
                    page.go('/soft')


    Title = ft.Image(src='/images/r_logo.png',width=150,fit=ft.ImageFit.CONTAIN)
    login = ft.TextField(label='Логин', hint_text='Введите ваш логин',width=300,focused_border_color='#7C4DFF')
    password = ft.TextField(label='Пароль', hint_text='Введите ваш пароль',width=300,focused_border_color='#7C4DFF')
    role_choose = ft.Dropdown(
        label='Роль',
        width=155,
        options=[
            ft.dropdown.Option('Диспетчер'),
            ft.dropdown.Option('Инсталятор')
        ],
        focused_border_color='#7C4DFF'
    )
    enter_btn = ft.ElevatedButton('Зарегистроваться',bgcolor='#ff4f12', color=ft.colors.WHITE, on_click=enter_btn_action)
    is_exist_acc = ft.Checkbox(label='Я ещё не смешарик', value=False, on_change=is_exist_acc_change)

    page.bgcolor = '#37474F'

    login_content = [Title,login,password,role_choose,enter_btn,is_exist_acc]



    t= ft.Column(login_content,alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    login_screen_content = ft.Container(content=t,width=page.width,height=page.height, alignment=ft.alignment.center)

    #адаптивные размеры окон
    def change_size(e):
        login_screen_content.width = page.width
        login_screen_content.height = page.height
        page.update()


    def route_change(route):
        page.views.clear()
        if page.route == '/' or page.route == '/login':
            page.title = 'Ros Login'
            page.views.append(
                ft.View(
                    '/login',
                    [
                        login_screen_content
                    ]
                )

            )
        if page.route == '/soft':
            page.title = 'Это победа, братья'
            page.views.append(
                ft.View(
                    '/soft',
                    [
                        ft.ElevatedButton('Exit',on_click=lambda _:page.go('/login'))
                    ]
                )
            )
        page.update()
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    page.theme_mode = 'DARK'
    page.on_resize = change_size
    page.update()



ft.app(target=main, view=ft.WEB_BROWSER, assets_dir='../assets', port=42069)