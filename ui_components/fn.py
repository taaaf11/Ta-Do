import os, platform, flet as ft

def get_data_storage_path() -> str:
        current_system = platform.system()
        if current_system == 'Windows':
            storage_path = os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local', 'Ta-Do')
        elif current_system == 'Linux':
            storage_path = os.path.join(os.environ['HOME'], '.local', 'share', 'Ta-Do')
        elif current_system == 'Darwin':  # mac os
            storage_path = os.path.join(os.environ['HOME'], 'Library', 'Ta-Do')
        return storage_path

def get_saved_theme_color_name() -> str:
    theme_color_data_path = f'{get_data_storage_path()}/theme_color_pref.txt'
    pine_green = '#01666f'  # default color
    if os.path.isfile(theme_color_data_path):
        theme_color_file = open(theme_color_data_path)
        theme_color = theme_color_file.read()
        theme_color_file.close()
        return theme_color if not theme_color == 'Default' else pine_green
    else:
        return pine_green

def get_saved_theme_mode() -> ft.ThemeMode:  # dark or light
    theme_mode_path = f'{get_data_storage_path()}/theme_mode_pref.txt'
    default_theme_mode = ft.ThemeMode.DARK
    if os.path.isfile(theme_mode_path):
        theme_mode_file = open(theme_mode_path)
        theme_mode = theme_mode_file.read()
        theme_mode_file.close()
        return ft.ThemeMode.LIGHT if theme_mode == 'light' else \
            default_theme_mode
    else:
        return default_theme_mode  # default theme mode
