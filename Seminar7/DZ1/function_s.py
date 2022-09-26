# match case
# json
import csv
import view

def add(lists,file_work): #  Добавление в файл
    
    with open(file_work, 'a', newline='') as csvfile:
        user = csv.writer(csvfile, delimiter=';')
        user.writerow(lists)

def dell(id_user,file_work): # удаление строки
    f=open(file_work).readlines()
    for i in [int(id_user)]:
        f.pop(i)
    with open(file_work,'w') as F:
        F.writelines(f)

def change(id_user,file_work): # изменение строки ID;Имя;Фамилия;Номер_тел;Описание;
    temp_list =[]
    with open(file_work, 'r') as file:
        reader = csv.reader(file, delimiter = ';')
        for row in reader:
            temp_list.append(row)
    for item in temp_list:
        if id_user in item:
            print(item)
            temp_list.remove(item)
            newLine = view.add_user()
            temp_list.append(newLine)
            print('Запись изменена')
            break
    with open(file_work, 'w') as file:
        writer = csv.writer(file, delimiter = ';')
        writer.writerows(temp_list)


def view_id(id_input,file_work):  # поиск в файле по id
    with open(file_work,'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter = ';')
        for row in reader:
            if row['id'] == id_input:
                print(row)

def view_all(file_work):  # отображение всего файла
    with open(file_work,'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter = ';')
        for row in reader:
            print(row)
    

