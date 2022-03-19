
# PASSWORD GENERATOR

import random as R

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$%&*'

def generate_pass_one(characters):
    print("\nPlease Note that password length must be greater than or equal to 8\n")
    # len_of_pass = int(input("Enter the length of the password. "))   
    i = 0
    while True:   
        len_of_pass = int(input("Enter the length of the password. "))   # if user want only one password then ask length of the password
        if len_of_pass >= 8:
            passw = R.choices(characters, k = len_of_pass)      # it choose the string of length given in k by using characters seperately.
            print("\nYour password is: ",end='')
            print(''.join(passw))                              # it join the characters of passw.
            break
        else:
            print("Please enter the length of password greater than or equal to 8 ")
        i+=1
        
def generate_pass_many(characters):
    No_of_passw = int(input("How many password you want to generate? "))    
    print("\nPlease Note that password length must be greater than or equal to 8\n")   
    # len_of_pass = int(input("Enter the length of the password. "))   
    i = 0
    while True:
        len_of_pass = int(input("Enter the length of the password. "))   
        if len_of_pass >=8:
            for i in range(1,No_of_passw+1):
                passw = R.choices(characters,k = len_of_pass)
                print(f"\nYour {i} password is:",end='')
                print(''.join(passw))
            break
        else:
            print("Please enter the length of password greater than or equal to 8 ")
        i+=1

user_input = input("Do you want to generate more than one password? ").lower()

if user_input == 'yes':
    generate_pass_many(characters)
    
elif user_input == 'no':
    generate_pass_one(characters)
    
else:
    print("Invalid input")
 
