import json as j
from re import I
import my_lib as ml
import work_with_information as w
    



def serch_change_task():#вместо изменения удаляет задачу
    path  = r'C:\Users\w01NB001\Documents\GeekBrains\python\dz8\todolist.json'
    id = ml.is_int('Введите ID задачи: ')
    with open (path, 'r', encoding='UTF-8') as file:
        to_do_list  = j.load(file)
        inf = 'нет такой задачи'
        for i in range(0,len(to_do_list)):
            if id == to_do_list[i]['ID']:
                try:
                    to_do_list[i]['Статус'] = w.status_choice()
                    inf = 'статус изменён'
                    break
                except IndexError:
                    continue
        print(inf)       
        with open(path, 'w', encoding='UTF-8') as file:
            j.dump(to_do_list[i], file, indent = 2, ensure_ascii=False)

serch_change_task()