import os
import PyInstaller.__main__

PyInstaller.__main__.run([
    '--name=%s' % 'Projetor bíblico',
    '--onefile',
    '--windowed',
    '--add-binary=%s' % os.path.join('resource', 'path', '*.png'),
    '--add-data=%s' % os.path.join('resource', 'path', '*.txt'),
    '--icon=%s' % os.path.join('resource', 'path', 'icon.ico'),
    os.path.join('my_package', '__main__.py'),
])
