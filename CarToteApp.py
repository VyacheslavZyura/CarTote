from kivy.app import App
from kivy.uix.button import Button

from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 100%)
Config.set('graphics', 'height', 100%)


class CarToteApp(App):

    def build(self):
        pass

if __name__ == "__main__":
     CarToteApp().run()
