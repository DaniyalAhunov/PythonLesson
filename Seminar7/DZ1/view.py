
def menu():
    print('''Меню:
    1 Добавить контакт
    2 Изменить контакт
    3 Удалить контакт
    4 Посмотреть один контакт
    5 посмотреть все контакты ''')
    user_input = input('Выберите действие: ')
    return user_input

def kontact(text):
    return input(text)

def add_user():
    user_kontact = []
    id_add = kontact('id ')
    user_kontact.append(id_add)
    f_name = kontact('Имя: ')
    user_kontact.append(f_name)
    l_name = kontact('Фамилия: ')
    user_kontact.append(l_name)
    number_phone = kontact('Номер телефона: ')
    user_kontact.append(number_phone)
    other = kontact('Прочее(Особые отметки): ')
    user_kontact.append(other)
    return user_kontact