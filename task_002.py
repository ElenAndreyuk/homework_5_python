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
def move(candies, player):
    play = int(input(f'сколько берет конфет {player%2 +1} игрок? '))
    if 0 < play < max_number+1:
        candies = candies - play
        if candies > 0:
            print(f'осталось {candies} конфет')
            player+=1
            return candies, player
        else: 
            print(f'выиграл игрок {player%2 +1}') 
            return candies, player
    else:
        return candies, player
       
player = 0    
while candies > 0:
    candies, player = move(candies, player)
        

