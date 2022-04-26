from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput


class DesktopApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color_code = '#79FF8F'
        self.size_hint = (1, 0.7)
        self.window = None
        self.question = Label(
            text="Your phrase of interest?",
            font_size=24,
            color=self.color_code
        )
        self.input = TextInput(
            multiline=False,
            padding_y=(15, 15),
            size_hint=self.size_hint
        )
        self.submit = Button(
            text="Submit phrase",
            size_hint=self.size_hint,
            bold=True,
            background_color=self.color_code,
        )

    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.4, 0.3)
        self.window.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        self.window.add_widget(self.question)

        self.window.add_widget(self.input)

        self.submit.bind(on_press=self.callback)
        self.window.add_widget(self.submit)

        return self.window

    def callback(self, instance):
        self.question.text = "Hello " + self.input.text + "!"


DesktopApp().run()
