import csv
def add(): # изучаем cvs работу
    with open('kontakt.csv', 'w', new_line='')as csvfile:
        user = csv.writer(csvfile, delimiter=' ')
        user.writerow()
        user.writerow()

    print('Добавить')
def dell(): # изучаем удаление строки
    print('Удалить')
def change(): # изучаем изменение строки ID;ФИО;Номер_тел;Описание;
    print('Изменить')
def view_id():  # изучаем поиск в файле по id
    print('Просмотр по ID')
def view_all():  # изучаем отображение всего файла
     with open('output.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print( row['id'], row['fName'],row['lName'],row['number'],row['other'])
    # print('Просмотр всех контактов')

