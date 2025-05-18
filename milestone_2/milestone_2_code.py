#Ask user for a password
password = input("Type in a password:")
#Check the number of characters
x = len(password)
#Compare and print
if x >= 1 and x <= 5:
    print("{} is too short!" .format(password))
    print("Password needs to have atleast 10 characters.")
elif x > 5 and x <=10:
    print("{} is not strong enough." .format(password))
    print("Improve password by adding 3 more characters.")
elif x > 10 and x <= 15:
    print("{} is average.".format(password))
else:
    print("The password is invalid.")