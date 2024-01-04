from .fn import get_data_storage_path, get_saved_theme_mode
from .themecolourdropdown import ThemeColourDropdown
import flet as ft
import os, glob


class SettingsPage(ft.Column):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.theme_mode_button = ft.TextButton(on_click=self.switch_theme_mode)
        if get_saved_theme_mode().value == 'dark':
            self.theme_mode_button.icon = ft.icons.LIGHT_MODE_SHARP
            self.theme_mode_button.text = 'Light mode'
        else:
            self.theme_mode_button.icon = ft.icons.DARK_MODE_SHARP
            self.theme_mode_button.text = 'Dark mode'
        self.delete_data_button = ft.TextButton(icon=ft.icons.DELETE_FOREVER_SHARP, text='Delete app data', on_click=self.delete_app_data)
        self.theme_color_dropdown = ThemeColourDropdown([
            'Red',
            'Pink',
            'Purple',
            'Indigo',
            'Blue',
            'Green',
            'Default'
        ])
        
        self.theme_dropdown_controls = ft.Column([
            ft.Row([
                ft.Text('Theme Colour: '),
                self.theme_color_dropdown
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=30),
            ft.Text('*Changes take effect once you\nrestart the app.', text_align=ft.TextAlign.CENTER)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        
        self.controls = [
            self.theme_mode_button,
            self.delete_data_button,
            self.theme_dropdown_controls
        ]
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def switch_theme_mode(self, e) -> None:
        if self.page.theme_mode == ft.ThemeMode.DARK:
            self.page.theme_mode = ft.ThemeMode.LIGHT
            
            # change button accordingly
            self.theme_mode_button.icon = ft.icons.DARK_MODE_SHARP
            self.theme_mode_button.text = 'Dark mode'
        else:
            self.page.theme_mode = ft.ThemeMode.DARK
            
            # change button accordingly
            self.theme_mode_button.icon = ft.icons.LIGHT_MODE_SHARP
            self.theme_mode_button.text = 'Light mode'
        
        self.page.update()
        self.save_theme_mode()
    
    def delete_app_data(self, e) -> None:
        #  app data rests in 'Ta-Do_data/todo_data.txt' file.
        app_data_dir = get_data_storage_path()
        try:  
            for match in glob.glob(f'{app_data_dir}/*.txt'):
                os.remove(match)
            os.rmdir(f'{app_data_dir}')
        except:
            return
    
    def save_theme_mode(self):
        theme_mode_file = open(f'{get_data_storage_path()}/theme_mode_pref.txt', 'w')
        theme_mode_file.write(self.page.theme_mode.value)
        theme_mode_file.close()
