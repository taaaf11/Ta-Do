import flet as ft


class Button(ft.TextButton):
    def __init__(self, icon, text,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.icon = icon
        self.text = text

    def build(self):
        return self
