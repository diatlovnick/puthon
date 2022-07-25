# 2- Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Посмотрели, что такое множество? Вот здесь его не используйте



lst = [1, 2, 3, 1, 2, 4, 2]

not_rec_lst = []
def rec_lst(lst: list):
    for i in range(0,len(lst)):
        lst_count = lst.count(lst[i])
        if lst_count <= 1:
            not_rec_lst.append(lst[i])
    return not_rec_lst
not_rec_lst = rec_lst(lst)
print(not_rec_lst)



