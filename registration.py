import time

import flet as ft

def main(page: ft.Page):
    Rosstelecom_logo = ft.Image(src='/images/r_logo.png', width=300,fit=ft.ImageFit.CONTAIN)

    Title = ft.Row([Rosstelecom_logo],alignment=ft.MainAxisAlignment.CENTER)
    t= ft.Column([Title],alignment=ft.MainAxisAlignment.CENTER)
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