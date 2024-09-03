import flet as ft
from pages.login.page1 import Page1
from pages.chat.page2 import Page2
from pages.chat.conversion import Conversion
from components.menu import AppMenu

class PageControl:
    def __init__(self, page, some_value):
        self.page = page
        self.some_value = some_value
        self.content_container = ft.Container(expand=True)
        self.app_menu = AppMenu(self.change_page).build()

        # Dictionary mapping routes to page classes
        self.pages = {
            "/page1": Page1,
            "/page2": Page2,
            "/Conversion": Conversion,
        }

    def build(self):
        return ft.Column(
            controls=[
                self.app_menu,
                self.content_container
            ],
            expand=True
        )

    def change_page(self, route, **kwargs):
        # Dynamically instantiate the page based on the route
        if route in self.pages:
            page_class = self.pages[route]
            # Pass the required 'page' argument along with additional kwargs
            content = page_class(self.page, **kwargs).build()
            self.content_container.content = content
            self.page.update()
        else:
            # Handle unknown routes
            self.content_container.content = ft.Text(f"404 - Page '{route}' not found.")
            self.page.update()
