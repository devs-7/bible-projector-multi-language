import os

packages = ['main', 'projetor']

for package in packages:
    current_path = os.path.abspath(os.getcwd())
    main_view_ui_path = os.path.join(current_path, 'ui', package, 'window.ui')
    main_view_py_path = os.path.join(current_path, 'ui', package, 'window.py')
    os.system(f"pyuic5 {main_view_ui_path} -o {main_view_py_path}")
