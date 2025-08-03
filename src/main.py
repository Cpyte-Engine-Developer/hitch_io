import flet as ft


def main(page: ft.Page):
    page.title = "Hitch.io"
    page.navigation_bar = ft.NavigationBar(
        destinations=(
            ft.NavigationBarDestination(icon=ft.Icons.WEB, label="Games"),
            ft.NavigationBarDestination(icon=ft.Icons.LIBRARY_BOOKS, label="Library"),
            ft.NavigationBarDestination(icon=ft.Icons.DOORBELL, label="Updates"),
            ft.NavigationBarDestination(icon=ft.Icons.SETTINGS, label="Settings")
        )
    )
    page.add(ft.Text("Body!"))


ft.app(main)
