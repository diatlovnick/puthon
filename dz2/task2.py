# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

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

number_n = input_number_test_float("введите число n: ")
list_of_numbers = [1]
for i in range(1,number_n):
    list_of_numbers.append(list_of_numbers[i-1]*(i+1))
print(list_of_numbers)