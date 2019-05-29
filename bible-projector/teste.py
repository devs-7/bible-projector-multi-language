def funcao(callback):
    callback('x', 'y')


funcao(lambda x, y:
       print(x, y)
       )
