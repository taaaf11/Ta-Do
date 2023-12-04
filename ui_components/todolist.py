import flet as ft
from .todo import Todo


class TodoList(ft.ListView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.controls = []

    def add_todo(self, todo: Todo):
        self.controls.append(todo)
        self.update()

    def build(self):
        return self
