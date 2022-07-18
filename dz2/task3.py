# 3 - Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

# *Пример:*

# - Для n = 6: {1: 2.0, 2: 2.25, 3: 2.37037037037037, 4: 2.44140625, 5: 2.4883199999999994, 6: 2.5216263717421135}

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
dict_of_numbers = {}

for i in range(1,number_n + 1):
    dict_of_numbers[i] = (1+1/i)**i
print(dict_of_numbers)

sum = 0.0
for i in dict_of_numbers:
    sum += sum + float(dict_of_numbers[i])
print(sum)
