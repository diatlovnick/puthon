# #3- Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

#x=input('введите координату х=')
#y=input('введите координату y=')
a = True
while a == True:
    x=int(input('введите координату х='))
    y=int(input('введите координату y='))
    if x==0 and y==0:
        a = True
        print('введите координаты отличные от 0')
    else:
        a = False
if (x >= 0) and (y >= 0):
    quart = 1
elif (x >= 0) and (y <= 0):
    quart = 4
elif (x <= 0) and (y <= 0):
    quart = 3
else:
    quart = 2
print(quart)