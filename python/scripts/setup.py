import os
import shutil
import traceback
from contextlib import suppress

import PyInstaller.__main__

from scripts import Script

application_name = 'Projetor bíblico'

assets_folder_path = os.path.join('data')
dist_folder_path = os.path.join('dist')
assets_dist_folder_path = os.path.join(dist_folder_path, 'data')


def setup():
    try:
        PyInstaller.__main__.run([
            os.path.join('main.py'),
            '--name=%s' % application_name,
            '--icon=%s' % os.path.join('assets', 'img', 'icon.ico'),
            '--add-data=%s' % os.path.join('data', 'bible.db;.', 'data'),
            # '--add-binary=%s' % os.path.join('resource', 'path', '*.png'),
            '--onefile',
            '--windowed',
        ])
    except:
        traceback.print_exc()
    finally:
        with suppress(FileNotFoundError):
            shutil.rmtree('build')

        with suppress(FileNotFoundError):
            os.remove(f'{application_name}.spec')

        with suppress(FileExistsError):
            os.mkdir(assets_dist_folder_path)


class SetupScript(Script):
    def __str__(self) -> str:
        return 'Setup'

    def __call__(self):
        setup()
