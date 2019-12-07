import helper.bible as bible
import windows.projection as window_projection
import traceback
import helper.colors as colors
import sqlite3

from kivy.app import App
from kivy.core.window import Window
from helper.kivy_componentes import *
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Main(App):
    def build(self):
        # Box
        self.box = BoxLayout(orientation='vertical')
        self.box_header = BoxLayout(orientation='horizontal')
        self.box_main = BoxLayout(orientation='horizontal')

        # Header
        self.pesquisar_button = Button(text='Pesquisar', on_press=self.pesquisar)
        self.pesquisa_text_input = TextInput(multiline=False)

        # Main
        self.preview = Label()
        self.historic = Label()

        # Estilos
        self.pesquisa_text_input.cursor_color = (0, 0, 0, 1)
        self.pesquisar_button.background_color = colors.name['dracula_light']

        self.box_header.add_widget(self.pesquisa_text_input)
        self.box_header.add_widget(self.pesquisar_button)
        self.box_main.add_widget(self.preview)
        self.box_main.add_widget(self.historic)
        self.box.add_widget(self.box_header)
        self.box.add_widget(self.box_main)
        return self.box

    def add_widget(self, widget):
        self.box.add_widget(widget)

    def pesquisar(self, button):
        try:
            window_projection.run()
            pesquisa = self.pesquisa_text_input.text
            self.pesquisa_text_input.text = ''
            verso = bible.query_one(pesquisa)
            self.pesquisa_text_input.text = bible.format_dict_ver(verso)
            self.preview.text = verso['text']
        except (IndexError, sqlite3.OperationalError):
            self.preview.text = 'Pesquisa incorreta.'
        except TypeError:
            self.preview.text = 'Texto não encontrado.'
        except Exception as e:
            self.preview.text = ', '.join(e.args)
            traceback.print_exc()


# Window.maximize()
Window.clearcolor = colors.name['dracula_dark']

main = Main()
main.title = 'Bible projector'
main.run()
