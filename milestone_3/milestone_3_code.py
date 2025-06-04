#Ask for the user's name and introduce the quiz
name = input("What is your name?")
print("Welcome to Pop Quiz {}!".format(name))
print("This is a 15-question quiz about movies, logos, and artists that you might know.")
#Start the quiz
start = input("Are you ready to start the quiz? (yes/no)")
start.lower
if start == "yes":
    print("Let's start.")
    #You could begin the quiz here
    score = 0
    #Question 1
    print("Catergory: Movies")
    breakpoint
    answer1 = input("Which pixar movie is about emotions inside a young girl's mind?")
    answer1.lower
    if answer1 == "inside out":
        print("Correct!")
        score =+ 1
    elif answer1 == "":
        print("Hello? Are you there?")
    else:
        print("The answer is Inside Out")
    breakpoint
    #Question 2
    answer2 = input("What 2021 sci-fi film features Zendaya and Timothee Chalamet?")
    answer2.lower
    if answer2 == "dune":
        print("Correct!")
        score =+ 1
    elif answer2 == "":
        print("Hello? Are you there?")
    else:
        print("The answer is Dune")
    breakpoint
    print("Category: Logo")
    #Question 3
    answer3 = input("What media and entertainment company includes a castle in their logo?")
    answer3.lower
    if answer3 == "walt disney" or answer3 == "disney":
        print("Correct!")
        score =+ 1
    elif answer3 == "":
        print("Hello? Are you there?")
    else:
        print("The answer is Walt Disney or Disney")

#Ask the user if they would like to exit the quiz  
if start == "no":
    exit = input("Would you like to exit the game?")
    exit.lower
    if exit == "yes":
        print("All good! Maybe next time.")

        
