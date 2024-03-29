
from datetime import datetime as dt
from time import time
import json as j
import my_lib as ml


def status_choice():
    st = ('Не сделано', 'В работе', 'Сделано')
    print("""Статус:    Выберите варриант:
                        1 - Не сделано
                        2 - В работе
                        3 - Сделано """)
    while True:
        choice = ml.is_int('    Ваш выбор -> ')
        if choice in (1,2,3):
            return st[choice-1]
        else:
            print('     Некорректный ввод, Попробуйте еще раз')

def priority():
    prior = ('Срочно', 'Терпит', 'Без срока')
    print("""Приоритет: Выберите вариант:
                        1 - Срочно
                        2 - Терпит
                        3 - Без срока """)
    while True:
        choice = ml.is_int('    Ваш выбор -> ')
        if choice in (1,2,3):
            return prior[choice-1]
        else:
            print('     Некорректный ввод, Попробуйте еще раз')


def get_id():
    path  = r'C:\Users\w01NB001\Documents\GeekBrains\python\dz8\todolist.json'
    try:
        with open (path, 'r', encoding='UTF-8') as file:
            to_do_list  = j.load(file)
            for i in range(len(to_do_list)):
                id = int(to_do_list[i]['ID']) + 1
    except:
        id = 1
    return id





def enter_task():
    result = []
    keys = ['ID', 'Дата', 'Срок', 'Задача', 'Приоритет', 'Статус', 'Исполнитель']
    print('Ввод новой задачи:')
    values = ['' for n in keys]#список с длиной равной количеству элементов в списке keys
    for i in range(len(keys)):
        if keys[i] == 'ID':
            values[i] = get_id()
            continue
        if keys[i] == 'Дата':
            values[i] = dt.now().strftime('%D')
            continue
        if keys[i] == 'Приоритет':
            values[i] = priority()
            continue
        if keys[i] == 'Статус':
            values[i] = status_choice()
            continue
        values[i] = input(keys[i] + ': ')
    task = dict(zip(keys,values))#применяется функция зип к спискам keys и values, и из этого создаётся словарь
    result.append(task)#добавляем словарь таск в список резалт
    path  = r'C:\Users\w01NB001\Documents\GeekBrains\python\dz8\todolist.json'
    try:
        with open (path, 'r', encoding='UTF-8') as file:
            to_do_list  = j.load(file)
        to_do_list +=result
        with open(path, 'w', encoding='UTF-8') as file:
            j.dump(to_do_list, file, indent = 2, ensure_ascii=False)
    except:
        with open(path, 'w', encoding='UTF-8') as file:
            j.dump(result, file, indent = 2, ensure_ascii=False)
    return

#enter_task()



                

   
# def change():#не понимаю как реализовать замену, хочу находить задачу по id, выбирать что там менять, перезаписывать конкретныую задачу, перезаписывать файл
#     path  = r'C:\Users\w01NB001\Documents\GeekBrains\python\dz8\todolist.json'
#     id = int(input('введите ID задачи'))
#     with open (path, 'r', encoding='UTF-8') as file:
#         to_do_list  = j.load(file)
#         for i in range(0, len(to_do_list)):
#             if id == to_do_list[i]['ID']:
#                 change_list = []
#                 change_keys = input("введите названия раздела который хотите изменить(Дата, Срок, Задача, Приоритет, Статус, Исполнитель)")
#                 if  change_keys == 'Дата':
#                     print('введите новые данные')
#                     values = input(change_keys + ': ')
#                     continue
#                 task = dict(zip(change_keys,values))
#                 change_list.append(task)
#                 with open (path, 'r', encoding='UTF-8') as file:
#                   to_do_list  = j.load(file)
#                   to_do_list +=change_list
#                       with open(path, 'w', encoding='UTF-8') as file:
#                           j.dump(to_do_list, file, indent = 2, ensure_ascii=False)

    
    
   

    

# import json
# from datetime import datetime as dt
# from time import time

# def create_json():
#     json_data = []
#     with open('todolist.json', 'w') as file:
#         file.write(json.dumps(json_data, indent=2, ensure_ascii=False))

# def add_to_json():
#     name = input('введите название задачи')
#     to_do = input('опишите задачу')
#     plan_date_end = input('указите планируемую дату окончания')
#     lst_id = time = dt.now().strftime('%H%M%C')#хотел сделать уникальный id, но не понимаю как, думал ещё создать отдельно список, назначать из него 0 элемент, потом из списка удалять этот элемент
#     start_date = dt.now().strftime('%D')
#     json_data = {
#         "Name": name,
#         "To Do": to_do,
#         "Plan date end": plan_date_end,
#         "ID": lst_id,
#         "Start date": start_date
#     }
#     data = json.load(open('todolist.json'))
#     data.append(json_data)
#     with open('todolist.json', 'w') as file:
#         json.dump(data, file, indent=2)
#     print('\n Задача добавлена')

# def view_list():
#     with open('todolist.json', 'r', encoding='UTF-8') as file:
#         data = json.load(file)
#         for i in range(0,len(data)):
#             print(data[i])

# def change_date():
#     id = input('введите id задачи: ')
#     date = input('введите дату начала задачи')
#     with open('todolist.json', 'w') as file:
#         data = json.load(file)
#         for i in range(0, len(data)):
#             if id == data[i]['ID'] and date == data[i]['Start date']:
#                 data[i]["Plan date end"] = input('Поменяйте дату окончания ')
#             else:
#                 print('такой задачи нет')
#     with open('todolist.json', 'w') as file:
#         json.dump(data, file, indent=2,ensure_ascii=False)
#     print('\nДанные изменены')


# #create_json()
# add_to_json()
# view_list()
# #change_date()
# #view_list()