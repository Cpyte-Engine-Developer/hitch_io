import flet as ft
from navigation_bar import NavigationBar


def main(page: ft.Page):
    page.title = "Hitch.io"
    page.navigation_bar = NavigationBar()
    page.update()


ft.app(main)
