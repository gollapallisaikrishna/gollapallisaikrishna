def sum_of(a,b):
  if a>b or b<a:
    return sum(a,b)
  else:
    return 'There are no Numbers'
 

mylist = ['','O','','']
from random import shuffle 
shuffle(mylist)


def myfunc():
    shuffle(mylist)
    return mylist
    
def user_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input('Give a number from 0,1,2:')
    return int(guess)

def inter(mylist,guess):
    if mylist[guess] == 'O':
        print('correct')
        print(mylist)
    else:
        print('Wrong')
        print(mylist)
    
mylist = ['','O','']
result = myfunc()
key = guess()
inter(result,key)
