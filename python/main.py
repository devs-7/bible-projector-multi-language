import models.bible as bible
import traceback

from tkinter import *

window = Tk()

# Configuração da tela
window.title("Bible projector")
window.geometry('800x600')
window.wm_state('zoomed')

for i in range(10):
    for j in range(10):
        Label(text=f'{i + j}').grid(row=i, column=j)

window.mainloop()

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
