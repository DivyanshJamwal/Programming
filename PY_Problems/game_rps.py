import random

def game(com, you):
    if com == you:
        return None
    elif com == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False
    elif com == 'p':
        if you == 's':
            return True
        elif you == 'r':
            return False
    elif com == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False

randNo = random.randint(1,3)
if randNo == 1:
    com = 'r'
elif randNo == 2:
    com = 'p'
elif randNo == 3:
    com = 's'

print("rock = r paper = p scissors = s")
you = input(f"Enter your choice : ")

print(f"Comp chose : {com}")
print(f"You chose : {you}")

a = game(com, you)

if a==True:
    print("You won!")
elif a==False:
    print("You Lose!")
elif a==None:
    print("Game is a tie!")


print("Thanks for playing this game!")

        

