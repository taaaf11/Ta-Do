import flet as ft


class AboutPage(ft.Column):
    def __init__(self, author_name: str, author_avatar_url: str | None = None, source_code_link: str | None = None, version_info: str | None = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.controls = [
            ft.Text('Written by:', size=30)
        ]
        
        if not (author_avatar_url is None):
            self.controls.append(
                ft.CircleAvatar(foreground_image_url=author_avatar_url,
                                radius=50)
            )
        
        # first avatar then name
        self.controls.append(ft.Text(author_name))
        
        if not (version_info is None):
            self.controls.append(
                ft.Text(f'Version: {version_info}', size=15)
            )
        if not (source_code_link is None):  
            self.controls.append(
                ft.Row([
                    ft.OutlinedButton(text='Source code', icon=ft.icons.LINK,
                                      on_click=lambda _:
                                      self.page.launch_url(source_code_link))
                ], alignment=ft.MainAxisAlignment.CENTER)
            )
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def build(self):
        return self
