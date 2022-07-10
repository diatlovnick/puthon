#4-Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

quart= int(input('введите номер четверти: '))
lst = [1,2,3,4]
a = True
while a == True:
    if quart in lst:
        a = False
    else:
        quart= int(input('введите номер четверти от 1 до 4:'))

if quart == 1:
    print('x >= 0 y >= 0')
    
elif quart == 2:
    print('x <= 0 y >= 0')
elif quart == 3:
    print('x <= 0 y <= 0')
else:
    print('x >= 0 y <= 0')