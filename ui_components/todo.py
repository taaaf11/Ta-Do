import flet as ft


class Todo(ft.Row):
    def __init__(self, content: str, done: bool = False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.content = content
        self.done = done
        self.checkbox = ft.Checkbox(label=self.content, value = self.done)
        self.controls = [self.checkbox]
        self.alignment = ft.CrossAxisAlignment.CENTER  # horizontal
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    def get_data(self):  # an 'interface' to get values of Todo instance
        return (self.content, self.done)

    def build(self):
        return self
