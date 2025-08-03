import flet as ft
from navigation_bar import NavigationBar
from games_container import GamesContainer
from library_container import LibraryContainer
from updates_container import UpdatesContainer
from settings_container import SettingsContainer


def main(page: ft.Page):
    page.title = "Hitch.io"

    games_container = GamesContainer()
    library_container = LibraryContainer()
    updates_container = UpdatesContainer()
    settings_container = SettingsContainer()

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
