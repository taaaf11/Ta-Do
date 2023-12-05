import flet as ft


class Todo(ft.Row):
    def __init__(self, content: str, done: bool = False, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.content = content
        self.done = done
        self.checkbox = ft.Checkbox(label=self.content, value=self.done, on_change=self.on_checkbox_change)
        self.controls = [self.checkbox]
        self.alignment = ft.MainAxisAlignment.START  # horizontal
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
    
    def on_checkbox_change(self, e) -> None:
        self.done = self.checkbox.value
    
    def get_data(self) -> tuple:  # an 'interface' to get values of Todo instance
        return self.checkbox.label, self.checkbox.value
        
    def build(self):
        return self
