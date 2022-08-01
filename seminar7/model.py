
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


x = complex(0,0)
y = complex(0,0) 



def init(a: str, b:str):
    global x
    global y
    x = complex(a)
    y = complex(b)

# init('3+2j','5+1j')

# print(x)
# print(y)


def sum():
    return x + y


def sub():
    return x - y

def mult():
    return x * y

def div():
    return x / y
