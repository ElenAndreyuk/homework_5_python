# Создайте программу для игры в ""Крестики-нолики"".


plus_null = [ ['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
print_array(plus_null)
def print_array(list1):
    for i in plus_null:
        for j in i:
            print(j, end = ' ')
        print()

def make_a_move(array, sign = 'X' ):
    x = int(input('введите номер столбца вашего хода: '))
    y = int(input('введите номер строки вашего хода: '))
    if plus_null[x-1][y-1] == '*':
        plus_null[x-1][y-1] = sign
    else:
        print('попробуйте снова')
        make_a_move(plus_null)    

    print_array(plus_null)
def check_win(array, x, y):
    for i in f  array[x][y] != '*' and    
make_a_move(plus_null)
