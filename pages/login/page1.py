import flet as ft

class Page1:
    def __init__(self, page, **kwargs):
        self.page = page
        self.some_value = kwargs.get("some_value", "Default Value")
        self.ip_address = kwargs.get("ip_address", "No IP Address Provided")
        self.dialog = None

    def did_mount(self):
        self.dialog = ft.AlertDialog(
            open=True,
            modal=True,
            title=ft.Text("Welcome!"),
            content=ft.TextField(label="Enter your name", autofocus=True, width=300),
            actions=[
                ft.ElevatedButton(text="Join chat", on_click=self.join_chat_click)
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        self.page.overlay.append(self.dialog)
        self.page.update()

    def join_chat_click(self, e):
        user_name = self.dialog.content.value
        self.page.session.set("user_name", user_name)
        self.dialog.open = False
        self.page.update()
        print(f"Username set to: {user_name}")

    def build(self):
        return ft.Column(
            controls=[
                ft.Text(f"Page 1 Content, some_value: {self.some_value}, IP Address: {self.ip_address}")
            ],
            expand=True
        )
