
#  Method 1( My Logic)

email = input("Enter your Email :").strip()   # Get the email as input from the user AND strip() Method removes white spaces in beginning and at the end of the email if any.
sym = '@'
if sym in email:
    k = email.split('@')                   # split() method split the email from @ into two parts first is a username and the other is a domain
    print(f'\nUsername : {k[0]} \nDomain : {k[1]}')
else:
    print("Invalid email")
# Mehod 2 (Already Defined Logic)             
                                            
# email = input("Enter Your Email: ").strip() 
# username = email[:email.index('@')]    -------> # It willl not print anything we have to add two print lines for Username and Domain
# domain = email[email.index('@') + 1:]       
                                            
# Mrehod 3  ( Modified logic of Method 2)

email = input("\nEnter Your Email: ").strip()
print(f"\nUsername : {email[:email.index('@')]}")
print(f"Domain : {email[email.index('@') + 1:]}\n")

# Another version of METHOD 3

email = input("\nEnter Your Email: ").strip()
print(f"\nUsername : {email[:email.index('@')]}\nDomain : {email[email.index('@') + 1:]}\n")
