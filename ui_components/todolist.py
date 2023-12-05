from .todo import Todo
from typing import TextIO
import flet as ft


class TodoList(ft.ListView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.controls = []

    def add_todo(self, todo: Todo) -> None:
        if not len(todo.content) == 0:
            self.controls.append(todo)
        for atodo in self.controls:
            if atodo.done:  # it is true, i.e. todo is completed
                self.controls.remove(atodo)  # prune to-do's
        self.update()
    
    @staticmethod
    def _into_lines(file: TextIO) -> list:  # put lines of file into a list
        eof = False
        lines = list()

        # read file
        while not eof:
            line = file.readline()
            if not line:
                eof = True
            if line == '': # line is empty
                continue
            if line[-1] == '\n':
                lines.append(line[:-1])
                continue
            lines.append(line)
        
        return lines
    
    def read_from_file(self) -> None:
        try:
            file = open('todo_data.txt', 'r')
        except:
            return
        
        lines_of_file = self._into_lines(file)
        file.close()
        
        for line in lines_of_file:
            line_contents = line.split('/')  # content in each line is like this
            content, done = line_contents[1], line_contents[0]
            
            if done == '0':  # state of the checkbox
                self.controls.append(Todo(content))  # default value of second arg is False
            else:  # it is '1'
                self.controls.append(Todo(content, True))
                
        self.update()
    
    def save_to_file(self) -> None:
        file = open('todo_data.txt', 'w')
        for item in self.controls:
            content, done = item.get_data()
            if done == True:  # checkbox is true
                file.write(f'1/{content}\n')
                continue
            else:  # is false
                file.write(f'0/{content}\n')
        file.close()

    def build(self):
        return self
