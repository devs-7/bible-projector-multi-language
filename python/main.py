import models.bible as bible
import traceback

while True:
    try:
        q = input("Digite sua pesquisa: ")
        x = bible.query_one(q)
        if x is not None:
            print()
            print(f"{x['liv']} {x['cap']}:{x['ver']}\n{x['text']}")
            print()
    except IndexError as e:
        print('Pesquisa inválida')
    except:
        traceback.print_exc()
