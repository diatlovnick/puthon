#1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.


# lst = ['2','1e3', 'er3', '211']
# find_number = 34
# def find_nuber_in_list(lst_to_seek:list,number:int):
#     for char in lst_to_seek:
#         for symbol in char:
#             if symbol == str(number):
#                 return lst_to_seek.index(char)
#     return -1
# pos_number = find_nuber_in_list(lst,find_number)
# if pos_number != -1:
#     print(pos_number)
# else:
#     print('в списке нет искомого числа')

#2. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.



lst = ['21','1', 'er', '21']
find_number = 1
#count = 2#количество вхождений
def find_nuber_in_list(lst_to_seek:list,number:int,count:int = 2):
    for i in range(0,len(lst_to_seek)):   
        if lst_to_seek[i] == str(number):
            count = count-1
        if count == 0:
            return i
    return -1
pos_number = find_nuber_in_list(lst,find_number)
if pos_number != -1:
    print(pos_number)
else:
    print('в списке нет 2 вхождение')

# lst = ['2','1e3', 'er3', '211']
# find_number = 3
# def find_nuber_in_list(lst_to_seek:list,number:int):
#     lst_index = {}
#     j = 0
#     for char in lst_to_seek:
#         for symbol in char:
#             if symbol == str(number):
#                 lst_index[j] = lst_to_seek.index(char)
#                 j = j+1        
#     return list(lst_index.values())

# pos_number = find_nuber_in_list(lst,find_number)
# if len(pos_number) != 0:
#     print(pos_number)
# else:
#     print('в списке нет искомого числа')