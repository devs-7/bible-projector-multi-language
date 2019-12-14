with open('bibles_txt/nvi.txt', encoding='utf-8') as file:
    bible_txt = list(file.read())
    for n, c in enumerate(bible_txt):
        if c == ']':
            i = 0
            while True:
                i += 1
                if bible_txt[n - i] == ' ':
                    bible_txt[n - i] = ':'
                    break
    bible_txt = ''.join(bible_txt)
    with open('bibles_txt/nvi_py.txt', 'w', encoding='utf-8') as f:
        f.write(bible_txt)
