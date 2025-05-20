import re

#Ask user for a password
password = input("Enter a password:")


#Counting and grouping the variables
x = len(password)
is_valid = True

#Check password length
if len(password) < 10:
    print("Password must have atleast 10 characters.")


#Check for lowercase
if not re.search (r"[a-z]", password):
    print("Password must have atleast 1 lowercase letter.")
    is_valid = False

#Check for uppercase
if not re.search (r"[A-Z]", password):
    print("Password must have aleast 1 uppercase letter.")
    is_valid = False

#Check for numbers
if not re.search (r"[\d]", password):
    print("password must have atleast 1 number.")
    is_valid = False

#Check for any invalid special character
if not re.search(r"[@ . _]", password):
    print("Password must only contain any of these special characters: @ . _")
    is_valid = False

#Final result if true
if is_valid:
    print("Password is strong.")

#Final result if false
else:
    print("Password: \"{}\" is weak." .format(password))