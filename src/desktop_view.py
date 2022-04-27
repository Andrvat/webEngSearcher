from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
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
        self.receiver.create()
        self.parent.current = 'audios'

    def set_data_receiver(self, receiver):
        self.receiver = receiver


class AudiosScreen(Screen):
    def __init__(self, **kwargs):
        super(AudiosScreen, self).__init__(**kwargs)
        self.sound = None
        self.source = None
        self.phrase = None
        self.intro = None

    def set_data_source(self, source):
        self.source = source

    def set_phrase(self, phrase):
        self.phrase = phrase

    def create(self):
        layout = GridLayout()
        layout.cols = 1

        self.sound = SoundLoader.load('static/1.wav')
        self.widgets = []
        for i in range(5):
            self.widgets.append(Label(text=self.sound.source
                                      ))
            self.widgets.append(Label(text=str(self.sound.length)
                                      ))
            self.widgets.append(Button(text='play',
                                       on_press=self.playaudio
                                       ))
            self.widgets.append(Button(text='stop',
                                       on_press=self.stopaudio
                                       ))
            self.widgets.append(Label(text=' '))

        for label in self.widgets:
            layout.add_widget(label)

        self.add_widget(layout)

    def playaudio(self, instance):
        self.sound.play()

    def stopaudio(self, instance):
        self.sound.stop()


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


# TODO: https://stackoverflow.com/questions/63882665/how-to-use-slider-as-progress-bar-and-control-audio-in-kivy-python
DesktopApp().run()
