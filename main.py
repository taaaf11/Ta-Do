from ui_components import TodoApp, TodoInputDialog
import flet as ft


def main(page: ft.Page):
    page.title = 'Ta-Do'
    page.theme_mode = 'dark'
    
    page.window_height = 600
    page.window_width = 500
    page.window_resizable = False
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def create_todo(e):
        add_todo_dialog = TodoInputDialog()
        page.dialog = add_todo_dialog
        page.dialog.open = True
        page.dialog.on_dismiss = lambda _: home_view.add_todo(add_todo_dialog.get_text())
        page.update()

    page.appbar = ft.AppBar(title=ft.Text('Ta-Do'))

    page.drawer = ft.NavigationDrawer(controls=[
        ft.NavigationDrawerDestination(
            icon=ft.icons.HOME_OUTLINED,
            label='Home',
            selected_icon=ft.icons.HOME_ROUNDED
        )
    ])

    page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.ADD_ROUNDED, on_click=create_todo)

    home_view = TodoApp()

    page.add(home_view)


if __name__ == '__main__':
    ft.app(target=main)
