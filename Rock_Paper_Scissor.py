import random
y="You Win!!"
n="You Lose"
scoreComp=0
scoreYou=0
def game(Comp, You): # adding game logic to function
    if Comp==You:
        print("Its tie")
    elif Comp== 's':
        if You=='p':
            print(y)
        elif You== 'r':
            print(n)
        else:
            print("Click 's' for scissor ,'r' for rock and 'p' for paper")
    elif Comp== 'p':
        if You=='r':
            print(y)
        elif You== 's':
            print(n)
        else:
            print("Click 's' for scissor ,'r' for rock and 'p' for paper")
    elif Comp== 'r':
        if You=='p':
            print(y)
        elif You== 's':
            print(n)
        else:
            print("Click 's' for scissor ,'r' for rock and 'p' for paper")
        
print("Computer's turn ")
randNo= random.randint(1,3)
if randNo==1:
    Comp = 's'
elif randNo==2:
    Comp='p'
elif randNo==3:
    Comp='r'
else:
    print("Click 's' for scissor ,'r' for rock and 'p' for paper")

You = input("Your Turn: Click (s) for scissor ,(r) for rock and (p) for paper")
print(f"You Choice: {You}")
print(f"Computer Choice: {Comp}")
game(Comp, You) # function call
print("\n")

'''Output1:
Computer's turn 
Your Turn: Click (s) for scissor ,(r) for rock and (p) for paperp
You Win!!
You Choice: s
Computer Choice: p
Output2:
Computer's turn 
Your Turn: Click (s) for scissor ,(r) for rock and (p) for paperr
You are tie
You Choice: r
Computer Choice: r
output 3:
Computer's turn 
Your Turn: Click (s) for scissor ,(r) for rock and (p) for paperp
You are tie       
You Choice: p     
Computer Choice: p
'''