#Правила именования переменных:
#1)имя переменной может состоять только из букв, цифр и знака подчёркивания;
#2)имя не может начинаться с цифры;
#3)имя не может содержать специальных символов @, $, %.
import random

def program_variable_name():
  symbols = []
  length = random.randint(1, 10)  # Длина названия переменной
  
  for i in range(33, 48):
      symbols.append(chr(i))
  for i in range(58, 65):
      symbols.append(chr(i))
  for i in range(91, 95):
      symbols.append(chr(i))
  symbols.append(chr(96))
  
  #['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '`']
  #Сохранил все символы в отдельный лист
  
  def getName(length):
      return "".join(chr(random.randint(33, 122)) for _ in range(length))
  
  #создал рандомное название для переменной
  
  name = getName(length)
  set_symbols = set(symbols.copy())
  set_name = set(name)
  set_intersection = set_name.intersection(set_symbols)#Проверка переменной name на наличии символов
  
  #Перевел в set чтобы можно было найти наличие символов в переменной name ( В названии переменной не должно быть символов )
  
  list_name = list(name)
  first_letter = list_name[0]
  
  
  if len(set_intersection) != 0:
    Answer= "Неправильно"
  else:
    if first_letter.isdigit() == True: #Условие на проверку ялвяется ли first_letter числом
      Answer= "Неправильно"
    else:
      Answer= "Правильно"
  
  
  zadanie=name
  return zadanie,Answer
