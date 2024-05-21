import flet as ft
from flet import *

def main(page:Page):
    page.title = "Тренировка интуиции"
    page.window_width = 350.00
    page.window_height = 600.00
    page.window_resizable = False
    page.update()

    # Получаем индекс вкладки
    def chagetab(e):
        my_index = e.control.selected_index
        tab_1.visible = True if my_index == 0 else False
        tab_2.visible = True if my_index == 1 else False
        tab_3.visible = True if my_index == 2 else False
        page.update()


    page.navigation_bar = CupertinoNavigationBar(
        bgcolor=colors.LIGHT_BLUE_700,
        inactive_color=colors.GREY,
        active_color=colors.WHITE,
        selected_index=0,
        on_change=chagetab,
        destinations=[
            NavigationDestination(icon=icons.EXPLORE, label="Правила игры", ),
            NavigationDestination(icon=icons.GAMES, label="Game"),
            NavigationDestination(icon=icons.TABLE_VIEW, label="Статистика"),
        ]
    )

    #tab_1 = Text('Инструкция', size=30, visible=True, color='blue')
    tab_1 = Container(content=Column([
            Text('Инструкция', size=30, color='blue', text_align=TextAlign.CENTER),
            Text('1. Нужно угадать каким цветом окрасится квадрат;'),
            Text('2. Подумай какой цвет может сейчас появится и нажми на кнопку этого цвета.')
        ]))

    tab_2 = Text('Tab 2', size=30, visible=False)
    tab_3 = Text('Tab 3', size=30, visible=False)

    page.add((
        Container(
            content=Column([
                tab_1,
                tab_2,
                tab_3]))))


ft.app(target=main)
