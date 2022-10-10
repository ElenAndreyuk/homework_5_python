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


# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать 
# все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
candies = 2021
max_number = 28
def move_1():
    player_1 = int(input('сколько берет конфет 1 игрок? '))
    if  0 < player_1 < max_number:
        candies = candies - player_1
        if candies > 0:
            print(f'осталось {candies} конфет')
        else: 
            print('выиграл игрок 1') 
    else:
        print(f'не больше {max_number}')
        # move_1(x)     
    
def move_2():
    player_2 = int(input('сколько берет конфет 2 игрок? '))
    if  0 < player_2 < max_number:
        candies = candies - player_2
        if candies > 0:
            print(f'осталось {candies} конфет')
        else:
            print('выиграл игрок 2')
        
    else:
        print(f'не больше {max_number}')
        # move_1(x)       

while candies > 0:
    move_1()
    print("++++++++++")   
    move_2()
    
    


