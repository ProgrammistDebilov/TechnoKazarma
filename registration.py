import time

import flet as ft

def main(page: ft.Page):
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
            if role_choose not in login_content:
                login_content.insert(3,role_choose)
            enter_btn.text = 'Зарегистрироваться'
        page.update()


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
    enter_btn = ft.ElevatedButton('Зарегистроваться',bgcolor='#ff4f12', color=ft.colors.WHITE)
    is_exist_acc = ft.Checkbox(label='Я ещё не смешарик', value=False, on_change=is_exist_acc_change)

    page.bgcolor = '#37474F'
    login_content = [Title,login,password,role_choose,enter_btn,is_exist_acc]
    t= ft.Column(login_content,alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    c = ft.Container(content=t,width=page.width,height=page.height, alignment=ft.alignment.center)
    def change_size(e):
        c.width = page.width
        c.height = page.height
        page.update()
    page.add(c)
    page.on_resize = change_size
    page.update()
    time.sleep(1)

ft.app(target=main, view=ft.WEB_BROWSER, assets_dir='assets')