# #1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

# while n := input('Enter number: ').isdigit() == False:
#     pass

# while n/10 > 0:
#     print(n%10)

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


number = str(input_number_test_float('введите вещественное число: '))
sum = 0
for i in number:
    if i.isdigit():
        sum = sum +int(i)

print(f"{number} = {sum}")