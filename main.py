# pip install pyTelegramBotAPI
# Если будут траблы с импортом types из telebot то нужно просто переустановить pyTelegramBotAPI
import telebot
from telebot import types
import myfunc #program with for
import funcIF 
import funcWhile
import funcVariable
import funcDatabase
import statistics
import sqlite3
import random

conn = sqlite3.connect('database.db', check_same_thread=False)
cursor = conn.cursor()

#5366922060:AAE1JocwwMlLBcNf4Hxg6HuM5ci-x58KHlU

global user_id

bot = telebot.TeleBot("") # TOKEEEN HEEEEREEEE!!!!!!!!!!

user=''

a=''
Answer=''

Answer=Answer.lstrip(' ')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    global user_id
    user_id = message.from_user.id
    markup=types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1=types.KeyboardButton('Тема')
    item2=types.KeyboardButton('Статистика')


    markup.add(item1,item2)

    bot.send_message(message.chat.id,'Привет, {0.first_name}!'.format(message.from_user),reply_markup=markup)



    bot.send_message(message.from_user.id, '''Данный телеграм бот предназначен для обучения на python.
Для того чтобы зарегистрироваться введите команду  /reg''')

def db_table_student(student_id: int, student_name: str, student_surname: str):
	cursor.execute('INSERT INTO students (student_id, student_name, student_surname) VALUES (?, ?, ?)', (student_id, student_name, student_surname))
	conn.commit()
    
def db_table_teacher(teacher_id: int, teacher_name: str, teacher_surname: str):
	cursor.execute('INSERT INTO teachers (teacher_id, teacher_name, teacher_surname) VALUES (?, ?, ?)', (teacher_id, teacher_name, teacher_surname))
	conn.commit()

def db_table_classrooms(class_code: str, class_name: str, teacher_id: int):
	cursor.execute('INSERT INTO classrooms (class_code, class_name, teacher_id) VALUES (?, ?, ?)', (class_code, class_name, teacher_id))
	conn.commit()

@bot.message_handler(commands=['reg'])
def reg(message):

    bot.send_message(message.from_user.id, '''Для того чтобы зарегистрироваться ответьте на последующие вопросы:''')
    markup=types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1=types.KeyboardButton('Ученик')
    item2=types.KeyboardButton('Учитель')


    markup.add(item1,item2)

    bot.send_message(message.chat.id,'Вы ученик или учитель?'.format(message.from_user),reply_markup=markup)


def reg_name_student (message):
    global us_id
    global us_name
    us_id = message.from_user.id
    us_name = message.text
    bot.send_message(message.from_user.id,"Какая у вас фамилия?")
    bot.register_next_step_handler(message,reg_surname_student)
def reg_surname_student(message):
    global us_sname
    us_sname = message.text
    
    try: 

        t_id=message.from_user.id
        cursor.execute('''SELECT COUNT(*) FROM teachers WHERE teacher_id={0}'''.format(t_id))
        num=cursor.fetchall()
        list122=num[0]
        num=list122[0]
        if num==0:
            markup=types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1=types.KeyboardButton('Тема')
            item2=types.KeyboardButton('Статистика')
            markup.add(item1,item2)
            db_table_student(student_id=us_id, student_name=us_name, student_surname=us_sname)
            bot.send_message(message.chat.id,'Регистрация прошла успешно!'.format(message.from_user),reply_markup=markup)
        else:
            markup=types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1=types.KeyboardButton('Задания')
            item2=types.KeyboardButton('Меню учителя')
            markup.add(item1,item2)
            bot.send_message(message.chat.id,'Вы уже зарегистрированы как учитель!'.format(message.from_user),reply_markup=markup)
    except sqlite3.Error as error:
        markup=types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1=types.KeyboardButton('Тема')
        item2=types.KeyboardButton('Статистика')


        markup.add(item1,item2)

        bot.send_message(message.chat.id,'Вы уже зарегистрированы в системе!'.format(message.from_user),reply_markup=markup)



def reg_name_teacher (message):
    global t_id
    global t_name
    t_id = message.from_user.id
    t_name = message.text
    bot.send_message(message.from_user.id,"Какая у вас фамилия?")
    bot.register_next_step_handler(message,reg_surname_teacher)
def reg_surname_teacher(message):
    global t_sname
    t_sname = message.text
    
    try: 

        cursor.execute('''SELECT COUNT(*) FROM students WHERE student_id={0}'''.format(t_id))
        num1=cursor.fetchall()
        list122=num1[0]
        num1=list122[0]
        if num1==0:
            markup=types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1=types.KeyboardButton('Задания')
            item2=types.KeyboardButton('Меню учителя')
            markup.add(item1,item2)
            db_table_teacher(teacher_id=t_id, teacher_name=t_name, teacher_surname=t_sname)
            bot.send_message(message.chat.id,'Регистрация прошла успешно!'.format(message.from_user),reply_markup=markup)
        else:
            markup=types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1=types.KeyboardButton('Тема')
            item2=types.KeyboardButton('Статистика')
            markup.add(item1,item2)
            bot.send_message(message.chat.id,'Вы уже зарегистрированы как ученик!'.format(message.from_user),reply_markup=markup)
 

    except sqlite3.Error as error:
        markup=types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1=types.KeyboardButton('Задания')
        item2=types.KeyboardButton('Меню учителя')


        markup.add(item1,item2)

        bot.send_message(message.chat.id,'Вы уже зарегистрированы в системе!'.format(message.from_user),reply_markup=markup)

def reg_classroom(message):
    cl_name = message.text
    t_id = message.from_user.id
    cursor.execute('''SELECT COUNT(*) FROM classrooms WHERE class_name= \"{0}\" AND teacher_id={1}'''.format(cl_name,t_id))
    num_count1=cursor.fetchall()
    list12=num_count1[0]
    num_count1=list12[0]
    if num_count1!=0:
        bot.send_message(message.chat.id,"Вы уже регистрировали класс с таким названием!")
    else:
        try:
            while True:
                cl_code=''
                for x in range(6): 
                    cl_code = cl_code + random.choice(list('1234567890ABCDEFGHIGKLMNOPQRSTUVYXWZ'))
                cursor.execute('''SELECT COUNT(*) FROM classrooms WHERE class_code=\"{0}\"'''.format(cl_code))
                num_count=cursor.fetchall()
                list1=num_count[0]
                num_count=list1[0]
                if num_count ==0:
                    break
            
            
            
            db_table_classrooms(class_code=cl_code, class_name=cl_name, teacher_id=t_id)
            bot.send_message(message.chat.id,'Новый класс зарегистрирован!')
            bot.send_message(message.chat.id,'Код данного класса: {0}\nОтправьте данный код своим ученикам чтобы они присоединились в данный класс. \nДля того чтобы присоединится в класс ученики должны написать /joinclass'.format(cl_code))
        except:
            bot.send_message(message.chat.id,'Произошла ошибка при создании нового класса!')


@bot.message_handler(commands=['joinclass'])
def join_class_step1(message):
    bot.send_message(message.from_user.id, 'Пожалуйста введите код класса к которому вы хотите присоедениться')
    bot.register_next_step_handler(message,join_class_step2)

def join_class_step2(message):
    cl_code= message.text
    us_id=message.from_user.id

    cursor.execute("""UPDATE students SET class_code = \"{0}\" WHERE student_id={1}""".format(cl_code,us_id))
    conn.commit()
    bot.send_message(message.from_user.id, 'Поздравляю вы присоединилсь в класс!')
   
@bot.message_handler(content_types=['text'])
def bot_message(message):
  global Answer
  if message.text == 'Ученик':
    a = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, 'Как вас зовут?', reply_markup=a)

    bot.register_next_step_handler(message,reg_name_student)
  elif message.text == 'Учитель':
    a = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, 'Как вас зовут?', reply_markup=a)

    bot.register_next_step_handler(message,reg_name_teacher)
  
  elif message.text == 'Меню учителя':
    markup=types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1=types.KeyboardButton('Создать новый класс')
    item2=types.KeyboardButton('Мои классы')
    item3=types.KeyboardButton('Статистика класса')
    item4=types.KeyboardButton('Обратно')

    markup.add(item1,item2,item3,item4)

    bot.send_message(message.chat.id,'Меню учителя'.format(message.from_user),reply_markup=markup)
  
  elif message.text == 'Создать новый класс':
 
    bot.send_message(message.from_user.id, 'Введите название класса')
    bot.register_next_step_handler(message,reg_classroom)
  
  elif message.text == 'Мои классы':
    t_id = message.from_user.id
    cursor.execute(''' SELECT classrooms.class_name, classrooms.class_code FROM classrooms WHERE teacher_id={0} '''.format(t_id))
    data=cursor.fetchall()
    for record in data:
        a=record[0]
        b=record[1]
        bot.send_message(message.from_user.id, 'Название класса: {0} \nКод класса: {1}'.format(a,b))

  
  elif message.text=='For':


    bot.send_message(message.from_user.id, '''Вопрос: Что выведет программа?
Ответ в одну строку с пробелами.''')
    zadanie,Answer=myfunc.program_for()
    bot.send_message(message.from_user.id,zadanie)
    topic_name="for"
    bot.register_next_step_handler(message,proverka,Answer,topic_name)
  elif message.text=='Статистика':
    try:
        user_id=message.from_user.id
        variable_procent,if_procent,for_procent,while_procent=statistics.get_statistics(user_id)
        bot.send_message(message.from_user.id,'''Вывод процента правильных ответов.
    Название переменных: {0}
    if: {1}
    for: {2}
    while: {3}'''.format(variable_procent,if_procent,for_procent,while_procent))
    except:
        bot.send_message(message.from_user.id,'''Вы не зарегистрированы в системе!
Для того чтобы зарегистрироваться напишите  /reg''')

  elif message.text=='Статистика класса': 
    bot.send_message(message.from_user.id,"Статистика не выведится если в классе не будет учеников или у вас нету класса с введенным названием.")
    bot.send_message(message.from_user.id,"Введите пожалуйста название класса, чтобы узнать статистику учеников данного класса.")
    bot.register_next_step_handler(message,class_statistics)

  elif message.text=='If':


    bot.send_message(message.from_user.id, '''Вопрос: Что выведет программа?''')
    zadanie,Answer=funcIF.program_if()
    bot.send_message(message.from_user.id,zadanie)
    
    topic_name="if"
    
    bot.register_next_step_handler(message,proverka,Answer,topic_name)

  elif message.text=='While':
    bot.send_message(message.from_user.id, '''Вопрос: Что выведет программа?''')
    zadanie,Answer=funcWhile.program_while()
    bot.send_message(message.from_user.id,zadanie)
    
    topic_name="while"
    
    bot.register_next_step_handler(message,proverka,Answer,topic_name)

  elif message.text=='Названия переменных':
    
    markup=types.ReplyKeyboardMarkup(resize_keyboard = True)    

    item1=types.KeyboardButton('Правильно')
    item2=types.KeyboardButton('Неправильно')
    markup.add(item1,item2)
    bot.send_message(message.chat.id,'Названия переменных',reply_markup=markup)
    
    bot.send_message(message.from_user.id, '''Вопрос: Правильно ли составлено название переменной?''')
    zadanie,Answer=funcVariable.program_variable_name()

    bot.send_message(message.from_user.id,zadanie)


  elif message.text=='Правильно':
    markup=types.ReplyKeyboardMarkup(resize_keyboard = True)    

    item1=types.KeyboardButton('Названия переменных')
    item2=types.KeyboardButton('If')
    item3=types.KeyboardButton('For')
    item4=types.KeyboardButton('While')
    back=types.KeyboardButton('Назад')
    markup.add(item1,item2,item3,item4,back)

    user='Правильно'
    bot.send_message(message.chat.id,'Ваш ответ: Правильно',reply_markup=markup)

    if user==Answer:
        bot.send_message(message.from_user.id,'Вы ответили правильно!')
        topic_name="variable_name_correct"
    else:
        bot.send_message(message.from_user.id,"Вы ответили неправильно, правильный ответ:"+Answer)
        topic_name="variable_name_wrong"
    user_id= message.from_user.id
    funcDatabase.update_db_user_topic(topic_name,user_id)
  elif message.text=='Неправильно':
    markup=types.ReplyKeyboardMarkup(resize_keyboard = True)    

    item1=types.KeyboardButton('Названия переменных')
    item2=types.KeyboardButton('If')
    item3=types.KeyboardButton('For')
    item4=types.KeyboardButton('While')
    back=types.KeyboardButton('Назад')
    markup.add(item1,item2,item3,item4,back)


    user='Неправильно'
    bot.send_message(message.chat.id,'Ваш ответ: Неправильно',reply_markup=markup)

    if user==Answer:
        bot.send_message(message.from_user.id,'Вы ответили правильно!')
        topic_name="variable_name_correct"
    else:
        bot.send_message(message.from_user.id,"Вы ответили неправильно, правильный ответ:"+Answer)
        topic_name="variable_name_wrong"
        
    user_id= message.from_user.id
    funcDatabase.update_db_user_topic(topic_name,user_id)
  elif message.text=='Тема':
    markup=types.ReplyKeyboardMarkup(resize_keyboard = True)    

    item1=types.KeyboardButton('Названия переменных')
    item2=types.KeyboardButton('If')
    item3=types.KeyboardButton('For')
    item4=types.KeyboardButton('While')
    back=types.KeyboardButton('Назад')
    markup.add(item1,item2,item3,item4,back)
    bot.send_message(message.chat.id,'Тема',reply_markup=markup)



  elif message.text=='Задания':
    markup=types.ReplyKeyboardMarkup(resize_keyboard = True)    

    item1=types.KeyboardButton('Названия переменных')
    item2=types.KeyboardButton('If')
    item3=types.KeyboardButton('For')
    item4=types.KeyboardButton('While')
    back=types.KeyboardButton('Обратно')
    markup.add(item1,item2,item3,item4,back)
    bot.send_message(message.chat.id,'Задания',reply_markup=markup)

  elif message.text=='Назад':
    markup=types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1=types.KeyboardButton('Тема')
    item2=types.KeyboardButton('Статистика')
  
  
    markup.add(item1,item2)

    bot.send_message(message.chat.id,'Назад',reply_markup=markup)
    
  elif message.text=='Обратно':
        markup=types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1=types.KeyboardButton('Задания')
        item2=types.KeyboardButton('Меню учителя')
        markup.add(item1,item2)
        bot.send_message(message.chat.id,'Обратно'.format(message.from_user),reply_markup=markup)
        
def proverka(message,Answer,topic_name):
    Answer=Answer.lstrip(' ')
    user_id= message.from_user.id
    if message.text==Answer:
        bot.send_message(message.from_user.id,'Вы ответили правильно!')
        topic_name=topic_name+'_correct'
        funcDatabase.update_db_user_topic(topic_name,user_id)
    else:
        bot.send_message(message.from_user.id,"Вы ответили неправильно, правильный ответ:"+Answer)
        topic_name=topic_name+'_wrong'
        funcDatabase.update_db_user_topic(topic_name,user_id)

def class_statistics(message):
    cl_name=message.text
    t_id=message.from_user.id
    cursor.execute(''' SELECT class_code FROM classrooms WHERE class_name=\"{0}\" AND teacher_id={1} '''.format(cl_name,t_id))
    class_code_db= cursor.fetchall()

    for record in class_code_db:
        cl_code=record[0]

        
        cursor.execute(''' SELECT student_id,student_name,student_surname FROM students WHERE class_code =\"{0}\" '''.format(cl_code))
        id_of_classmates = cursor.fetchall()

        for record in id_of_classmates:
            id_of_student=record[0]
            stud_name=record[1]
            stud_surname=record[2]
            variable_procent,if_procent,for_procent,while_procent=statistics.get_statistics(id_of_student)
            bot.send_message(message.from_user.id,'''Вывод процента правильных ответов у ученика {0} {1}.
        Название переменных: {2}
        if: {3}
        for: {4}
        while: {5}'''.format(stud_name,stud_surname, variable_procent,if_procent,for_procent,while_procent))
    
    
bot.infinity_polling()












