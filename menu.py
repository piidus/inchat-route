import flet as ft

class AppMenu:
    def __init__(self, on_route_change):
        self.on_route_change = on_route_change

    def build(self):
        return ft.NavigationRail(
            selected_index=0,
            destinations=[
                ft.NavigationRailDestination(icon=ft.icons.HOME, label="Page 1"),
                ft.NavigationRailDestination(icon=ft.icons.LOOKS_TWO, label="Page 2"),
                ft.NavigationRailDestination(icon=ft.icons.LOOKS_3, label="Page 3")
            ],
            on_change=self.on_nav_change,
            expand=True
        )

    def on_nav_change(self, e):
        routes = ["/page1", "/page2", "/page3"]
        self.on_route_change(routes[e.control.selected_index])
