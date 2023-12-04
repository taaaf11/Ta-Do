from .todolist import TodoList
from .todo import Todo
import flet as ft
import os


class TodoApp(ft.UserControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.todos = TodoList()

    def add_todo(self, todo: Todo):
        self.todos.add_todo(todo)
        self.todos.save_to_file()
        self.update()

    def build(self):
        return self.todos
