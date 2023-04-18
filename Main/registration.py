import flet as ft

def main(page: ft.Page):

    Title = ft.Text('INSTALL MANAGER',size=36, color=ft.colors.PINK)
    t= ft.Column([Title],alignment=ft.MainAxisAlignment.CENTER)
    c = ft.Container(content=t,width=page.width,height=page.height, alignment=ft.alignment.center)
    def change_size(e):
        c.width = page.width
        c.height = page.height
        page.update()
    page.add(c)
    page.on_resize = change_size
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER)