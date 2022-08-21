
import json as j
import my_lib as ml


def delete_task():#не понимаю как реализовать замену, хочу находить задачу по id, выбирать что там менять, перезаписывать конкретныую задачу, перезаписывать файл
    path  = r'C:\Users\w01NB001\Documents\GeekBrains\python\dz8\todolist.json'
    id = ml.is_int('Введите ID задачи: ')
    with open (path, 'r', encoding='UTF-8') as file:
        to_do_list  = j.load(file)
        inf = 'нет такой задачи'
        for i in range(0,len(to_do_list)):
            if id == to_do_list[i]['ID']:
                try:
                    del to_do_list[i]
                    inf = print('Задача удалена!')
                    break
                except IndexError:
                    continue
        print(inf)       
        with open(path, 'w', encoding='UTF-8') as file:
            j.dump(to_do_list, file, indent = 2, ensure_ascii=False)
#delete_task()