#Ask user for name
name = input("What is your name?")
#Ask user for age and years to add
current_age = int(input("How old are you now? "))
years_to_add = int(input("How many years would you like to add? "))
#Calculate the total of age plus years to add
current_age += years_to_add
#Print out the total
print("Hi {}! You will be {} in {} years." .format(name,current_age,years_to_add))