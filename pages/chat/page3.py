import flet as ft

class Page3:
    def __init__(self, page, **kwargs):
        self.page = page
        self.some_value = kwargs.get("some_value", "Default Value")

    def build(self):
        return ft.Column(
            controls=[
                ft.Text(f"Page 3 Content, some_value: {self.some_value}")
            ],
            expand=True
        )
