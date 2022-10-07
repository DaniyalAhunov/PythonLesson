import sqlite3 
import telebot


bot = telebot.TeleBot("5606918702:AAEGIN_sOQBhdyYrtcNCerur-ihM3t9u5uk")


@bot.message_handler(commands= ['start'])
def start_command(message):
	bot.send_message(message.chat.id, f"""Добро пожаловать {message.from_user.first_name}!!!
    \nЯ бот для записи номер телефонов что бы проверить функции которые я умею делать введи /help""")

@bot.message_handler(commands = ['help'])
def help_command(message):
    bot.send_message(message.chat.id,f"""{message.from_user.first_name}, приветсвую тебя в разделе помощь\nМои функции: \n/help - справка \n/add - добавление контакта
\n/loopall -просмотр всех контактов \n/loopid - просмотр одного контакта по id\n/delluser - удалить контакт""")


@bot.message_handler(commands = ['loopall']) 
def loopall_command(message):
      with sqlite3.connect('PythonGB/Seminar10/my_bot/kontakt_user.db') as db_conn:
        sql_cur = db_conn.cursor()
        for value in sql_cur.execute("SELECT * FROM kontact"):
            srt = ''
            for i in value: 
                srt += str(i) + ' '
            bot.send_message(message.chat.id, srt)
            
@bot.message_handler(commands = ['add']) 
def add_command(message):
    if message.text == '/add': 
            bot.reply_to(message, 'Имя контакта: ') # как получить это значение
               
            @bot.message_handler(counter_types=['text'])
            def input_other(message):
                global others
                others = message.text
                with sqlite3.connect('PythonGB/Seminar10/my_bot/kontakt_user.db') as db_conn:
                    sql_cur = db_conn.cursor()
                    values = [f_name, num, others]
                    sql_cur.execute(f"INSERT INTO kontact VALUES (NULL, ?, ?, ?)",values)
                    bot.send_message(message.chat.id, f'Пользователь добавлен {values}')

            @bot.message_handler(counter_types=['text'])
            def input_num(message):
                global num
                num = message.text
                bot.reply_to(message, 'Введите коментарий: ')
                bot.register_next_step_handler(message, input_other)
               
            @bot.message_handler(counter_types=['text'])
            def input_name(message):
                global f_name
                f_name = message.text
                bot.reply_to(message, 'Номер: ')
                bot.register_next_step_handler(message, input_num)
            bot.register_next_step_handler(message, input_name)   


@bot.message_handler(commands = ['loopid'])
def loopid(message):
    if message.text == '/loopid': 
        bot.reply_to(message, 'Введите id: ') # как получить это значение
        @bot.message_handler(counter_types=['text'])
        def input_id(message):
            global user_id
            user_id = message.text
            with sqlite3.connect('PythonGB/Seminar10/my_bot/kontakt_user.db') as db_conn:
                sql_cur = db_conn.cursor() 
                for value in sql_cur.execute(f"SELECT * FROM kontact WHERE id_user = ?",[user_id]):
                    srt = ''
                    for i in value: 
                        srt += str(i) + ' '
                    bot.send_message(message.chat.id, srt)
        bot.register_next_step_handler(message, input_id)
    
@bot.message_handler(commands = ['delluser'])
def loopid(message):
    if message.text == '/delluser': 
        bot.reply_to(message, 'Введите id который хотите удалить: ')
        @bot.message_handler(counter_types=['text'])
        def input_id(message):
            global user_id
            user_id = message.text
            with sqlite3.connect('PythonGB/Seminar10/my_bot/kontakt_user.db') as db_conn:
                    sql_cur = db_conn.cursor()
                    sql_cur.execute(f"DELETE FROM kontact WHERE id_user = ?", [user_id])
                    bot.send_message(message.chat.id, 'Контакт удалён')
        bot.register_next_step_handler(message, input_id)


bot.polling()