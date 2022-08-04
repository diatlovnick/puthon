
# def input_number_test_float(text):
#     int_test = True
#     is_minus = False
#     while int_test:
#         coord = input(f"{text}")
#         if coord[0] == "-":
#             is_minus = True
#             coord = coord.replace("-","")
#         if coord.isdigit():
#             coord = int(coord)
#             if is_minus:
#                 coord *= -1
#             int_test = False
#         else:
#             print("вы ввели не число, введите число")
#     return coord


#x = complex(0,0)
#y = complex(0,0) 



def init(a:str, b:str): return complex(a), complex(b)



def sum(x:complex,y:complex):
    return x + y


def sub(x:complex,y:complex):
    return x - y

def mult(x:complex,y:complex):
    return x * y

def div(x:complex,y:complex):
    return x / y
