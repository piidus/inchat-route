import flet as ft
from page1 import Page1
from page2 import Page2
from page3 import Page3

class PageControl:
    def __init__(self, page: ft.Page):
        self.page = page
        self.content_container = ft.Container(expand=True)
        
        # Dictionary mapping routes to page classes
        self.pages = {
            "/page1": Page1,
            "/page2": Page2,
            "/page3": Page3
        }

    def build(self):
        return self.content_container

    def change_page(self, route, some_value="Default value"):
        if route in self.pages:
            page_class = self.pages[route]
            content = page_class(some_value).build()
        else:
            content = ft.Text("404 - Page not found.")

        # Update the content of the container
        self.content_container.content = content
        self.page.update()

    def handle_link(self, url: str):
        route = url.split("?")[0]
        params = url.split("?")[1:]  # Extract parameters if any

        # Change page based on the extracted route
        self.change_page(route, *params)
