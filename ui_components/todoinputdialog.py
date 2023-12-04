import flet as ft
from .textinput import TextInput
from .button import Button
from .todo import Todo


class TodoInputDialog(ft.AlertDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = ft.Text('Create a new ToDo')
        self.text_field = TextInput()
        self.content = self.text_field
        self.actions = [ft.Row([
            Button(icon=ft.icons.CHECK_SHARP, text='Ok')
        ], alignment=ft.MainAxisAlignment.CENTER)]

    def get_text(self):
        return Todo(self.text_field.value)

    def build(self):
        return self
