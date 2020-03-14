import os
import PyInstaller.__main__

PyInstaller.__main__.run([
    os.path.join('main.py'),
    '--name=%s' % 'Projetor bíblico',
    '--icon=%s' % os.path.join('assets', 'img', 'icon.ico'),
    '--add-data=%s' % os.path.join('data', 'dados.db;.', 'data'),
    # '--add-binary=%s' % os.path.join('resource', 'path', '*.png'),
    '--onefile',
    '--windowed',
])
