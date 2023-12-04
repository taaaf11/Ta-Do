from .todoapp import TodoApp
from .button import Button
import flet as ft

class SettingsPage(ft.Column):
    def __init__(self, app_instance: TodoApp, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app_instance = app_instance
        self.controls = [
            Button(icon=ft.icons.SAVE, text='Save data', on_click=self.save_data)
        ]
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def save_data(self, e):
        self.app_instance.todos.save_to_file()
    
    def build(self):
        return self
