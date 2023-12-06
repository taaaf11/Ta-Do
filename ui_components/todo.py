from .button import Button
import flet as ft


class Todo(ft.Row):
    def __init__(self, content: str, done: bool = False, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # self.todo_list_inst = todo_list_inst
        self.content = content
        self.done = done
        self.checkbox = ft.Checkbox(label=self.content, value=self.done, on_change=self.on_checkbox_change)
        
        self.delete_button = Button(icon=ft.icons.DELETE_OUTLINE, on_click=self.delete,
                                    visible=False, icon_color=ft.colors.GREY)
        
        self.controls = [self.checkbox, self.delete_button]
        self.alignment = ft.MainAxisAlignment.SPACE_BETWEEN
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.expand = True
    
    def on_checkbox_change(self, e) -> None:
        self.done = self.checkbox.value  # changing the value of class variable accordingly
        if self.done == True:            # if a todo is checked, delete button appears
            self.delete_button.visible = True
        else:                            # otherwise not
            self.delete_button.visible = False
        self.update()
    
    def delete(self, e) -> None:
        # at self.page.controls[0], TodoApp() instance rests.
        # Calling its method del_todo to delete a todo
        # see 'page.add' (last) lines of main.py
        self.page.controls[0].del_todo(self)
    
    def get_data(self) -> tuple:  # an 'interface' to get values of Todo instance
        return self.checkbox.label, self.checkbox.value
        
    def build(self):
        return self
