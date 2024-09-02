import flet as ft

class Page1:
    def __init__(self, some_value):
        self.some_value = some_value

    def build(self):
        return ft.Column([
            ft.Text(f"Welcome to Page 1! Received value: {self.some_value}"),
            ft.ElevatedButton(text="Go to Page 2", on_click=self.go_to_page2)
        ])

    def go_to_page2(self, e):
        # Handle button click to navigate to Page 2
        pass
