import json as j
# не понимаю как найти конкретную задачу по id и дальше поменять конкретный параметр

    

#def serch():
#     id = input('введите id задачи: ')
#     path  = r'C:\Users\w01NB001\Documents\GeekBrains\python\dz8\todolist.json'
#     with open('todolist.json', 'w') as file:
#         data = j.load(file)
#         for i in range(0, len(data)):
#             if id == data[i]['ID']:
#                retutn# хочу находить нужную задачу и дальше передавать её в метод search_change(), а в методе менять нужный параметр задачи 
#             else:
#                 print('такой задачи нет')
def search_change():#попробовал написать метод, который изменяет выбранный параметр
    path  = r'C:\Users\w01NB001\Documents\GeekBrains\python\dz8\todolist.json'
    keys = ['Дата', 'Срок', 'Задача', 'Приоритет', 'Статус', 'Исполнитель']
    print("""Выберите что хотите поменять:
                        1 - Дата
                        2 - Срок
                        3 - Задача
                        4 - Приоритет
                        5 - Статус
                        6 - Исполнитель """)
    while True:
        choice = int(input('    Ваш выбор -> '))
        if choice in (1,2,3,4,5,6):
            change = input(keys[choice-1] + ': ')
            with open(path, 'w', encoding='UTF-8') as file:
                j.dump(change, file, indent=2, ensure_ascii=False)


        else:
            print('     Некорректный ввод, Попробуйте еще раз')