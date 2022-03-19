# Rock - Paper - Scissor GAME ( Implemented by DICTIONARY)

import random as R

game_items = {'r':'rock','p': 'paper','s': 'scissors'}
print("\nWelcome in Rock - Paper - Scissor Game")
N = int(input("\nHow many rounds you want to play? : "))

print('''r for rock
s for scissors
p for paper \n''')

U=0
C=0
l=[]
for i in game_items.values():
    l.append(i)

for i in range(N):
    k = R.choice(l)
    user_choice = game_items.get(input("\nEnter  'r'  'p'  's' : ").lower())
    print(f"Computer's choice :{k}")
    if user_choice == game_items.get('r'):
        if k == game_items.get('r'):
            print("\nTie ")
        elif k == game_items.get('s'):
            U+=1
            print("\nYou win")
        elif k == game_items.get('p'):
            C+=1
            print("\nComputer win")
    elif user_choice == game_items.get('p'):
        if k == game_items.get('p'):
            print("\nTie ")
        elif k == game_items.get('r'):
            U+=1
            print("\nYou win")
        elif k == game_items.get('s'):
            C+=1
            print("\nComputer win")
    if user_choice == game_items.get('s'):
        if k == game_items.get('s'):
            print("\nTie ")
        elif k == game_items.get('p'):
            U+=1
            print("\nYou win")
        elif k == game_items.get('r'):
            C+=1
            print("\nComputer win")

print(f"\nYour Score :{U}")
print(f"Computer Score :{C}")

if U>C:
    print("\nHuraaaah! YOU WON THE MATCH")
elif U == C:
    print("\nMATCH TIE")
else:
    print("\nOhhh YOU LOOSE THE MATCH")