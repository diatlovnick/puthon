def start():
    print("""
                1 - Показать все задачи
                2 - Добавить задачу
                3 - Редактировать задачу
                4 - Удалить задачу 
                5 - ВЫХОД
    """)
    while True:
        choice = input('    Ваш выбор -> ')
        if choice in ('1','2','3','4','5'):
            return choice
        else:
            print('     Некорректный ввод, Попробуйте еще раз')

