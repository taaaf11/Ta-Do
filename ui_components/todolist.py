from .fn import get_data_storage_path
from .todo import Todo
from typing import TextIO
import flet as ft
import os


class TodoList(ft.ListView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.controls = []
        self.height = 320
        self.app_data_dir = get_data_storage_path()

    def add_todo(self, todo: Todo, index=None) -> None:
        if not len(todo.content) == 0:  # dialog is not empty
            if index is None:
                self.controls.append(todo)
            else:
                self.controls.insert(index, todo)
        self.update()
        self.save_to_file()  # auto save
    
    def del_todo(self, todo: Todo) -> None:
        self.controls.remove(todo)
        self.update()
        self.save_to_file()  # auto save
    
    def del_all_checked(self) -> None:
        for todo in self.controls.copy():
            if todo.done:
                self.del_todo(todo)
    
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
        # it is first run, or user deleted the app data.
        if not os.path.isdir(self.app_data_dir):
            os.mkdir(self.app_data_dir)
            return
        else:
            # data file does not exist
            if not os.path.isfile(f'{self.app_data_dir}/todo_data.txt'):
                open(f'{self.app_data_dir}/todo_data.txt', 'w').close()  # create an empty file
                return
        
        file = open(f'{self.app_data_dir}/todo_data.txt', 'r')
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
        # write mode is used to save only what the
        # user is seeing. opening the file in append
        # mode causes the repitition of data in file
        file = open(f'{self.app_data_dir}/todo_data.txt', 'w')
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
