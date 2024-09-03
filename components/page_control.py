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

        # Track the current page instance
        self.current_page = None

    def build(self):
        return ft.Column(
            controls=[
                self.app_menu,
                self.content_container
            ],
            expand=True
        )

    def change_page(self, route, **kwargs):
        # Call will_unmount on the current page if it exists
        if self.current_page and hasattr(self.current_page, 'will_unmount'):
            self.current_page.will_unmount()

        # Dynamically instantiate the page based on the route
        if route in self.pages:
            page_class = self.pages[route]
            # Pass the required 'page' argument along with additional kwargs
            self.current_page = page_class(self.page, **kwargs)
            
            # Set content and call did_mount if it exists
            self.content_container.content = self.current_page.build()
            self.page.update()
            
            if hasattr(self.current_page, 'did_mount'):
                self.current_page.did_mount()
        else:
            # Handle unknown routes
            self.content_container.content = ft.Text(f"404 - Page '{route}' not found.")
            self.page.update()
