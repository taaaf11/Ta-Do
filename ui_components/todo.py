import flet as ft


class Todo(ft.Container):
    def __init__(self, content, done: bool = False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.content = content
        self.done = done
        self.checkbox = ft.Checkbox(label=content, value = done)
        self.content = ft.Row([
            self.checkbox
        ])

    def build(self):
        return self
