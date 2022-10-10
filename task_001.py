# Напишите программу, удаляющую из текста 
# все слова, содержащие ""абв"".
text = "Потому что, потому что Всех нужнее и дороже, Всех доверчивей и строже В этом мире абв В этом мире абв!"
text_list = text.split()
virus = "абв"   
for i in text_list:
    for j in range(len(i)):
        print(type(j))
        if i[j] == 'а' and i[j+1] == 'б' and i[j+2] == 'в':
            text_list.remove(i)
print(text_list) 