import random as r

pool_of_complang = ['python','javascript','c','cpp','java','sql','html','css','r','swift','php','kotlin','perl','matlab','dart','powershell','rest','scala'] 

print("******** Wlecome word guessing game ******** \n")
print("This Game has pool of 18 computer languages in which you have to guess one!")
print("\nDo you want to play. Type YES or NO. \n")
user_choice = input("")

if user_choice.lower().strip() == 'yes' :
    user_name = input("\nEnter your name :")
    print(f'\n Welcome {user_name.upper()} in word guessing game.')
    print("\nYou have Five chances. ")
    random_word = r.choice(pool_of_complang)
    user_input = None
    
    for i in range(4,-1,-1):
        user_input = input("\nEnter the word of your choice :").lower().strip()
        
        if len(user_input) == len(random_word) :
            
            if user_input == random_word :
                print("Congratulations! You guess right. You Won the Game")
                break
            else:
                print("You guess word of same length, but the word is wrong. Choose another word.")
                print(f"You have {i} chances")

        elif len(user_input) > len(random_word):
            print("You guess word of greater length. Choose word of small length. ")
            print(f"You have {i} chances")
        elif len(user_input) < len(random_word):
            print("You guess word of small length. Choose word of greater length. ")
            print(f"You have {i} chances")
            
        if i==0:
            print("\nYour chances are finsih.\n You loose the game \n SORRY GAME OVER!")
else:
    print("Ok Bye")
