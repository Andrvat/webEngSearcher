from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput


class InputScreen(Screen):
    def __init__(self, **kwargs):
        super(InputScreen, self).__init__(**kwargs)

        self.color_code = '#79FF8F'
        self.size_hint = (1, 0.7)
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

        self.main = GridLayout()
        self.main.cols = 1
        self.main.size_hint = (0.5, 0.4)
        self.main.pos_hint = {'center_x': 0.5, 'center_y': 0.8}

        self.main.add_widget(self.question)
        self.main.add_widget(self.input)
        self.main.add_widget(self.submit)

        self.submit.bind(on_press=self.callback)

        self.add_widget(self.main)

    def callback(self, instance):
        self.question.text = "Hello " + self.input.text + "!"


class DesktopApp(App):
    def build(self):
        manager = ScreenManager()
        input_screen = InputScreen(name='input')

        manager.add_widget(input_screen)
        return manager


DesktopApp().run()
