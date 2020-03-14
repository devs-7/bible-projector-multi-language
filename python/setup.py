# Para gerar o executável rode o comando:
# python setup.py build

import os
from cx_Freeze import setup, Executable

database_path = os.path.join(os.getcwd(), 'data', 'dados.db')

executables = [
    Executable("main.py")
]

buildOptions = dict(
    packages=[],
    includes=['PyQt5'],
    include_files=[database_path],
    excludes=[]
)

setup(
    name="main",
    version="1.0",
    description="Descrição do programa",
    options=dict(build_exe=buildOptions),
    executables=executables
)
