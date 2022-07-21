# 3 - Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5.567, 10.003] => 0.564 или 564

lst_numbers = [1.1, 1.2, 3.1, 5.567, 10.003]

def lst_float_min_max(lst: list):
    max = lst[0] - int(lst[0])
    min = lst[0] - int(lst[0])
    
    for i in lst:
        number = i - int(i)
        if number > max:
            max = number
        if number < min:
            min = number
    res = max - min
    return res
result = lst_float_min_max(lst_numbers)
print(f"{result:.3f}")
