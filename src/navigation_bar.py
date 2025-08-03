import flet as ft
from navigation_bar_destination import NavigationBarDestination


class NavigationBar(ft.NavigationBar):
    def __init__(self):
        super().__init__()
        self.destinations = (
            NavigationBarDestination(icon=ft.Icons.WEB, label="Games"),
            NavigationBarDestination(icon=ft.Icons.LIBRARY_BOOKS, label="Library"),
            NavigationBarDestination(icon=ft.Icons.DOORBELL, label="Updates"),
            NavigationBarDestination(icon=ft.Icons.SETTINGS, label="Settings")
        )