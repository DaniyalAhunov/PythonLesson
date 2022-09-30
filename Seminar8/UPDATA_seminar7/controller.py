import view
import Baza_D as db
import validac

def button_click():
    
    menu = view.menu()
    izi = validac.valid_input(menu, 5)
    if izi == True:
        if menu == "1":
            db.table_name()
            db.add_user()
        elif menu == "2":
            id_del = view.kontact_user('Введите ID: ')
            db.change(id_del)
        elif menu == "3":
            id_del = view.kontact_user('Введите ID: ')
            db.view_id(id_del)
            input_user = view.kontact_user('Эта строка будет удалена для подтверждения нажмите 1 или любой другой символ для отказа ')
            if input_user == "1":
                print('Ваша строка удалена безвозвртано')
                db.del_user(id_del)    
            else:
                button_click()      
        elif menu == "4":
            id_one = view.kontact_user('Введите ID: ')
            db.view_id(id_one)
        elif menu == "5":
            db.view_all()
    else:
         button_click()
