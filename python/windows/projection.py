from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from helper.kivy_componentes import *


class Main(App):
    def build(self):
        return Label(text='opa')


def run():
    main = Main()
    main.title = 'Projeção'
    main.run()
