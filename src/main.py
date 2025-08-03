import flet as ft
from navigation_bar import NavigationBar
from games_container import GamesContainer


def main(page: ft.Page):
    page.title = "Hitch.io"

    games_container = GamesContainer()
    library_container = ft.Container(
        ft.Text("Library"),
        alignment=ft.alignment.center,
    )
    updates_container = ft.Container(
        ft.Text("Updates"),
        alignment=ft.alignment.center,
    )
    settings_container = ft.Container(
        ft.Text("Settings"),
        alignment=ft.alignment.center,
    )

    animated_switcher = ft.AnimatedSwitcher(
        games_container,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=100,
        switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN
    )
    page.navigation_bar = NavigationBar(
        (games_container, library_container, updates_container, settings_container),
        animated_switcher
    )

    page.add(animated_switcher)
    page.update()


ft.app(main)
