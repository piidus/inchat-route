import flet as ft
import platform
from models.model import first_time
class Page1:
    def __init__(self, page, **kwargs):
        self.page = page
        self.some_value = kwargs.get("some_value", "Default Value")
        self.ip_address = kwargs.get("ip_address", "No IP Address Provided")
        self.permission_handler = ft.PermissionHandler()  # Initialize PermissionHandler
        self.name_field = ft.TextField(label="Enter your name", width=300)
        self.error_message = ft.Text("", color=ft.colors.RED)  # Placeholder for error messages

    def did_mount(self):

        if platform.system() == 'Android':
            print("This is an Android device.")
            self.page.overlay.append(self.permission_handler)
            self.page.update()  # Ensure the page is updated after adding the handler

            # Check if the required permissions are granted
            storage_permission = self.permission_handler.check_permission(ft.PermissionType.STORAGE)
            
            if not storage_permission:
                # Request storage permission if not already granted
                self.permission_handler.request_permission(ft.PermissionType.STORAGE)
        
        else:
            print("This is not an Android device.")
        # Add PermissionHandler to the page's overlay
        
    def join_chat_click(self, e):
        user_name = self.name_field.value
        if not user_name:
            self.error_message.value = "Please enter your name to join the chat."
            self.page.update()
            return

        self.page.session.set("user_name", user_name)
        self.error_message.value = ""  # Clear any previous error message
        self.page.update()
        print(f"Username set to: {user_name}")

    def build(self):
        return ft.Column(
            controls=[
                ft.Text(f"Page 1 Content, some_value: {self.some_value}, IP Address: {self.ip_address}"),
                self.name_field,
                self.error_message,
                ft.ElevatedButton(text="Join chat", on_click=self.join_chat_click),
                ft.OutlinedButton(
                    "Check Microphone Permission",
                    data=ft.PermissionType.MICROPHONE,
                    on_click=self.check_microphone_permission,
                ),
                ft.OutlinedButton(
                    "Request Microphone Permission",
                    data=ft.PermissionType.MICROPHONE,
                    on_click=self.request_microphone_permission,
                ),
                ft.OutlinedButton(
                    "Open App Settings",
                    on_click=self.open_app_settings,
                ),
            ],
            expand=True
        )

    def check_microphone_permission(self, e):
        permission_status = self.permission_handler.check_permission(e.control.data)
        self.page.add(ft.Text(f"Checked {e.control.data.name}: {permission_status}"))

    def request_microphone_permission(self, e):
        permission_status = self.permission_handler.request_permission(e.control.data)
        self.page.add(ft.Text(f"Requested {e.control.data.name}: {permission_status}"))

    def open_app_settings(self, e):
        app_settings_status = self.permission_handler.open_app_settings()
        self.page.add(ft.Text(f"App Settings: {app_settings_status}"))

