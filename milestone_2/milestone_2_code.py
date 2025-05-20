import re
#Ask user for a password
password = input("Enter a password:")
#Counting and grouping the variables
x = len(password)
#Compare and print
if len(password) < 10:
    print("Password must have atleast 10 characters.")
if not re.search (r"[a-z]", password):
    print("Password must have atleast 1 lowercase letter.")
if not re.search (r"[A-Z]", password):
    print("Password must have aleast 1 uppercase letter.")
if not re.search (r"[\d]", password):
    print("password must have atleast 1 number.")
if re.search(r"[!#$%^&*?]", password):
    print("Password must only contain any of these special characters: @ . _")
elif len(password) >= 10 and (r"[a-z]") and (r"[A-Z]") and (r"[\d]") and (r"[@ . _]"):
    print("Password is strong.")
else:
    print("Password: \"{}\" is weak." .format(password))
