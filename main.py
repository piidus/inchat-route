import flet as ft
from menu import AppMenu
from page_control import PageControl

def main(page: ft.Page):
    page.title = "Flet Multi-Page App"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.colors.WHITE

    # Initialize PageControl and AppMenu
    page_control = PageControl(page)
    menu = AppMenu(page_control.change_page)

    # Build UI with a NavigationRail and a content container
    layout = ft.Row([
        menu.build(),
        page_control.build()
    ], expand=True)
    
    page.add(layout)
    page_control.change_page("/page1")  # Load the default page

ft.app(target=main)
