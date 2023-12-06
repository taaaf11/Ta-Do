from .textinput import TextInput
from .todo import Todo
from .button import Button
import flet as ft


class TodoInputDialog(ft.AlertDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = ft.Text('Create a new ToDo')
        self.text_field = TextInput(on_submit=self.close)  # user presses enter key
        self.content = self.text_field
        
        # self.actions expects an iterable
        self.actions = [Button(icon=ft.icons.CHECK_SHARP, text='Ok', on_click=self.close)]
        self.actions_alignment = ft.MainAxisAlignment.CENTER

    def get_todo(self) -> Todo:
        return Todo(self.text_field.value)
    
    def close(self, e) -> None:
        self.open = False
        self.page.update()

    def build(self):
        return self
