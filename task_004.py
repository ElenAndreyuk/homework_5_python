# # Реализуйте RLE алгоритм: реализуйте модуль 
# # сжатия и восстановления данных.
data = 'aaasserrrrrtttttionsssss'

def archive(data):
    data_out = ''
    counter = 1
    temp = data[0]
    for i in range(1, len(data)):
        if data[i] == temp:
            counter +=1
        else:
            data_out += str(counter) + temp  
            counter = 1
            temp = data[i]  
    data_out += str(counter) + temp
    return data_out

def unarchive(data):
    data_out = ''
    counter = 0
    for i in range(0, len(data)):
        if not data[i].isalpha():
            counter = counter*10 + int(data[i])
        else:
            temp = ''
            data_out = data_out + ''.join([temp + data[i] for x in range(counter)])
            counter = 0
    return data_out

data_out = archive(data)
print(data_out)
data_2 = unarchive(data_out)
print(data_2)