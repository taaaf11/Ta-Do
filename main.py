#
# App Name: Ta-Do
# Author: Muhammad Altaaf
# Contact email: taafuuu@gmail.com
# Description: A simple to-do app.
# Version: 1.1.0
# Source code: 'https://www.github.com/taaaf11/Ta-Do'
#


from ui_components import TodoApp, TodoInputDialog, SettingsPage, AboutPage
import flet as ft


def main(page: ft.Page):
    github_repo_link = 'https://www.github.com/taaaf11/Ta-Do'
    
    page.title = 'Ta-Do'
    page.theme = ft.Theme(color_scheme_seed='#01666f')  # pine green
    page.theme_mode = ft.ThemeMode.DARK
    
    page.window_height = 450
    page.window_width = 530
    page.window_resizable = False
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # these two variables' values would be shared between the two very defined functions
    todo_dialog = TodoInputDialog()
    page.dialog = todo_dialog
    
    def handle_kbd_shortcuts(e: ft.KeyboardEvent):
        # when escape key is pressed, the dialog dismisses
        # in addition, we want the value to be empty, so that a
        # todo is not added on dialog dismiss
        if e.key == 'Escape':
            todo_dialog.text_field.value = ''
        
        # user presses backspace key even when the input field is empty
        elif e.key == 'Backspace' and todo_dialog.text_field.value == '':
            page.dialog.open = False
        
        elif e.key == 'N':  # user presses 'n' key.
            if todo_dialog.open:  # user is entering something into todo input dialog
                return  # don't do anything if the dialog is open
            create_todo()
        
        elif e.key == 'Delete':  # deletes all checked todo's
            home_view.del_all_checked_todos()
        
        page.update()
    
    def create_todo():
        page.dialog.title = ft.Text('Create a new ToDo...')
        page.dialog.open = True
        page.dialog.on_dismiss = lambda _: home_view.add_todo(todo_dialog.get_todo());\
            todo_dialog.text_field.value = ''  # cleaning the value of box
        page.update()
    
    # we don't our todo's to be center aligned, but we want contents of other 'pages'
    # to be vertically center aligned, the solution is to keep the vertical alignment of the
    # home page in a variable and use it when the home page is requested.
    old_page_vertical_alignment = page.vertical_alignment
    
    page.on_keyboard_event = handle_kbd_shortcuts
    
    def navigate_to_page(e):
        selected_page = e.control.selected_index
        if selected_page == 0:
            home_view.visible = True
            settings_view.visible = False
            about_view.visible = False
            
            # Read comments above for variable old_page_vertical_alignment
            page.vertical_alignment = old_page_vertical_alignment
        elif selected_page == 1:
            home_view.visible = False
            settings_view.visible = True
            about_view.visible = False
            
            # Read comments above for variable old_page_vertical_alignment
            page.vertical_alignment = ft.MainAxisAlignment.CENTER
        elif selected_page == 2:
            home_view.visible = False
            settings_view.visible = False
            about_view.visible = True
            
            # Read comments above for variable old_page_vertical_alignment
            page.vertical_alignment = ft.MainAxisAlignment.CENTER
        
        page.update()

    page.appbar = ft.AppBar(title=ft.Text('Ta-Do'))

    page.drawer = ft.NavigationDrawer(controls=[
        ft.NavigationDrawerDestination(
            icon=ft.icons.HOME_OUTLINED,
            label='Home',
            selected_icon=ft.icons.HOME_SHARP
        ),
        ft.NavigationDrawerDestination(
            icon=ft.icons.SETTINGS_OUTLINED,
            label='Settings',
            selected_icon=ft.icons.SETTINGS_SHARP
        ),
        ft.Divider(thickness=2),
        ft.NavigationDrawerDestination(
            icon=ft.icons.LIGHTBULB_OUTLINE,
            label='About',
            selected_icon=ft.icons.LIGHTBULB_SHARP
        )
    ], selected_index=0, on_change=navigate_to_page)

    page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.ADD_SHARP, on_click=lambda _: create_todo(), shape=ft.CircleBorder())
    
    home_view = TodoApp()
    settings_view = SettingsPage(home_view, visible=False)
    about_view = AboutPage(author_name='Muhammad Altaaf', source_code_link=github_repo_link, version_info='1.1.0', visible=False)

    page.add(home_view, settings_view, about_view)
    
    # get data from file, couldn't do any better
    home_view.todos.read_from_file()
    page.update()


if __name__ == '__main__':
    ft.app(target=main)
