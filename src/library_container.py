import flet as ft


class LibraryContainer(ft.Container):
    def __init__(self):
        super().__init__()
        self.content = ft.Text("Library")
        self.alignment = ft.alignment.center
