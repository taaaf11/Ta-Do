import flet as ft


class TextInput(ft.TextField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.border_radius = 20
        self.hint_text = 'I am gonna do...'
    
    def build(self):
        return self
