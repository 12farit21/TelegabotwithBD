import random
def program_while():
  Answer=''
  
  break_continue_list=['continue','break'] 
  break_continue=str(random.choice(break_continue_list))
  
  condition_list=['<','!=','=='] # ['<','!=','==']
  condition_number=str(random.choice(condition_list))
  
  program=random.randint(1,2)
  # Если выпадет 1 то не будет break, continue
  # Если выпадет 2 то будут break и continue
  
  if program==1: 
    if condition_number=='<':
  
      a=random.randint(1,10)
      b=random.randint(a+2,a+10)
  
      
      zadanie='''a={0}
b={1}
while a<b:
  a=a+1
  print(a)'''.format(a,b)
  
      while a<b:
        a=a+1
        Answer=Answer+' '+str(a)
      
    if condition_number=='!=' or condition_number=='==' :
      a=random.randint(1,10)
      b=random.randint(a,a+4)
  
      full_condition='a'+' '+condition_number+' '+'b'
  
      zadanie='''a={0}
b={1}
while a {2} b:
  a=a+1
  print(a)
else:
  print(0)'''.format(a,b,condition_number)
  
      while eval(full_condition):
        a=a+1
        Answer=Answer+' '+str(a)
      else:
        Answer=Answer+' '+str(0)
  
  if program==2: 
    
    a=random.randint(1,10)
    b=random.randint(a+3,a+11)
    c=random.randint(a+2,b-1)
   
  
    zadanie='''a={0}
b={1}
c={2}
while a<b:
  a=a+1
  if a==c:
    {3}
  print(a)'''.format(a,b,c,break_continue)
  
    while a<b:
      a=a+1
      if a==c:
        if break_continue=='break':
          break
        if break_continue=='continue':
          continue
      Answer=Answer+' '+str(a)
      

  return zadanie,Answer
