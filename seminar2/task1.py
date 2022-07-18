# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
#     *Пример:*
    
#     - Для N = 5: 1, -3, 9, -27, 81
# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
    
#     *Пример:*
    
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# 3. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.
# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа -
# определять количество вхождений одной строки в другой.

# string1 = input('Напиши что нибудь: ')
# string2 = input('Напиши что нибудь ещё разок: ')
# if len(string1) < len(string2):
#     string1, string2 = string2, string1

# count = 0

# for i in range(0, len(string1)-len(string2)):
#     if string2.lower() == string1[i:i+len(string2)].lower():
#         count += 1
#     print(string1[i:i+len(string2)])
# print(count)



# n = int(input('Введите число n = '))
# string = ''
# s = 1
# for i in list(range(n)):
#     string = string + str(s) + ' '
#     s *= -3
# print(string)

# задача 2
# в инете посмотрел вот такое решение
# n = int(input('Введите число n = '))
# slovar = {x: 3 * x + 1 for x in range(1, n+1)}
# print(slovar)



str1 = input('введите строку 1: ')
str2 = input('введите строку 2: ')

print(str1[1:])
print(str1[:5])

print(str[:5])






# n = (input('введите натурально число '))
# pos_test = True
# while pos_test:
    
#     while n := input('Enter number: ').isdigit() == False:
#         pass
#     if n > 0:
#         pos_test = 

# def input_coords(text):

#     int_test = True
#     is_minus = False
#     while int_test:
#         coord = input(f"{text}")
#         if coord[0] == "-":
#             is_minus = True
#             coord = coord.replace("-","")
#         if coord.isdigit():
#             coord = int(coord)
#             if is_minus:
#                 coord *= -1
#             int_test = False
#         else :
#             print("Not a number , try again")
#     return coord
