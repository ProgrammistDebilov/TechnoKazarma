import flet as ft
import webbrowser
import os
import Backend.work_db as fdb
import Backend.location as gps
def main(page: ft.Page):
    def keyboard_shortcuts(e:ft.KeyboardEvent):
        if page.route == '/login':
            match e.key:
                case 'Enter':
                    enter_btn_action('')
                case '\\':
                    is_exist_acc.value = not is_exist_acc.value
                    is_exist_acc_change('')
                    is_exist_acc.update()
                case 'Delete':
                    login.value = ''
                    password.value = ''
                    role_choose.value = None
                    is_exist_acc.value = False
                    is_exist_acc_change('')
                    page.update()
        if page.route == '/soft':
            match e.key:
                case 'Escape' if add_order_dialog.open == True:
                    close_alert_new_order_dlg('')
                case 'Enter' if add_order_dialog.open == True:
                    close_alert_new_order_dlg('')



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
                enter_btn.disabled = True
                ok = fdb.sign_in((login.value,password.value))
                if not ok:
                    enter_btn.disabled = False
                    send_banner('Неверный логин/пароль')
                if ok:
                    page.client_storage.clear()
                    page.client_storage.set('loged', True)
                    page.client_storage.set('login', login.value)

                    page.client_storage.set('role', fdb.return_role(login.value))
                    login.value = ''
                    password.value = ''
                    try:
                        close_banner('')
                    except AttributeError:
                        pass
                    if page.client_storage.get('role') == 'Инсталятор':
                        try:
                            soft_main_list_content.remove(add_new_order_btn)
                        except:
                            pass
                        if accept_order_btn not in soft_main_list_content:
                            soft_main_list_content.append(accept_order_btn)
                    elif page.client_storage.get('role') == 'Диспетчер':
                        try:
                            soft_main_list_content.remove(accept_order_btn)
                        except:
                            pass
                        if add_new_order_btn not in soft_main_list_content:
                            soft_main_list_content.append(add_new_order_btn)
                    installers_info.clear()
                    for i in fdb.return_installers():
                        icon = ft.Icon(ft.icons.PERSON_4_OUTLINED)
                        if i.get('alacrity') == 1:
                            icon.color = ft.colors.GREEN
                        else:
                            icon.color = ft.colors.RED
                        installers_info.append(
                            ft.ListTile(
                                leading=icon,
                                title=ft.Text(i.get('login'))
                            )
                        )
                    page.update()
                    page.go('/soft')
                    enter_btn.disabled = False

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
                ok = 0
                enter_btn.disabled = True
                if role_choose.value != 'Инсталятор':
                    ok = fdb.sign_up((login.value, password.value, role_choose.value))
                elif role_choose.value == 'Инсталятор':
                    size = gps.get_loc()
                    print(size)
                    ok = fdb.sign_up((login.value, password.value, role_choose.value,size[1],size[0] ))
                if not ok:
                    send_banner('Логин уже занят')
                    enter_btn.disabled = False
                if ok:
                    page.client_storage.clear()
                    page.client_storage.set('loged', True)
                    page.client_storage.set('login', login.value)
                    page.client_storage.set('role', role_choose.value)

                    password.value = ''
                    login.value = ''
                    role_choose.value = None
                    try:
                        close_banner('')
                    except AttributeError:
                        pass
                    if page.client_storage.get('role') == 'Инсталятор':
                        try:
                            soft_main_list_content.remove(add_new_order_btn)
                        except:
                            pass
                        if accept_order_btn not in soft_main_list_content:
                            soft_main_list_content.append(accept_order_btn)
                    elif page.client_storage.get('role') == 'Диспетчер':
                        try:
                            soft_main_list_content.remove(accept_order_btn)
                        except:
                            pass
                        if add_new_order_btn not in soft_main_list_content:
                            soft_main_list_content.append(add_new_order_btn)


                    installers_info.clear()
                    for i in fdb.return_installers():
                        icon = ft.Icon(ft.icons.PERSON_4_OUTLINED)
                        if i.get('alacrity') == 1:
                            icon.color = ft.colors.GREEN
                        else:
                            icon.color = ft.colors.RED
                        installers_info.append(
                            ft.ListTile(
                                leading=icon,
                                title=ft.Text(i.get('login'))
                            )
                        )
                    page.go('/soft')
                    enter_btn.disabled = False


    #Title = ft.Image(src='images/r1.png',width=page.width//20,fit=ft.ImageFit.CONTAIN)
    #Title = ft.Text('РОСТЕЛЕКОМ', size=page.width//20, color='#7C4DFF')
    Title = ft.Icon(ft.icons.WIFI, color='#7C4DFF', size=page.width//5)
    login = ft.TextField(label='Логин', hint_text='Введите ваш логин',width=300,focused_border_color='#7C4DFF')
    password = ft.TextField(label='Пароль', hint_text='Введите ваш пароль',width=300,focused_border_color='#7C4DFF', password=True, can_reveal_password=True)
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






    ######Main content
    def exit_btn(e):
        page.client_storage.clear()
        page.go('/login')

    def close_alert_new_order_dlg(e):
        add_order_dialog.open = False
        page.update()
    def open_alert_new_order_dlg(e):
        page.dialog = add_order_dialog
        add_order_dialog.open = True
        page.update()

    def close_alert_accept_order_dlg(e):
        accept_order_dialog.open = False
        page.update()

    def open_alert_accept_order_dlg(e):
        reqs = fdb.return_orders_n()
        reqs_accept_order_options.clear()
        for i in reqs:
            reqs_accept_order_options.append(ft.dropdown.Option(i.get('adress')))

        page.dialog = accept_order_dialog
        accept_order_dialog.open = True
        page.update()

    def add_order_func(e):
        if adress_field_add_order.value != '':
            adress_field_add_order.error_text = None
            fdb.add_order(adress_field_add_order.value)
            adress_field_add_order.value = ''
            close_alert_new_order_dlg('')
        else:
            adress_field_add_order.error_text = 'Напишите для начала адрес заявки'
        page.update()

    adress_field_add_order = ft.TextField(width=250,label='Адрес заявки', hint_text='Напишите город и адрес')
    reqs_accept_order_options = []
    reqs_accept_order = ft.Dropdown(options=reqs_accept_order_options,label='Заявки', hint_text='Выберите заявку')
    installers_info = []
    installs = ft.Column(installers_info)

    add_order_dialog = ft.AlertDialog(
        modal=True,
        title = ft.Text('Фиксирование заявки'),
        content=adress_field_add_order,
        actions=[ft.TextButton('Зафиксировать', on_click=add_order_func), ft.TextButton('Отмена', on_click=close_alert_new_order_dlg)]
    )

    accept_order_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text('Принятие заявки'),
        content=ft.Container(content=reqs_accept_order, width=page.width),
        actions=[ft.TextButton('Принять', on_click=close_alert_accept_order_dlg),
                 ft.TextButton('Отмена', on_click=close_alert_accept_order_dlg)]
    )

    #Нижняя панель
    exit = ft.IconButton(icon=ft.icons.EXIT_TO_APP,on_click=exit_btn, icon_color='#6200EA',icon_size=20)
    installers_page = ft.IconButton(icon=ft.icons.BUILD_OUTLINED,on_click=lambda _:page.go('/installers'), icon_color='#6200EA',icon_size=20)
    home_page = ft.IconButton(icon=ft.icons.HOME_OUTLINED,on_click=lambda _:page.go('/soft'), icon_color='#6200EA',icon_size=20)
    down_bar_content = ft.Row([installers_page,home_page,exit],  alignment=ft.MainAxisAlignment.CENTER)
    down_bar = ft.Container(content=down_bar_content,width=page.width,height=60, bgcolor='#B388FF', alignment=ft.alignment.top_center)



    show_map_btn = ft.ElevatedButton(content=ft.Container(ft.Column([ft.Text('Открыть карту', size=30)], alignment=ft.MainAxisAlignment.CENTER),alignment=ft.alignment.center), width=300,height=80, bgcolor='#ff4f12', color=ft.colors.WHITE,on_click=lambda _ : page.launch_url("100.65.5.56:8050"))
    add_new_order_btn = ft.ElevatedButton('Зафиксировать заявку', width=200, height=40, bgcolor='#607D8B', color=ft.colors.WHITE, on_click=open_alert_new_order_dlg)
    accept_order_btn = ft.ElevatedButton('Принять заявку', width=200, height=40, bgcolor='#607D8B', color=ft.colors.WHITE, on_click=open_alert_accept_order_dlg)

    soft_main_list_content = [show_map_btn,add_new_order_btn,accept_order_btn]


    soft_main_content = ft.Column(soft_main_list_content, alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    soft_main_window = ft.Container(content=soft_main_content,width=page.width, height=page.height - down_bar.height, alignment=ft.alignment.center)



    soft_colummn_main = ft.Column([soft_main_window,down_bar])
    soft_screen_content = ft.Container(content=soft_colummn_main, width=page.width,height=page.height)

    installers_screen_row_main = ft.Row([ft.Card(content=installs,width=400)], alignment=ft.MainAxisAlignment.CENTER)

    installers_screen_content = ft.Container(content=ft.Column([installers_screen_row_main], scroll='adaptive'), width=page.width,height=page.height-down_bar.height)

    #адаптивные размеры окон
    def change_size(e):
        login_screen_content.width = page.width
        Title.size = page.width//5
        login_screen_content.height = page.height
        down_bar.width = page.width
        soft_main_content.width = page.width
        soft_main_window.height = page.height - down_bar.height
        soft_main_window.width = page.width
        soft_screen_content.height = page.height
        installers_screen_content.height = page.height - down_bar.height
        installers_screen_content.width = page.width
        page.update()



    def route_change(route):
        page.views.clear()
        if page.route == '/' or page.route == '/login':
            page.title = 'Ros Login'
            page.views.append(
                ft.View(
                    '/login',
                    [
                        ft.ListView(controls=[login_screen_content],expand=False,spacing=0)
                    ],
                    scroll='Auto'
                )

            )
        if page.route == '/soft':
            page.title = 'Это победа, братья'
            page.views.append(
                ft.View(
                    '/soft',
                    [
                        soft_screen_content

                    ]
                )
            )
        if page.route == '/installers':
            page.title = 'Работяги'
            page.views.append(
                ft.View(
                    '/installers',
                    [
                        installers_screen_content,
                        down_bar
                    ],
                )
            )
        page.update()
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    if page.client_storage.get('loged'):
        if page.client_storage.get('role') == 'Инсталятор':
            try:
                soft_main_list_content.remove(add_new_order_btn)
            except:
                pass
            if accept_order_btn not in soft_main_list_content:
                soft_main_list_content.append(accept_order_btn)
        elif page.client_storage.get('role') == 'Диспетчер':
            try:
                soft_main_list_content.remove(accept_order_btn)
            except:
                pass
            if add_new_order_btn not in soft_main_list_content:
                soft_main_list_content.append(add_new_order_btn)
        installers_info.clear()
        for i in fdb.return_installers():
            icon = ft.Icon(ft.icons.PERSON_4_OUTLINED)
            if i.get('alacrity') == 1:
                icon.color = ft.colors.GREEN
            else:
                icon.color = ft.colors.RED

            installers_info.append(
                ft.ListTile(
                    leading=icon,
                    title=ft.Text(i.get('login'))
                )
            )
        page.update()
        page.go('/soft')
    else:
        page.go('/login')
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.on_keyboard_event = keyboard_shortcuts
    page.go(page.route)
    page.theme_mode = 'DARK'
    page.on_resize = change_size

    page.update()



ft.app(target=main, view=ft.WEB_BROWSER, assets_dir='../assets', port=42069)