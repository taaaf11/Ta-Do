from .button import Button
import flet as ft


class SettingsPage(ft.Column):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.theme_mode_button = Button(icon=ft.icons.LIGHT_MODE_SHARP, text='Light mode', on_click=self.switch_theme_mode)
        self.controls = [
            self.theme_mode_button
        ]
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def switch_theme_mode(self, e) -> None:
        if self.page.theme_mode == ft.ThemeMode.DARK:
            self.page.theme_mode = ft.ThemeMode.LIGHT
            
            # change button accordingly
            self.theme_mode_button.icon = ft.Icon(ft.icons.DARK_MODE_SHARP)
            self.theme_mode_button.text = 'Dark mode'
            self.page.update()
        else:
            self.page.theme_mode = ft.ThemeMode.DARK
            
            # change button accordingly
            self.theme_mode_button.icon = ft.Icon(ft.icons.LIGHT_MODE_SHARP)
            self.theme_mode_button.text = 'Light mode'
            self.page.update()
    
    def build(self):
        return self
