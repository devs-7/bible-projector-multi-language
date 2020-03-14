import os

current_path = os.path.abspath(os.getcwd())
main_view_ui_path = os.path.join(current_path, 'ui', 'main_view', 'view.ui')
main_view_py_path = os.path.join(current_path, 'ui', 'main_view', 'view.py')
os.system(f"pyuic5 {main_view_ui_path} -o {main_view_py_path}")
