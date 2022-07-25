#3- Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#Пример: при N = 12 -> [2, 3]

n = 100
def simpl_def(number: int) -> list:
    lst_simple_def = []
    number_dif = number
    for i in range(2,number+1):
        for j in range(2,number+1):
            if number_dif % j == 0:
                lst_simple_def.append(j)
                number_dif = number_dif / j
                break
    return lst_simple_def
res_lst = simpl_def(n)
print(res_lst)
