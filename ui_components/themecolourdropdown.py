from .fn import get_data_storage_path
import flet as ft


class ThemeColourDropdown(ft.Dropdown):
    def __init__(self, colors: list, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.label = 'Color Scheme'
        self.on_change = self.save_color_option
        self.width = 250
        for color_name in colors:
            self.options.append(
                ft.dropdown.Option(color_name)
            )
    
    def save_color_option(self, e):
        file = open(f'{get_data_storage_path()}/theme_color_dropd_pref.txt', 'w')
        file.write(self.value)
        file.close()
