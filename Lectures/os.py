import shutil
import os

# os.chdir(path)
# os.cxhd


os.chdir('.')  # смена текущей директории

os.getcwd()  # 'C:\Users\79190\PycharmProjects\webproject'

os.path.basename('C:/Users/79190/PycharmProjects/webproject/main.py')  # 'main.py'

os.path.abspath('main.py')  # 'C:/Users/79190/PycharmProjects/webproject/main.py'


shutil.copyfile(src, dst)  # копирует содержимое (но не метаданные) файла src в файл dst.
shutil.copy(src, dst)  # копирует содержимое файла src в файл или папку dst.
shutil.rmtree(path)  # Удаляет текущую директорию и все поддиректории;
# path должен указывать на директорию, а не на символическую ссылку.