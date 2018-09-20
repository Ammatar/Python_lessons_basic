# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

# немного не успел доделать
import hw05_easy_func, os
curr_dir= os.getcwd()
curr_dir1= curr_dir
print('Вы сейчас находитесь в директории:', curr_dir)
def start_func(curr_dir):
    print('1) Перейти в папку, 2) Посмотреть сождержимое текущей папки, 3) Удалить папку, 4) Создать папку, 5) Вернуться в домашнюю директорию, 6) Выход')
    inputed = int(input(''))
    #print(inputed)
    if inputed == 1:
        print(hw05_easy_func.look_func(curr_dir))
        curr_dir = hw05_easy_func.change_dir(input())
        print(curr_dir)
        return curr_dir, start_func(curr_dir)
    elif inputed == 2:
        look = hw05_easy_func.look_func(curr_dir)
        #print(look)
        start_func(curr_dir)
    elif inputed == 3:
        print('Введите имя папки которую необходимо удалить')
        folder_name = input('')
        delete = hw05_easy_func.remove_folder_func(curr_dir, folder_name)
        start_func(curr_dir)
    elif inputed == 4:
        print('Введите имя папки которую необходимо создать')
        folder_name = input('')
        create = hw05_easy_func.create_folder_func(curr_dir, folder_name)
        start_func(curr_dir)
    elif inputed == 5:
        curr_dir = curr_dir1
        start_func(curr_dir)
    elif inputed == 6:
        pass
    else:
        print('Введено некорректное число')
        start_func(curr_dir)

start_func(curr_dir)
