# Rock - Paper - Scissor GAME ( Implemented by List)

import random as r

items = ['scissors', 'paper', 'rock']
abbreavtion = [ 's', 'p', 'r']

print("\t\t\t\t\t\t\t\t\tWelcome to the Rock, Paper, Scissors Game")
N = int(input("How many rounds do you want to play?\n"))
print(f"\n Let's start match of {N} rounds\n")
print('''r. rock              p. paper              s. scissors''')

U = 0
C = 0

for i in range(N):
    comp_choice = r.choice(items)
    userChoice = input(("\nEnter 'r'  'p'  's' : ").lower())
    print(f"Computer's choice :{comp_choice}")
    if userChoice == abbreavtion[0]:
        if comp_choice == items[0]:
            print("Tie")
        elif comp_choice == items[1]:
            U += 1
            print("You Win")
        elif comp_choice == items[2]:
            C += 1
            print("Computer Win")
    elif userChoice == abbreavtion[2]:
        if comp_choice == items[2]:
            print("Tie")
        elif comp_choice == items[0]:
            U += 1
            print("You Win")
        elif comp_choice == items[1]:
            C += 1
            print("Computer Win")
    elif userChoice == abbreavtion[1]:
        if comp_choice == items[1]:
            print("Tie")
        elif comp_choice == items[0]:
            C += 1
            print("Computer Win")
        elif comp_choice == items[2]:
            U += 1
            print(" You Win")

print(f"\nYour Score :{U}")
print(f"Computer Score :{C}")
if U==C: 
    print("\nMatch Tie")
elif U>C:
    print(" \nHurahhh!!! You Won the match") 
else:
    print(" \nYou loose the match")