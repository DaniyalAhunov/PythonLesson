import sqlite3

def table_name():
    with sqlite3.connect('PythonGB/Seminar10/my_bot/kontakt_user.db') as db:
        sql_cur = db.cursor()
        sql_cur.execute('''CREATE TABLE IF NOT EXISTS kontact (
                                        id_user INTEGER PRIMARY KEY AUTOINCREMENT,
                                        fname VARCHAR,
                                        number BIGINT,
                                        other VARCHAR)''') 
        
    
def add_user(f_name,num,others):
    with sqlite3.connect('PythonGB/Seminar10/my_bot/kontakt_user.db') as db_conn:
        sql_cur = db_conn.cursor()
        values = [f_name, num, others]
        sql_cur.execute(f"INSERT INTO kontact VALUES (NULL, ?, ?, ?)",values)
        

def view_all():
    with sqlite3.connect('PythonGB/Seminar10/my_bot/kontakt_user.db') as db_conn:
        sql_cur = db_conn.cursor()
        for value in sql_cur.execute("SELECT * FROM kontact"):
            srt = ''
            for i in value: 
                srt += str(i) + ' '
            return srt

def view_id(id):
    with sqlite3.connect('PythonGB/Seminar10/my_bot/kontakt_user.db') as db_conn:
        sql_cur = db_conn.cursor()
        for value in sql_cur.execute(f"SELECT * FROM kontact WHERE id_user = ?", [id]):
            return(value)

def del_user(id):
    with sqlite3.connect('PythonGB/Seminar10/my_bot/kontakt_user.db') as db_conn:
        sql_cur = db_conn.cursor()
        sql_cur.execute(f"DELETE FROM kontact WHERE id_user = ?", [id])
    
def change(id):
    with sqlite3.connect('PythonGB/Seminar10/my_bot/kontakt_user.db') as db_conn:
        sql_cur = db_conn.cursor()
        for value in sql_cur.execute(f"SELECT * FROM kontact WHERE id_user = ?", [id]):
            print(f'Строка которую хотите изменить:\n{value}')
        f_name = ""
        num = ""
        others = ""
        sql_cur.execute(f"""UPDATE kontact 
                        SET fname = ?,
                            number = ?,
                            other = ?
                        WHERE id_user = ?""", [f_name, num, others, id])

