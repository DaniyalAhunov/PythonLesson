import view
import function_s
import validac
def button_click():
    menu = view.menu()
    izi = validac.valid_input(menu)
    if izi == True:
        game ={
            '1': function_s.add,
            '2' : function_s.change,
            '3' : function_s.dell,
            '4' : function_s.view_id,
            '5' : function_s.view_all
        }
        game[menu]()
    else:
         button_click()

    

