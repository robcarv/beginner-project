import random

def play ():

    print ('-------------rules------------------\n')
    print('     rock beat scissor\n     scissor beat paper \n     paper beat rock\n')
    print ('------------------------------------')
    print(' Choose one option ')
    user  =  input("  'r' For rock\n  'p' for paper\n  's' for scissors\n").lower()
    computer  = random.choice(['r','p','s'])

    # def is_win(user,computer):
    if (user == 'r' and computer =='s'):
        print(f"you won {user} beat {computer}")
    elif (user =='s' and computer =='p'):
        print(f"you won {user} beat {computer}")
    elif (user =='p' and computer =='r'):
        print(f"you won {user} beat {computer}")  
    elif user == computer:
        print (f"Tie {user} = {computer}")
    else:
        print(f"computer winnn \n {computer} beat {user} ")
    
print(play())