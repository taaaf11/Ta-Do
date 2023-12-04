from ui_components import TodoApp, PopupInput
import flet as ft


def main(page: ft.Page):
    page.title = 'Ta-Do'
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def create_todo(e):
        add_todo_dialog = PopupInput()
        page.dialog = add_todo_dialog
        page.dialog.open = True
        page.dialog.on_dismiss = lambda _: home_view.add_todo(add_todo_dialog.get_text())
        # home_view.add_todo(todo_dialog.text_field.value)
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
