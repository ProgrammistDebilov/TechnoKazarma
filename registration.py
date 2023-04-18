import time

import flet as ft

def main(page: ft.Page):
    Title = ft.Image(src='/images/r_logo.png',width=150,fit=ft.ImageFit.CONTAIN)
    role_choose = ft.Dropdown(
        width=200,
        options=[
            ft.dropdown.Option('Диспетчер'),
            ft.dropdown.Option('Инсталятор')
        ]
    )
    page.bgcolor = '#37474F'
    t= ft.Column([Title,role_choose],alignment=ft.MainAxisAlignment.CENTER)
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