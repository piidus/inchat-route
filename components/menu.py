import flet as ft

class AppMenu:
    def __init__(self, on_route_change):
        self.on_route_change = on_route_change

    def build(self):
        return ft.Container(
            content=ft.Row(
                [
                    ft.Icon(ft.icons.PALETTE, size=18),
                    ft.Text("App Example", size=18),
                    # ft.IconButton(ft.icons.WB_SUNNY_OUTLINED, on_click=self._dummy_action),
                    # ft.IconButton(ft.icons.FILTER_3, on_click=self._dummy_action),
                    ft.PopupMenuButton(
                        items=[
                            ft.PopupMenuItem(text="Page 1", on_click=lambda _: self.on_route_change("/page1")),
                            ft.PopupMenuItem(text="Page 2", on_click=lambda _: self.on_route_change("/page2")),
                            ft.PopupMenuItem(text="Page 3", on_click=lambda _: self.on_route_change("/Conversion")),
                        ],
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            padding=ft.padding.all(5),
            bgcolor=ft.colors.SURFACE_VARIANT,
        )

    def _dummy_action(self, e):
        pass  # Placeholder for actions like theme switching, etc.
