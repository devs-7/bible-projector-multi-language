import models.bible as bible
import traceback

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from helper.kivy_componentes import *


class Main(App):
    def build(self):
        box = BoxLayout(orientation='vertical')

        pesquisar_button = Button(text='pesquisar', on_press=lambda x: print(x))
        pesquisa_text_input = TextInput()

        pesquisa_text_input.multiline = False
        pesquisa_text_input.cursor_color = (0, 0, 0, 1)

        box.add_widget(Lista(['1', '2', '3']))
        box.add_widget(pesquisa_text_input)
        box.add_widget(pesquisar_button)
        return box


Main().run()

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
