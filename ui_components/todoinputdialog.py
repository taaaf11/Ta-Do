from .textinput import TextInput
from .todo import Todo
import flet as ft


class TodoInputDialog(ft.AlertDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Title would be explicitly set where this dialog would be used
        # self.title = ...
        self.text_field = TextInput(on_submit=self.close)  # user presses enter key
        self.content = self.text_field  # don't get confused. This denotes a 'container' for
                                        # ui elements of the dialog
        
        # self.actions expects an iterable
        self.actions = [ft.TextButton(icon=ft.icons.CHECK_SHARP, on_click=self.close),
                        ft.TextButton(icon=ft.icons.CANCEL_SHARP, on_click=self.cancel)]
        self.actions_alignment = ft.MainAxisAlignment.CENTER

    def get_todo(self) -> Todo:
        return Todo(self.text_field.value)
    
    def close(self, e) -> None:
        self.open = False
        self.page.update()
    
    # similar to self.close function, but empties the input
    def cancel(self, e) -> None:
        self.text_field.value = ''
        
        # I could do self.close,
        # but it requires an event in its parameters        
        self.open = False
        self.page.update()
