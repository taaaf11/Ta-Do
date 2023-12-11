import flet as ft


class AboutPage(ft.Column):
    def __init__(self, author_name: str, source_code_link: str | None = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.author_name = author_name
        self.source_code_link = source_code_link
        self.controls = [
            ft.Text('Written by:', size=30),
            ft.CircleAvatar(foreground_image_url='https://www.github.com/taaaf11.png?size=120px',
                            radius=50),
            ft.Text(self.author_name, size=20),
            ft.Text('Version: 1.0.1', size=15)
        ]
        if not(self.source_code_link is None):  
            self.controls.append(
                ft.Row([
                    # ft.Text('Source code:'),
                    ft.OutlinedButton(text='Source code', icon=ft.icons.LINK,
                                      on_click=lambda _:
                                      self.page.launch_url(source_code_link))
                ], alignment=ft.MainAxisAlignment.CENTER)
            )
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def build(self):
        return self
