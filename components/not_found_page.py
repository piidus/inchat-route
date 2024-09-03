import flet as ft

class NotFoundPage:
    def build(self):
        return ft.Column([
            ft.Text("404 - Page not found."),
            ft.Button(text="Go to Home", on_click=self.go_home)
        ])

    def go_home(self, e):
        # Handle navigation to the home page
        pass
