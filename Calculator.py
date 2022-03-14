
# Calculator

def add (x,y):
    return x+y
    # # Add = 0
    # # while True:
    # #     num = int(input())
    # #     if user_input == '+' :
    # #         Add = Add + num
    #         return Add
    

def sub (x,y):
    return x-y

def mul (x,y):
    return x*y

def div (x,y):
    return x/y

def rem (x,y):
    return x%y

print("\nSELECT\n")
print("1.Addition")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Remainder")

while True:
    
    user_input = int(input("\nEnter Choice (1/2/3/4/5) : "))
    if user_input in [1,2,3,4,5] :
        num1 = int(input("\nEnter first number : "))
        num2 = int(input("Enter second number : "))
        if user_input == 1:
            print(f"{num1} + {num2} = {add(num1,num2)}\n")
        elif  user_input == 2:
            print(f"{num1} - {num2} = {sub(num1,num2)}\n")
        elif user_input == 3:
            print(f"{num1} X {num2} = {mul(num1,num2)}\n")
        elif user_input == 4:
            print(f"{num1} / {num2} = {div(num1,num2)}\n")
        elif user_input == 5:
            print(f"{num1} % {num2} = {rem(num1,num2)}\n")
            
    else:
        print("OOPS! invalid Choice")
        break
