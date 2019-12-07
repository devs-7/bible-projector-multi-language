import helper.bible as bible
import windows.projection as window_projection
import traceback

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from helper.kivy_componentes import *


class Main(App):
    def build(self):
        # Box
        self.box = BoxLayout(orientation='vertical')
        self.box_header = BoxLayout(orientation='horizontal')
        self.box_main = BoxLayout(orientation='horizontal')

        # Header
        self.pesquisar_button = Button(text='pesquisar', on_press=self.pesquisar_button_click)
        self.pesquisa_text_input = TextInput(multiline=False)

        # Main
        self.preview = Label()
        self.historic = Label()

        # Estilos
        self.pesquisa_text_input.cursor_color = (0, 0, 0, 1)
        self.pesquisar_button.background_color = (2, 2, 2, 1)

        self.box_header.add_widget(self.pesquisa_text_input)
        self.box_header.add_widget(self.pesquisar_button)
        self.box_main.add_widget(self.preview)
        self.box_main.add_widget(self.historic)
        self.box.add_widget(self.box_header)
        self.box.add_widget(self.box_main)
        return self.box

    def add_widget(self, widget):
        self.box.add_widget(widget)

    def pesquisar_button_click(self, button):
        try:
            pesquisa = self.pesquisa_text_input.text
            self.pesquisa_text_input.text = ''
            verso = bible.query_one(pesquisa)
            self.pesquisa_text_input.text = bible.format_dict_ver(verso)
            self.preview.text = verso['text']
        except:
            traceback.print_exc()

main = Main()
main.title = 'Bible projector'
main.run()

# Configuração da tela
# window.title("Bible projector")
# window.geometry('800x600')
# window.wm_state('zoomed')
#
# for i in range(10):
#     for j in range(10):
#         Label(text=f'{i + j}').grid(row=i, column=j)
#
# window.mainloop()

# while True:
#     try:
#         q = input("Digite sua pesquisa: ")
#         x = bible.query_one(q)
#         if x is not None:
#             print()
#             print(f"{x['liv']} {x['cap']}:{x['ver']}\n{x['text']}")
#             print()
#     except IndexError as e:
#         print('Pesquisa inválida')
#     except:
#         traceback.print_exc()
