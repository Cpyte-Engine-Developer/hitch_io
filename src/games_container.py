import flet as ft


class GamesContainer(ft.Container):
    def __init__(self):
        super().__init__()
        self.alignment = ft.alignment.center
        self.content = ft.Text("Games")