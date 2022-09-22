def valid_input(func):
    func = func.isdigit()
    if func == True:
        if func > 0 and func <= 5:
            return True
        else:
            print('Введите правильно значения для выбора в меню')
    else:
        print('Вы ввели не цифру')

