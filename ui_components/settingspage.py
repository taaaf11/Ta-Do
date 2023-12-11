from .fn import get_data_storage_path
import flet as ft
import os


class SettingsPage(ft.Column):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.theme_mode_button = ft.TextButton(icon=ft.icons.LIGHT_MODE_SHARP, text='Light mode', on_click=self.switch_theme_mode)
        self.delete_data_button = ft.TextButton(icon=ft.icons.DELETE_FOREVER_SHARP, text='Delete app data', on_click=self.delete_app_data)
        self.controls = [
            self.theme_mode_button,
            self.delete_data_button
        ]
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def switch_theme_mode(self, e) -> None:
        if self.page.theme_mode == ft.ThemeMode.DARK:
            self.page.theme_mode = ft.ThemeMode.LIGHT
            
            # change button accordingly
            self.theme_mode_button.icon = ft.icons.DARK_MODE_SHARP
            self.theme_mode_button.text = 'Dark mode'
            self.page.update()
        else:
            self.page.theme_mode = ft.ThemeMode.DARK
            
            # change button accordingly
            self.theme_mode_button.icon = ft.icons.LIGHT_MODE_SHARP
            self.theme_mode_button.text = 'Light mode'
            self.page.update()
    
    def delete_app_data(self, e) -> None:
        #  app data rests in 'Ta-Do_data/todo_data.txt' file.
        app_data_dir = get_data_storage_path()
        try:  
            os.remove(f'{app_data_dir}/todo_data.txt')
            os.rmdir(f'{app_data_dir}')
        except:
            return
    
    def build(self):
        return self
