import random

def program_if():
  program=random.randint(1,2)
  # Если выпадет 1 то значения переменных a и b будет численными
  # Если выпадет 2 то значения переменных будет True или False
  
  condition_list=['<','>','==','!=']
  condition1=str(random.choice(condition_list))
  
  condition_list=['and','or']
  condition2=str(random.choice(condition_list))
  
  
  
  if program==1: 
    
    a=str(random.randint(-20,20))
    b=str(random.randint(-20,20))
    full_condition=str(a) + str(condition1)+str(b)
    if eval(full_condition):
      Answer= '1'
    else:
      Answer='0'
    zadanie='a={0}\nb={1}\nif a {2} b:\n  print(1)\nelse:\n  print(0)'.format(a,b,condition1)
  
  if program==2: 
    znachenie_list=['True','False']
    znachenie1=random.choice(znachenie_list)
    a=str(znachenie1)
    znachenie_list=['True','False']
    znachenie1=random.choice(znachenie_list)
    b=str(znachenie1)
    full_condition2=str(a) +' '+ str(condition2)+' '+str(b)
    if eval(full_condition2):
      Answer= '1'
    else:
      Answer='0'
  
    zadanie='a={0}\nb={1}\nif a {2} b:\n  print(1)\nelse:\n  print(0)'.format(a,b,condition2)
    
  return zadanie,Answer
