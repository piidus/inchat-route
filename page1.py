import flet as ft

class Page1:
    def __init__(self, page, **kwargs):
        self.page = page
        self.some_value = kwargs.get("some_value", "Default Value")
        self.ip_address = kwargs.get("ip_address", "No IP Address Provided")

    def build(self):
        return ft.Column(
            controls=[
                ft.Text(f"Page 1 Content, some_value: {self.some_value}, IP Address: {self.ip_address}")
            ],
            expand=True
        )
