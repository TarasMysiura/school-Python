# from tkinter import *;
# my_window = Tk();
# my_window.title("Перше вікно")
# my_window.geometry("600x500")
# my_window.resizable(0,0)
# my_window['bg'] = "#e87917"
# my_window.mainloop();

# from tkinter import *
# n = int(input('Введіть кіькість деталей, які виготовляє робітник за день - '))
# k = int(input('Введіть кількість днів - '))
# s = n*k
# if s < 150:
#     print('Робітник не виготовляє норму')
#     My_window = Tk()
#     My_window.title('Маленьке вікно')
#     My_window.geometry('100x100')
#     My_window.resizable(0, 0)
#     My_window["bg"] = "#FF0000"
#     My_window.mainloop()
# else:
#     print('Робітник виготовляє норму')
#     My_window = Tk()
#     My_window.title('Маленьке вікно')
#     My_window.geometry('100x100')
#     My_window.resizable(0, 0)
#     My_window["bg"] = "#31B404"
#     My_window.mainloop()

from tkinter import *
s = int(input('Введіть початкову швидкість потяга  - '))
t = 1
while s < 300:
    s = s+5  # збільшуємо швидкість потяга на 5
    t = t+1
    print('За', t, 'годин потяг їхатиме зі швидкістю ', s)
print('Потяг досягнув швидкості 300 км за год протягом', t, 'годин')
if t < 50:
    My_window = Tk()
    My_window.title('Вікно')
    My_window.geometry('500x500')
    My_window.resizable(0, 0)
    My_window["bg"] = "#ff0000"
    My_window.mainloop()
else:
    My_window = Tk()
    My_window.title('Вікно')
    My_window.geometry('500x500')
    My_window.resizable(0, 0)
    My_window["bg"] = "#31B404"
    My_window.mainloop()
