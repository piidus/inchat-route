import flet as ft

class Page3:
    def __init__(self, value):
        self.value = value

    def build(self):
        return ft.Column(
            [
                ft.Text("This is Page 3"),
                ft.Text(f"Passed value: {self.value}")
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True
        )
