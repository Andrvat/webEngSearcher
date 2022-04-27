import os.path

from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

from src.converter import convert_to_secs


class InputScreen(Screen):
    def __init__(self, **kwargs):
        super(InputScreen, self).__init__(**kwargs)
        self.receiver = None

        self.default_color = '#79FF8F'
        self.size_hint = (1, 0.7)
        self.question = Label(
            text="Your phrase of interest?",
            font_size=24,
            color=self.default_color
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
            background_color=self.default_color,
        )

        layout = GridLayout()
        layout.cols = 1
        layout.size_hint = (0.5, 0.4)
        layout.pos_hint = {'center_x': 0.5, 'center_y': 0.8}

        layout.add_widget(self.question)
        layout.add_widget(self.input)
        layout.add_widget(self.submit)

        self.submit.bind(on_press=self.callback)

        self.add_widget(layout)

    def callback(self, instance):
        self.receiver.set_phrase(self.input.text)
        self.receiver.prepare()
        self.parent.current = 'audios'

    def set_data_receiver(self, receiver):
        self.receiver = receiver


class AudiosScreen(Screen):
    view = ObjectProperty(None)

    def __init__(self, explorer, **kwargs):
        super(AudiosScreen, self).__init__(**kwargs)
        self.sound_buttons = {}
        self.explorer = explorer
        self.default_color = '#79FF8F'
        self.layout = None
        self.source = None
        self.phrase = None

    def prepare(self):
        self.ids.intro_label.text = f'Your phrase: {self.phrase}'
        self.layout = GridLayout()
        self.layout.cols = 1
        self.layout.spacing = 10
        self.layout.size_hint_y = None
        self.layout.bind(minimum_height=self.layout.setter("height"))

        usages = self.explorer.get_usage(text=self.phrase)

        for i, usage in enumerate(usages):
            sound = None
            if os.path.exists(f"{os.path.dirname(os.path.realpath(__file__))}/static/{usage['video_id']}.ogg"):
                sound = SoundLoader.load(f"static/{usage['video_id']}.ogg")

            info = {'usage': usage, 'sound': sound}
            self.add_label(text='')
            self.add_label(text=f"Episode №{i + 1}", font_size=20)
            self.add_label(text=usage['video_title'])
            play_button = self.build_button(text='play', on_press=self.play_audio)
            stop_button = self.build_button(text='stop', on_press=self.stop_audio)
            self.sound_buttons[play_button] = info
            self.sound_buttons[stop_button] = info
            self.layout.add_widget(play_button)
            self.layout.add_widget(stop_button)

        scroll = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        scroll.add_widget(self.layout)
        self.view.add_widget(scroll)

    def set_data_source(self, source):
        self.source = source

    def set_phrase(self, phrase):
        self.phrase = phrase

    def play_audio(self, instance):
        usage = self.sound_buttons[instance]['usage']
        sound = self.sound_buttons[instance]['sound']
        if sound is not None:
            sound.seek(convert_to_secs(usage['hours'], usage['minutes'], usage['seconds']))
            sound.play()

    def stop_audio(self, instance):
        sound = self.sound_buttons[instance]['sound']
        if sound is not None:
            sound.stop()

    def add_label(self, text, padding=2, font_size=16):
        self.layout.add_widget(Label(text=text, font_size=font_size))
        for _ in range(padding):
            self.layout.add_widget(Label(text=''))

    def build_button(self, text, on_press):
        return Button(text=text,
                      size=(50, 50),
                      on_press=on_press,
                      size_hint=(1, None),
                      bold=True,
                      background_color=self.default_color,
                      )


class DesktopApp(App):
    def __init__(self, explorer, **kwargs):
        super().__init__(**kwargs)
        Builder.load_file("static/audios.kv")
        self.explorer = explorer

    def build(self):
        manager = ScreenManager()
        input_screen = InputScreen(name='input')
        audios_screen = AudiosScreen(name='audios', explorer=self.explorer)

        audios_screen.set_data_source(input_screen)
        input_screen.set_data_receiver(audios_screen)

        manager.add_widget(input_screen)
        manager.add_widget(audios_screen)
        return manager
