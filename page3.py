import flet as ft

class Page3:
    def __init__(self, some_value):
        self.some_value = some_value

    def build(self):
        return ft.Column([
            ft.Text(f"Welcome to Page 3! Received value: {self.some_value}"),
            ft.ElevatedButton(text="Go to Page 1", on_click=self.go_to_page1)
        ])

    def go_to_page1(self, e):
        # Handle button click to navigate back to Page 1
        pass
