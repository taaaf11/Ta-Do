import flet as ft


# Created just for developer convenience.
# Can't put size=smth everywhere in source.
class SimpleText(ft.Text):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size = 15


# said it already
class HeadingText(SimpleText):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size = 16
        self.weight = ft.FontWeight.BOLD


class HelpPage(ft.Column):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.controls = [
            HeadingText('Home Page'),
            SimpleText('This is the initial view when you open the app. Here you will see a \'+\' plus button, which is used for adding a todo. Todo\'s can be edited or deleted as per user needs.\n'),

            HeadingText('Settings Page'),
            SimpleText('Here you will have the options to change the overall functionality of the app.'),

            SimpleText('For theming and colors:', italic=True),
            SimpleText('• Button for switching dark and light modes.'),
            SimpleText('• A convenient dropdown menu for changing the base colour scheme of the app.'),    
            SimpleText('• Also, a button is provided to clear the app data, if the user wishes.\n'),

            HeadingText('Help Page'),
            SimpleText('This help section.\n'),

            HeadingText('About Page'),
            SimpleText('About of this app.\n')
        ]
    
    def inc_size(self):
        for text in self.controls:
            text.size += 1
        self.update()
    
    def dec_size(self):
        for text in self.controls:
            text.size -= 1
        self.update()
