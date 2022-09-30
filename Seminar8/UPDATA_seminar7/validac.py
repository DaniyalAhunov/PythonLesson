def valid_input(func, max_Number):
    func = func.isdigit()
    if func == True:
        if func > 0 and func <= max_Number:
            return True
        else:
            print('Введите правильно значения для выбора в меню')
    else:
        print('Вы ввели не цифру')
