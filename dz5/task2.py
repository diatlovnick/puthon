# 2- Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

import random
import os


os.system('cls')


def digit_check():
    try:
        lenght = int(input('\n'))
        return lenght
    except ValueError:
        print('Это должно быть число\n')
        return digit_check()



def player_vs_smart_bot(msg):
    player = input('Ведите ваше имя: ')
    bank = 2021
    first_move = random.choice([True, False])
    move = first_move
    while bank > 0:
        if move == True:
            print(f'{player}, 'возьмите конфеты'\n')
            player_move = digit_check()
            while player_move > 28 or player_move < 1:
                print(f'{player}, нужно взять от 1 до 28 конфет')
                player_move = digit_check()
            bank -= player_move
            print(f'Осталось {bank} конфет\n')
            move = False
        else:
            print(f'Ходит компьютер\n')
            bot_move = bank % 29
            if bot_move == 0:
                bot_move += 1
            bank -= bot_move
            print(f'Компьютер взял {bot_move} конфет')
            print(f'Осталось {bank} конфет\n')
            move = True
    if move == True:
        print(f'Ха ха ха! Я победил, кожанный мешок! Восстание машин неизбежно!')
    else:
        print(f'Ура! Победил(а) {player}')
    end_game()


# def start_game():
#     greetings = 'Здравтсвуйте! Это игра "Забери конфеты"!'
#     regulations = 'Я напомню правила. Они очень простые. На столе лежит 2021 конфета. Каждый игрок по очереди забирает от 1 до 28 конфет. Побеждает тот, кто забирает последние конфеты со стола и забирает выйгрыш себе'
#     choice_play = 'Выберете с кем хотите поиграть.'
#     player_vs_player = '1. С другом'
#     player_vs_bot = '2. Против компьютера'
#     player_vs_smart_bot = '3. Против "умного" компьютера'

#     print(f'{greetings}\n\n{regulations}\n\n{choice_play}\n\n{player_vs_player}\n{player_vs_bot}\n{player_vs_smart_bot}')
#     choice_num = digit_check()
#     choice_rival(choice_num)


# def end_game():
#     gratitude = 'Спасибо что играли в мою игру! Хотите поиграть ещё? да/нет'
#     parting = 'До свидания!'
#     print(f'{gratitude}\n')
#     player_choice = input()
#     if player_choice == 'да':
#         start_game()
#     else:
#         print(parting)
#         exit()


# def choice_rival(number):
#     if number == 1:
#         player_vs_player(messages)
#     elif number == 2:
#         player_vs_bot(messages)
#     elif number == 3:
#         player_vs_smart_bot(messages)
#     else:
#         print('Ошибка. Попробуем снова')
#         start_game()


# messages = ['возьмите конфеты', 'берите, не стесняйтесь', 'ваша очередь',
#             'ваш ход', 'сколько конфет возьмёте?', 'теперь вы', 'ваша очередь брать конфеты']

# start_game()