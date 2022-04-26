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
        self.receiver = None

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
        self.receiver.set_phrase(self.input.text)
        self.parent.current = 'audios'

    def set_data_receiver(self, receiver):
        self.receiver = receiver


class AudiosScreen(Screen):
    def __init__(self, **kwargs):
        super(AudiosScreen, self).__init__(**kwargs)
        self.source = None
        self.phrase = None
        self.intro = None

    def set_data_source(self, source):
        self.source = source

    def set_phrase(self, phrase):
        self.phrase = phrase
        if self.intro is not None:
            self.remove_widget(self.intro)
        self.intro = Label(text=self.phrase)
        self.add_widget(self.intro)


class DesktopApp(App):
    def build(self):
        manager = ScreenManager()
        input_screen = InputScreen(name='input')
        audios_screen = AudiosScreen(name='audios')

        audios_screen.set_data_source(input_screen)
        input_screen.set_data_receiver(audios_screen)

        manager.add_widget(input_screen)
        manager.add_widget(audios_screen)
        return manager


DesktopApp().run()
