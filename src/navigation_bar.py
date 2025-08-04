from typing import Sequence
import flet as ft


class NavigationBar(ft.NavigationBar):
    def __init__(self, containers: Sequence[ft.Container], animated_switcher: ft.AnimatedSwitcher):
        super().__init__()
        self.destinations = (
            ft.NavigationBarDestination(icon=ft.Icons.WEB, label="Games"),
            ft.NavigationBarDestination(icon=ft.Icons.LIBRARY_BOOKS, label="Library"),
            ft.NavigationBarDestination(icon=ft.Icons.DOORBELL, label="Updates"),
            ft.NavigationBarDestination(icon=ft.Icons.SETTINGS, label="Settings")
        )
        self.on_change = self.on_navigation_bar_destination_select
        self.containers = containers
        self.animated_switcher = animated_switcher

    def on_navigation_bar_destination_select(self, event: ft.ControlEvent):
       self.animated_switcher.content = self.containers[self.selected_index]
       self.animated_switcher.update()
