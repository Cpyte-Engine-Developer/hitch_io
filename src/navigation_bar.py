import flet as ft


class NavigationBar(ft.NavigationBar):
    def __init__(self, destinations: tuple[ft.NavigationBarDestination]):
        super().__init__()
        self.destinations = destinations