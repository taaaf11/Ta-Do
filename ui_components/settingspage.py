from .todoapp import TodoApp
from .button import Button
import flet as ft

class SettingsPage(ft.Column):
    def __init__(self, app_instance: TodoApp, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app_instance = app_instance
        self.current_theme_mode = 'dark'
        self.theme_mode_button = Button(icon=ft.icons.LIGHT_MODE_SHARP, text='Light mode', on_click=self.switch_theme_mode)
        self.controls = [
            self.theme_mode_button
        ]
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def switch_theme_mode(self, e):
        if self.page.theme_mode == 'dark':
            self.page.theme_mode = 'light'
            
            # change button accordingly
            self.theme_mode_button.icon = ft.icons.DARK_MODE_SHARP
            self.theme_mode_button.text = 'Dark mode'
            self.page.update()
        else:
            self.page.theme_mode = 'dark'
            
            # change button accordingly
            self.theme_mode_button.icon = ft.icons.LIGHT_MODE_SHARP
            self.theme_mode_button.text = 'Light mode'
            self.page.update()
    
    def build(self):
        return self
