from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Label


class Lista(BoxLayout):
    def __init__(self, lista, **kwargs):
        self.orientation = 'vertical'
        super().__init__(**kwargs)
        for item in lista:
            self.add_widget(Label(text=item))
