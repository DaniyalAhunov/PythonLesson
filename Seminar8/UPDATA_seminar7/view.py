def kontact_user(text):
    return input(text)


def menu():
    print('''Меню:
    1 Добавить контакт
    2 Изменить контакт
    3 Удалить контакт
    4 Посмотреть один контакт
    5 посмотреть все контакты ''')
    user_input = input('Выберите действие: ')
    return user_input
