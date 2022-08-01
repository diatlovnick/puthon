#1- Определить, присутствует ли в заданном списке строк, некоторое число

lst = ['sdd', 's1', '22.']
search_number = 1
def is_num(lst, search_number):
    return list(filter(lambda element: str(search_number) in element, lst))
res = is_num(lst,search_number)
print(res)