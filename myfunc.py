import random
a=''
answer=''


def program_for():
  answer=''
  program=random.randint(1,3)
  if program==1: 

    x=random.randint(1,10)
    
    #zadanie (x)
    zadanie='for i in range({0}):\n  print(i)'.format(x)
    for i in range(x):
      answer=answer+' '+str(i)

  if program==2:
    x=random.randint(0,10)
    y=random.randint(x+1,x+15)
    #zadanie (xy)
    zadanie='''for i in range({0},{1}):
    print(i)'''.format(x,y)

      

    for i in range(x,y):
      answer=answer+' '+str(i)

      
  if program==3:
    while True:
      x=random.randint(-10,10)
      y=random.randint(-10,10)
      if x>y:
        z=random.randint(-3,-1)
        break
      elif x<y:
        z=random.randint(1,3)
        break
          
      #zadanie (xyz)
    zadanie='for i in range({0},{1},{2}):\n  print(i)'.format(x,y,z)
    
    for i in range(x,y,z):
      answer=answer+' '+str(i)

  return zadanie,answer