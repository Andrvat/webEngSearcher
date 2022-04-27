from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.properties import NumericProperty

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


class MyButton(Button):
    num = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (0.2, None)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.background_color = '#04D0F9'

    def on_press(self):
        App.get_running_app().some_words.text = f'Test {self.num}'


class MyApp(App):
    def build(self):
        Window.size = (900, 600)
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.2, 0.6)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.6}

        self.some_words = Label(font_size='16', text='Win or Lose', color='white', halign='center')
        self.window.add_widget(self.some_words)

        self.create_scrollview()

        return self.window

    def create_scrollview(self):
        listNames = ['1st Button', '2nd button', '3rd button', '4th button', '5th button', '6th button']
        layout = GridLayout(cols=1, size_hint_y=None)
        layout.bind(minimum_height=layout.setter("height"))
        for i in range(6):
            button = MyButton(text=listNames[i], num=i + 1)
            layout.add_widget(button)
            layout.ids[str(i + 1)] = button
        scrollview = ScrollView(size=(Window.width, Window.height))
        scrollview.add_widget(layout)
        self.window.add_widget(scrollview)


if __name__ == "__main__":
    MyApp().run()