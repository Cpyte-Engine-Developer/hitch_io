import flet as ft


class UpdatesContainer(ft.Container):
    def __init__(self):
        super().__init__()
        self.content = ft.Text("Updates")
        self.alignment = ft.alignment.center