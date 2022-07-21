# 2 - Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

lst = [2, 3, 4, 5, 6]

# def mult_pair_number(lst: list) -> list:
#     lst_mult = []
#     first_index = 0
#     last_index = len(lst) - 1
#     while last_index - first_index >= 0:
#         lst_mult.append(lst[first_index] * lst[last_index])
#         first_index += 1
#         last_index -= 1
#     return lst_mult
# result_lst = mult_pair_number(lst)
# print(result_lst)


def mult_pair_number(lst: list) -> list:
    lst_mult = []
    len_lst_mult = len(lst)//2 + 1
    for i in range(len_lst_mult):           
            lst_mult.append(lst[i] * lst[-1 - i])
    return lst_mult
res_lst = mult_pair_number(lst)
print(res_lst)