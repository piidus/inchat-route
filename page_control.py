import flet as ft
from page1 import Page1
from page2 import Page2
from page3 import Page3

class PageControl:
    def __init__(self, page):
        self.page = page
        self.content_container = ft.Container(expand=True)

    def build(self):
        return self.content_container

    def change_page(self, route):
        if route == "/page1":
            content = Page1("Value for Page 1").build()
        elif route == "/page2":
            content = Page2("Value for Page 2").build()
        elif route == "/page3":
            content = Page3("Value for Page 3").build()
        self.content_container.content = content
        self.page.update()
