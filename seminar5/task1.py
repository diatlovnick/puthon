
import random

def input_int(text: str):
    f = True
    while f:
        n = input(text)
        if n.isdigit():
            return int(n)
            f = False
        else:
            print('введите число')
n = input_int('n= ')
print(n)

list_1 = [random.randint(0,100) for i in range(n+1)]

list_2 = ["x" for i in range(n+1)]
list_3 = [i for i in range(0,n+1)]
#data = list(enumerate(list_2))
#data_2 = list(map(lambda x,y: x ** y, list_2,list_3))
data_3 = list(zip(list_1,list_2,list_3))

data_str= list(map(str, data_3))
data_fltr = list(filter(lambda a: a != " ", data_str))
print(data_fltr)



print(data_3)