import flet as ft


class Todo(ft.Row):
    def __init__(self, content: str, done: bool = False, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.content = content
        self.done = done
        self.checkbox = ft.Checkbox(label=self.content, value=self.done, on_change=self.on_checkbox_change)
        
        self.rename_button = ft.TextButton(icon=ft.icons.EDIT_SHARP, on_click=self.edit,
                                    visible=True, icon_color=ft.colors.GREY)
        
        self.delete_button = ft.TextButton(icon=ft.icons.DELETE_OUTLINE, on_click=self.delete,
                                    visible=False, icon_color=ft.colors.GREY)
        
        if self.checkbox.value:  # when read from file, checkmark-ed todo's don't show
            self.delete_button.visible = True  # delete automatically
        
        self.buttons_row = ft.Row([self.rename_button, self.delete_button])
        
        self.controls = [self.checkbox, self.buttons_row]
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
        self.page.controls[0].save_data()  # read comments in the function defined below
    
    def delete(self, e) -> None:
        # at self.page.controls[0], TodoApp() instance rests.
        # Calling its method del_todo to delete a todo
        # see 'page.add' (last) lines of main.py
        self.page.controls[0].del_todo(self)
    
    def edit(self, e):
        page_instance = self.page
        page_instance.dialog.title = ft.Text('Edit todo...')
        page_instance.dialog.text_field.value = self.checkbox.label
        page_instance.dialog.open = True
        page_instance.dialog.on_dismiss = lambda _: page_instance.controls[0].add_todo(Todo(page_instance.dialog.text_field.value))
        page_instance.controls[0].del_todo(self)
        page_instance.update()
    
    def get_data(self) -> tuple:  # an 'interface' to get values of Todo instance
        return self.checkbox.label, self.checkbox.value
        
    def build(self):
        return self
