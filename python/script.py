import helper.bible as bible
import helper.db_controller as db

livros = list(map(lambda x: x[0], db.query(f"SELECT nome FROM livros ORDER BY id")))

for liv in livros:
    print(f'<Menu mnemonicParsing="false" text="{liv}">')
    print('\t<items>')

    for cap in range(1, 1000):
        try:
            if ver == 1:
                break
        except:
            pass

        print(f'\t\t<Menu mnemonicParsing="false" text="{cap}">')
        print('\t\t\t<items>')

        for ver in range(1, 1000):
            x = bible.query(f"{liv} {cap} {ver}")
            if x == None:
                x = bible.query(f"{liv} {cap+1} {1}")
                if x == None:
                    ver = 1
                break
            else:
                print(f'\t\t\t\t<MenuItem mnemonicParsing="false" text="{ver}"/>')

        print('\t\t\t</items>')
        print('\t\t</Menu>')



    print('\t</items>')
    print('</Menu>')
