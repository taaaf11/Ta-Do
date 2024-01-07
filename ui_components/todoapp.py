from .fn import get_data_storage_path
from .todolist import TodoList
from .todo import Todo
import flet as ft
import os


class TodoApp(ft.UserControl):
    def __init__(self, on_scroll, *args, **kwargs):  # on_scroll is just a wrapper for the on_scroll of TodoList 
        super().__init__(*args, **kwargs)
        self.todos = TodoList(on_scroll=on_scroll)

    def add_todo(self, todo: Todo) -> None:
        path = get_data_storage_path()
        if not os.path.isdir(path):
            os.mkdir(path)
        self.todos.add_todo(todo)  # auto saves
        self.update()
    
    def del_todo(self, todo: Todo) -> None:
        self.todos.del_todo(todo)  # auto saves
        self.update()
    
    def del_all_checked_todos(self) -> None:
        self.todos.del_all_checked()
    
    def save_data(self) -> None:
        self.todos.save_to_file()  # settings page button
    
    # all above functions are wrapper for the functions of
    # TodoList() class functions

    def build(self):
        return self.todos
