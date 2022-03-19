# random number generation
import random as rd
k=rd.randint(1,100)
# print(k)
U=None
i=0
while(U!=k):
    U=int(input("Enter your guess :"))
    i+=1
    if U==k:
        print("Your guessed it corrrect!")
    else:
        if(U>k):
            print("Your guess is wrong! Enter a smaller number. \n")
        else:
            print(f"You guess is wrong! Enter a larger number. ")

print(f'You gussed the number in {i} guesses. ')

with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if(i<hiscore):
    print("You have just broken the high score!")
    with open("hiscore.txt", "w") as f:
        f.write(str(i))
        
