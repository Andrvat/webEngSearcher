import os

os.environ["KIVY_AUDIO"] = "ffpyplayer"


from kivy.app import App
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.scrollview import ScrollView
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
        self.receiver.prepare()
        self.parent.current = 'audios'

    def set_data_receiver(self, receiver):
        self.receiver = receiver


class AudiosScreen(Screen):
    view = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(AudiosScreen, self).__init__(**kwargs)
        self.layout = None
        self.color_code = '#79FF8F'
        self.sound = None
        self.source = None
        self.phrase = None

    def prepare(self):
        self.ids.intro_label.text = f'Your phrase: {self.phrase}'
        self.layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter("height"))

        self.sound = SoundLoader.load('static/1.wav')

        for _ in range(20):
            self.build_label(text='', padding=2)
            self.build_label(text=self.sound.source, padding=2)
            self.build_label(text=self.phrase, padding=2)
            self.layout.add_widget(Button(text='play',
                                          size=(50, 50),
                                          on_press=self.playaudio,
                                          size_hint=(1, None),
                                          bold=True,
                                          background_color=self.color_code,
                                          ))
            self.layout.add_widget(Button(text='stop',
                                          size=(50, 50),
                                          on_press=self.stopaudio,
                                          size_hint=(1, None),
                                          bold=True,
                                          background_color=self.color_code,
                                          ))
            self.build_label(text='', padding=6)
        scroll = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        scroll.add_widget(self.layout)
        self.view.add_widget(scroll)

    def set_data_source(self, source):
        self.source = source

    def set_phrase(self, phrase):
        self.phrase = phrase

    def playaudio(self, instance):
        self.sound.seek(100)
        self.sound.play()

    def stopaudio(self, instance):
        self.sound.stop()

    def build_label(self, text, padding):
        self.layout.add_widget(Label(text=text))
        for _ in range(padding):
            self.layout.add_widget(Label(text=''))


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


Builder.load_file("static/audios.kv")
# TODO: https://stackoverflow.com/questions/63882665/how-to-use-slider-as-progress-bar-and-control-audio-in-kivy-python
DesktopApp().run()
