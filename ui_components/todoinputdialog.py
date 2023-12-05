from .textinput import TextInput
from .todo import Todo
import flet as ft


class TodoInputDialog(ft.AlertDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = ft.Text('Create a new ToDo')
        self.text_field = TextInput()
        self.content = self.text_field

    def get_todo(self) -> Todo:
        return Todo(self.text_field.value)

    def build(self):
        return self
