# #Изи TKINTER за 5 минут
# https://www.youtube.com/watch?v=t2w1L2MvOGY

# TK() - создает главное окно приложения (окон может быть несколько)
# Frame() - рамка или окно, дополнительно к главному
# LabelFrame()
# Label() - выводит текст в окне
# Button() - создает кнопку
# RadioButton() - создает радио-кнопку
# Entry() - поле ввода (типа input())
# Text() - поле для текста
# bind() - обработка событий
# pack(), grid(), place() - располагает виджеты в окне
# mainloop() - запускает цикл обработки событий

# импортируем tkinter
from tkinter import *

# создаем экземпляр класса Tk()
root = Tk()  # создадим экземпляр класса, по традиции называют root или window
# root.config(bg='black') # добавим цвет фона
root['bg'] = '#f1faf1'  # добавим цвет фона
root.wm_attributes('-alpha', 0.95)  # добавим прозрачность
root.title("Наименование")  # добавим название
root.geometry("600x400+700+500")  # ширина x высота + отступ от верхнего левого угла
root.resizable(width=False, height=False)  # запретить пользователю менять размер окна
# root.iconbitmap('icon.ico')  # добавить иконку

# создадим переменную для использования в обработчике событий и поместим в неё переменную TKinter
# переменные в TKinter -> StringVar(), IntVar(), BooleanVar()
value = StringVar()

# # 1 вариант: Создадим обработчик поля Entry с помощью button event
# def test(event):
#     get_var = value.get()  # value.get()  - позволяет получить переменную
#     lab["text"] = get_var
#
#
# lab = Label(text="Привет!")
# ent = Entry(textvariable=value)
# but = Button(text="OK")
# # b.bind()  - позволяет привязать событие
# but.bind('<Button-1>', test)  # <Button-1> - левая кнопка мыши, <Return> - нажатие Enter


# 2 вариант: Создадим обработчик с помощью атрибута command в методе Button()
def test():
    get_var = value.get()
    lab["text"] = get_var


lab = Label(text="Привет!")
ent = Entry(textvariable=value)
but = Button(command=test, text="OK")


# grid() - разбивает окно на невидимую сетку
# l.grid(row=1, column=1)
# e.grid(row=2, column=1)
# b.grid(row=3, column=1)

# grid.openimage()
# grid.forget()

# pack() - пакует элементы сверху вниз, по умолчанию отображает по центру
lab.pack(side=BOTTOM)
ent.pack()
but.pack()

root.mainloop()


# # Table view entries
# root = Tk()
#
# height = 5
# width = 5
# for i in range(height):  # Rows
#     for j in range(width):  # Columns
#         b = Entry(root, text="")
#         b.grid(row=i, column=j)
#
# mainloop()