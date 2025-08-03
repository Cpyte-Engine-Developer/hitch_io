import flet as ft


class NavigationBarDestination(ft.NavigationBarDestination):
    def __init__(self, icon: ft.Icons, label: str):
        super().__init__()
        self.icon = icon
        self.label = label