from .todo import Todo
from typing import TextIO
import flet as ft
import os


class TodoList(ft.ListView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.controls = []
        if os.path.isfile('todo_data.txt'):
            self.read_from_file()

    def add_todo(self, todo: Todo):
        self.controls.append(todo)
        self.update()
    
    @staticmethod
    def _into_lines(file: TextIO):
        eof = False
        lines = list()

        # read file
        while not eof:
            line = file.readline()
            if not line:
                eof = True
            if line == '': # line is empty
                continue
            lines.append(line)
        
        return lines
    
    def read_from_file(self):
        file = open('todo_data.txt', 'r')
        lines_of_file = self._into_lines(file)
        
        for line in lines_of_file:
            line_contents = line.split('/')  # content in each line is like this
            if line_contents[0] == '0':  # state of the checkbox
                self.controls.append(Todo(line_contents))  # default value of second arg is False
            else:  # it is '1'
                self.controls.append(Todo(line_contents, True))
                
        self.update()
    
    def save_to_file(self):
        file = open('todo_data.txt', 'a')
        for item in self.controls:
            content, done = item.get_data()
            if done:  # checkbox is true
                file.write(f'0/{content}')
            else:  # is false
                file.write(f'1/{content}')

    def build(self):
        return self
