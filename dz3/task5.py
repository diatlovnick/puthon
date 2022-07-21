# 5 - Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи](https://clck.ru/sH87m)

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

number = input_number_test_float("введите число: ")

def pos_fib(num: int) -> list:
    pos_num = [0,1]
    for i in range(1,num):
        pos_num.append(pos_num[-1] + pos_num[-2])
    return pos_num
def neg_fib(num: int) -> list:
    neg_num = [0,1]
    for i in range(1,num):
        neg_num.append(neg_num[-2] - neg_num[-1])
    return neg_num
print(neg_fib(number)[::-1] + pos_fib(number)[1:])
