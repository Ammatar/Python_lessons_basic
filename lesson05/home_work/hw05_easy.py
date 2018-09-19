# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os, time, shutil
#print(os.getcwd())
number = 1
number_1 = 1
while number < 10:
    os.mkdir('./dir_'+str(number), mode=511, dir_fd=None)
    number += 1
time.sleep(10)
while number_1 <10:
    os.removedirs('./dir_'+str(number_1))
    number_1 += 1

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

print(list(os.listdir('./')))

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
shutil.copy(r'./lesson5.py', r'./lesson5_copy.py')
time.sleep(10)
os.remove(r'./lesson5_copy.py')
