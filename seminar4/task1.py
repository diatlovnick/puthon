# 1. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

# 2. Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию. (не использовать sort и sorted)
# 3.Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.
# 4.Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.


from random import randint


def input_number_test_float(text):
    int_test = True
    is_minus = False
    while int_test:
        coord = input(f"{text}")
        if coord[0] == "-":
            is_minus = True
            coord = coord.replace("-","")
        if coord.isdigit():
            coord = int(coord)
            if is_minus:
                coord *= -1
            int_test = False
        else:
            print("вы ввели не число, введите число")
    return coord

n = int(input_number_test_float("введите число n: "))

def list_length_n(n:int = 0,lst: list = []):
    for i in range(-n,n):
        lst.append(randint(n*-1,n+1))
    print(lst)
    return lst
lst = list_length_n(n,)

with open('text.txt', mode = 'w') as file:
    for k in range(0,5):
        file.write(f"\n{randint(0, len(lst)-1)}")
    
with open('text.txt', mode = 'r') as file:
    res = 1
    lst_index = []
    for line in file.read():
        if line.isdigit():
           res *= lst[int(line)] 
           lst_index.append(line)
print(f"{lst_index=}")           
print(f"{lst=}")
print(res)

#with open('text.txt', mode = 'r') as file:


# Пояснения к первой задаче: нужны три функции.
# Первая - на ваш N дает список
# Вторая - из вашего списка записывает в файл любое количество индексов (иначе индексы в списке не соотносятся с списком) 
# Третья - считывает индексы с файла, находит их в списке, умножает их.

# При решении учтите, что N может быть равно 2, может 5, а может и 1000
