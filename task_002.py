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
candies = 50
max_number = 11
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
    player_1 = int(input('сколько берет конфет 1 игрок? '))
    if  0 < player_1 < max_number:
        candies = candies - player_1
        if candies > 0:
            print(f'осталось {candies} конфет')
        else: 
            print('выиграл игрок 1') 
            break
    else:
        print(f'не больше {max_number}')
    print("++++++++++")   
    player_2 = int(input('сколько берет конфет 2 игрок? '))
    if  0 < player_2 < max_number:
        candies = candies - player_2
        if candies > 0:
            print(f'осталось {candies} конфет')
        else:
            print('выиграл игрок 2')
            break
        
    else:
        print(f'не больше {max_number}')
    
    


