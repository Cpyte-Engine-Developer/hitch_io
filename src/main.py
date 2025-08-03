import flet as ft
from navigation_bar import NavigationBar


def main(page: ft.Page):
    page.title = "Hitch.io"
    page.navigation_bar = NavigationBar(
        destinations=(
            ft.NavigationBarDestination(icon=ft.Icons.WEB, label="Games"),
            ft.NavigationBarDestination(icon=ft.Icons.LIBRARY_BOOKS, label="Library"),
            ft.NavigationBarDestination(icon=ft.Icons.DOORBELL, label="Updates"),
            ft.NavigationBarDestination(icon=ft.Icons.SETTINGS, label="Settings")
        )
    )
    page.update()


ft.app(main)
