import view
import function_s
import validac

def button_click():
    file_work = "PythonGB/Seminar7/DZ1/output.csv"
    menu = view.menu()
    izi = validac.valid_input(menu, 5)
    if izi == True:
        if menu == "1":
            user_kontact = view.add_user()
            function_s.add(user_kontact,file_work)
        elif menu == "2":
            id_user = view.kontact('Введите ID: ')
            function_s.change(id_user,file_work)
        elif menu == "3":
            id_user = view.kontact('Введите ID: ')
            izi = validac.valid_input(id_user, 2)
            if izi == True:
                function_s.view_id(id_user,file_work)
                input_user = view.kontact('Эта строка будет удалена для подтверждения нажмите 1 или любой другой символ для отказа')
                if input_user == "1":
                    print('Ваша строка удалена безвозвртано')
                    function_s.dell(id_user,file_work)
                else:
                    button_click()      
        elif menu == "4":
            function_s.view_id(view.kontact('Введите ID: '),file_work)
        elif menu == "5":
            function_s.view_all(file_work)
    else:
         button_click()


    

     