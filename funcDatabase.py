#12312312313123
import sqlite3
import telebot
from telebot import types

#1 Название переменных  variable_name_correct   variable_name_wrong
#2 IF    if_correct if_wrong
#3 FOR for_correct for_wrong
#4 WHILE while_correct while_wrong


conn = sqlite3.connect('database.db', check_same_thread=False) #check_same_thread=False
cursor = conn.cursor()



def update_db_user_topic(topic_name,student_id):

    sql_update = """Update students set {0} = {1} + 1 where student_id={2}""".format(topic_name,topic_name,student_id)
    cursor.execute(sql_update)
    conn.commit()


def get_db_user_topic(student_id,topic_name):
    sqlite_select_query = """SELECT {} from students WHERE student_id={}""".format(topic_name,student_id)
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    for i in records:
        value = i[0] #Нужно для того чтобы перевести лист в инт
        
    return value