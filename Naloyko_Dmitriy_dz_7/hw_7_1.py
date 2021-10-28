#Задание №1
import os

base_dir = 'my_project'
sub_dirs = ['settings', 'mainapp', 'adminapp', 'authapp']

def create_project(base, dirs):
    create_base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), base)
    if not os.path.exists(create_base_dir):
        os.mkdir(create_base_dir)
    else:
        print(f'{base_dir} уже существует.')
    for dir in dirs:
        create_sub_dirs = os.path.join(base, dir)
        if not os.path.exists(create_sub_dirs):
            os.mkdir(create_sub_dirs)
        else:
            print(f'{dir} уже существует')