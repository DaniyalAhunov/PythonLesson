# 2.Создайте программу для игры с конфетами человек против человека.
# Условие задачи: 
# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
import random
def max_ledenec(x: int ,led: int):
    if x > 28:
        x = int(input(f'{x} слишком много \nВы можете взять максимум 28 конфет \nОсталось {led}\nУкажите количесвто которое вы возьмете '))
        if x > 28:
            max_ledenec(x, led)
        else:
            return x
    elif x > led:
        x = int(input(f'{x} слишком много \nВы можете взять максимум {led} \nУкажите количесвто которое вы возьмете '))
        if x > led:
            max_ledenec(x,led)
        else:
            return x
    else:
        return x
def bot(ledenec: int):
    if ledenec <= 57 and ledenec > 29:
        x = ledenec -  29
        return x
    elif ledenec < 29:
        x = ledenec
        return x
    else:
        x = random.randint(1,29)
        return x

def two_player(ledenec: int, player_1: str, player_2: str, xod: bool):

    while ledenec > 0:
        if xod == True:
            x2 = int(input(f'Ход {player_1}\nВы можете взять максимум 28 концет \nОсталось {ledenec}\nУкажите количесвто которое вы возьмете '))
            x1 = max_ledenec(x2,ledenec)
            ledenec -= int(x1)
            xod = False
        else:
            x2 = int(input(f'Ход {player_2}\nВы можете взять максимум 28 концет \nОсталось {ledenec}\nУкажите количесвто которое вы возьмете '))
            x1 = max_ledenec(x2,ledenec)
            ledenec -= int(x1)
            xod = True
    return xod
def final_geme(itog: bool, player_1: str, player_2: str):
    if itog == True:
        print(f'{player_1} выиграл и получил все конфеты ')
    else:
        print(f'{player_2} выиграл и получил все конфеты ')
def one_Player(ledenec: int, player_1: str, xod: bool):
    while ledenec > 0:
        if xod == True:
            x2 = int(input(f'Ход {player_1}\nВы можете взять максимум 28 концет \nОсталось {ledenec}\nУкажите количесвто которое вы возьмете '))
            x1 = max_ledenec(x2,ledenec)
            ledenec -= int(x1)
            xod = False
        else:
            x2 = bot(ledenec)
            print(f'Бот взял {x2} \n')
            ledenec -= int(x2)
            xod = True
def regulator():
    print('''Правила игры:
На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. ''')        
def start_two():
    player_1 = input('Введите имя игрока 1: ')
    player_2 = input('Введите имя игрока 2: ')
    xod = bool(random.getrandbits(1))
    ledenec = 2021
    itog = two_player(ledenec, player_1, player_2, xod)
    final_geme(itog, player_1, player_2)
def start_one():
    player_1 = input('Введите своё имя: ')
    player_2 = 'БОТ'
    xod = bool(random.getrandbits(1))
    ledenec = 200
    itog = one_Player(ledenec, player_1, xod)
    final_geme(itog, player_1, player_2)
x = input('''Добро пожаловать в игру Ledenec 
Введите цифру:
1 - чтобы изучит правила
2 - игра на одного с ботом
3 - игра на двоих
''')

game = {
    '1': regulator,
    '2': start_one,
    '3': start_two
}
if int(x) <= 3:
    game[x]()
else:
    print('перезайдите в игру у нас нет такого значения которое выбрали вы')