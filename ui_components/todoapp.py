from .todolist import TodoList
from .todo import Todo
import flet as ft


class TodoApp(ft.UserControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.todos = TodoList()

    def add_todo(self, todo: Todo) -> None:
        self.todos.add_todo(todo)  # auto saves
        self.update()
    
    def del_todo(self, todo: Todo) -> None:
        self.todos.del_todo(todo)  # auto saves
        self.update()
    
    def save_data(self) -> None:
        self.todos.save_to_file()  # settings page button
    
    # all above functions are just wrapper to the functions of
    # TodoList() class functions

    def build(self):
        return self.todos
