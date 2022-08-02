#3- Найти расстояние между двумя точками пространства(числа вводятся через пробел)


# from functools import reduce
# p1 = list(map(int, input('Введите координаты первой точки: ').split()))
# p2 = list(map(int, input('Введите координаты второй точки: ').split()))
# d = reduce(
#           lambda a, b: (a + b)**(1/2), 
#           (map(
#                 lambda p: (p[1] - p[0])**2, 
#                 zip(p1, p2))))
# print(d)


def not_work_func():# не получилось сделать проверку, можете написать как надо было сделать.
      f = True
      is_coord = True
      while f:
            lst = list(input('Введите координаты первой точки: ').split())
            for i in range(len(lst)):
                  number = is_int(lst[i])
                  if number == False and len != 2:
                        is_coord = False
            if is_coord == True:
                  f = False
            else:
                  print('координаты введены некоректно')
      return lst
      

def is_int(input_number:str):
      try:
            input_number = int(input_number)
            return input_number
      except ValueError:
            return False