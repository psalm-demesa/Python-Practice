#Ask for the user's name and introduce the quiz
name = input("What is your name?")
print("Welcome to Pop Quiz {}!".format(name))
print("This is a 15-question quiz about movies, music, and artists that you might know.")
#Start the quiz
start = input("Are you ready to start the quiz? (yes/no)")
start.lower
if start == "yes":
    print("Let's start.")
    #You could begin the quiz here
    score = 0
    #Questions
    print("Catergory: Movies")
    


#Ask the user if they would like to exit the quiz  
if start == "no":
    exit = input("Would you like to exit the game?")
    exit.lower
    if exit == "yes":
        print("All good! Maybe next time.")

        
