# # Реализуйте RLE алгоритм: реализуйте модуль 
# # сжатия и восстановления данных.

# # fffffffffffffffffffffffffgggggggHHHHHHHHHHfffffffffffffffEEEEeeeeeeeeeeeeebbbbbbbbbb

# data = 'aaasserrrrrtttttionsssss'
# for i in data:
#     while i*()

# Реализуйте RLE алгоритм: реализуйте модуль
# сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных
# текстовых файлах.
from itertools import count
import My_cls
My_cls.cls()

def open_file(file):  # функция чтения из файла
    with open(f'{file}', 'r') as text_in:
        str_in = text_in.readline()
        text_in.close()
    return str_in
def write_file(file, data):  # функция записи в файл
    with open(file, 'w') as text_out:
        text_out.write(data)
        text_out.close()

def archive_file(str_in):  # функция упаковки
    str_out = ''
    counter = 1
    temp = str_in[0]
    for i in range(1, len(str_in)):
        if str_in[i] == temp:
            counter += 1
        else:
            str_out += str(counter) + temp
            counter = 1
            temp = str_in[i]
    str_out += str(counter) + temp
    return str_out
def unarchive_file(str_in):  # функция распаковки
    str_out = ''
    counter = 0
    for i in range(0, len(str_in)):
        if not str_in[i].isalpha():
            counter = counter * 10 + int(str_in[i])
        else:
            temp = ''
            str_out = str_out + ''.join([temp + str_in[i]
                                        for x in range(counter)])
            counter = 0

    # str_out += str(counter) + temp
    return str_out

f_not_arc = 'not_arch.txt'  # имя файла с несжатыми данными
f_arc = 'archive.txt'  # имя файла со сжатыми данными
f_unarc = 'unarchive.txt'  # имя файла с восстановленными данными

# ___________________________________________
# Эта часть идет как программа чтения данных
# из файла, сжатия данных и записи их в файл
print('1. Считываем данные и сжимаем их')
str_in = open_file(f_not_arc)
print(str_in)
str_out = archive_file(str_in)
print(str_out)
write_file(f_arc,  str_out)
# -----------------------------------------------------

# _____________________________________________________
# Эта часть идет как программа чтения сжатых
# данных из файла, их восстановления и
# записи их в файл
print('\n\n2. Считываем сжатые данные и восстанавливаем их')
arch_txt = open_file(f_arc)
print(arch_txt)
unarc = unarchive_file(arch_txt)
write_file(f_unarc, str(unarc))
print(unarc, '\n\n')

# -----------------------------------------------------
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
