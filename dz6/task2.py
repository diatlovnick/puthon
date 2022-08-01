#2- Найти сумму чисел списка стоящих на нечетной позиции

lst = [2, 3, 5, 9, 3]
sort_lst = list(filter(lambda i: lst.index(i)%2 !=0, lst))#не понимаю почему он добавляет в список чётные позиции после "9"
print(sort_lst)
res = sum(sort_lst)
print(res)