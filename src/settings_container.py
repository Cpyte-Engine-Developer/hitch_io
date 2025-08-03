import flet as ft


class SettingsContainer(ft.Container):
    def __init__(self):
        super().__init__()
        self.content = ft.Text("Settings")
        self.alignment = ft.alignment.center