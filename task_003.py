# Создайте программу для игры в ""Крестики-нолики"".

def output_board(val): 
    print("\n") 
    print("\t     |     |") 
    print("\t  {}  |  {}  |  {}".format(val[0], val[1], val[2])) 
    print('\t_____|_____|_____') 
  
    print("\t     |     |") 
    print("\t  {}  |  {}  |  {}".format(val[3], val[4], val[5])) 
    print('\t_____|_____|_____') 
  
    print("\t     |     |") 
  
    print("\t  {}  |  {}  |  {}".format(val[6], val[7], val[8])) 
    print("\t     |     |") 
    print("\n") 

def take_input(step,symbol):
    val[step - 1] = symbol

def get_result():
    win = ""
    for i in victories:
        if val[i[0]] == "X" and val[i[1]] == "X" and val[i[2]] == "X":
            win = "X"
        if val[i[0]] == "O" and val[i[1]] == "O" and val[i[2]] == "O":
            win = "O"            
    return win

val = [1, 2, 3, 4, 5, 6, 7, 8, 9]
victories = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
game_over = False
player1 = True
while game_over == False:
    output_board(val)
    if player1 == True:
        symbol, step = "X", int(input("игрок 1, ваш ход: "))
    else:
        symbol, step = "O", int(input("игрок 2, ваш ход: "))
    take_input(step, symbol) 
    win = get_result() 
    if win == "":
        game_over = False
    else:
        game_over = True
    player1 = not(player1)        
   
output_board(val)
print("Победил", win)