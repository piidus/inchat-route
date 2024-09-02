import flet as ft

class Page1:
    def __init__(self, value):
        self.value = value

    def build(self):
        return ft.Column(
            [
                ft.Text("This is Page 1"),
                ft.Text(f"Passed value: {self.value}")
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True
        )
