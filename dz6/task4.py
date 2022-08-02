# 4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1




lst = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
search_num = "й2цу"

def second_coming(lst:list, num:int):
    try:
        return [i for i, element in enumerate(lst) if num in element][1] if len(lst) >= 2 else 0
    except IndexError:
        return -1


res = second_coming(lst,search_num)
print(res)