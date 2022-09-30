import sqlite3
import view
def table_name():
    with sqlite3.connect('PythonGB/Seminar8/UPDATA_seminar7/kontakt_user.db') as db:
        sql_cur = db.cursor()
        sql_cur.execute('''CREATE TABLE IF NOT EXISTS kontact (
                                        id_user INTEGER PRIMARY KEY AUTOINCREMENT,
                                        fname VARCHAR,
                                        number BIGINT,
                                        other VARCHAR)''') 
        
    
def add_user():
    with sqlite3.connect('PythonGB/Seminar8/UPDATA_seminar7/kontakt_user.db') as db_conn:
        sql_cur = db_conn.cursor()
        f_name = view.kontact_user('Введите имя: ')
        num = view.kontact_user('Введите номер: ')
        others = view.kontact_user('Введите коментарий к контакту: ')
        values = [f_name, num, others]
        sql_cur.execute(f"INSERT INTO kontact VALUES (NULL, ?, ?, ?)",values)
        

def view_all():
    db_conn = sqlite3.connect('PythonGB/Seminar8/UPDATA_seminar7/kontakt_user.db')
    sql_cur = db_conn.cursor()
    for value in sql_cur.execute("SELECT * FROM kontact"):
        print(value)
    
def view_id(id):
    db_conn = sqlite3.connect('PythonGB/Seminar8/UPDATA_seminar7/kontakt_user.db')
    sql_cur = db_conn.cursor()
    for value in sql_cur.execute(f"SELECT * FROM kontact WHERE id_user = ?", [id]):
        print(value)

def del_user(id):
    with sqlite3.connect('PythonGB/Seminar8/UPDATA_seminar7/kontakt_user.db') as db_conn:
        sql_cur = db_conn.cursor()
        sql_cur.execute(f"DELETE FROM kontact WHERE id_user = ?", [id])
    
def change(id):
    with sqlite3.connect('PythonGB/Seminar8/UPDATA_seminar7/kontakt_user.db') as db_conn:
        sql_cur = db_conn.cursor()
        for value in sql_cur.execute(f"SELECT * FROM kontact WHERE id_user = ?", [id]):
            print(f'Строка которую хотите изменить:\n{value}')
        f_name = view.kontact_user('Введите новое имя: ')
        num = int(view.kontact_user('Введите новый номер: '))
        others = view.kontact_user('Введите коментарий к контакту: ')
        sql_cur.execute(f"""UPDATE kontact 
                        SET fname = ?,
                            number = ?,
                            other = ?
                        WHERE id_user = ?""", [f_name, num, others, id])