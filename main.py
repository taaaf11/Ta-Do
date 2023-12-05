#
# App Name: Ta-Do
# Author: Muhammad Altaaf
# Contact email: taafuuu@gmail.com
# Description: A simple to-do app.
#


from ui_components import TodoApp, TodoInputDialog, SettingsPage, AboutPage
import flet as ft


def main(page: ft.Page):
    page.title = 'Ta-Do'
    page.theme = ft.Theme(color_scheme_seed='#01666f')  # pine green
    page.theme_mode = ft.ThemeMode.DARK
    
    page.window_height = 400
    page.window_width = 500
    page.window_resizable = False
    
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def create_todo(e):
        add_todo_dialog = TodoInputDialog()
        page.dialog = add_todo_dialog
        page.dialog.open = True
        page.dialog.on_dismiss = lambda _: home_view.add_todo(add_todo_dialog.get_todo())
        page.update()
    
    # we don't our todo's to be center aligned, but we want contents of other 'pages'
    # to be vertically center aligned, so this is the solution
    old_page_vertical_alignment = page.vertical_alignment
    
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

    page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.ADD_SHARP, on_click=create_todo, shape=ft.CircleBorder())

    home_view = TodoApp()
    settings_view = SettingsPage(home_view, page, visible=False)
    about_view = AboutPage(author_name='Muhammad Altaaf', visible=False)

    page.add(home_view, settings_view, about_view)
    
    # get data from file, couldn't do any better
    home_view.todos.read_from_file()
    page.update()


if __name__ == '__main__':
    ft.app(target=main)
