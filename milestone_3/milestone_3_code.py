#Ask for the user's name and introduce the quiz
while True:
    name = input("What is your name?")
    print("Welcome to Pop Quiz {}!".format(name))
    print("This is a 6-question quiz about movies, logos, and actors that you might know.")
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
        #Question 4
        answer4 = input("The logo of Dreamworks Animation has a crescent moon. True or False")
        answer4.lower
        if answer4 == "true":
            print("Correct!")
            score =+ 1
        if answer4 == "false":
            print("Incorrect!")
        elif answer4 == "":
            print("Hello? Are you there?")
        else:
            print("The answer is true.")
        breakpoint
        print("Category: Actors")
        #Question 5
        answer5 = input("Which actor played the role of Tony Stark/Iron Man in the Marvel Cinematic Universe?")
        answer5.lower
        if answer5 == "robert downey jr" or answer5 == "rdj" or answer5 == "robert downey jr.":
            print("Correct!")
            score =+ 1
        elif answer5 == "":
            print("Hello? Are you there?")
        else:
            print("The answer is Robert Downey Jr. or RDJ")
        #Question 6
        answer6 = input("What movie did Ryan Reynolds star in that is considered one of the highest-grossing superhero movies of all time?")
        answer6.lower
        if answer6 == "deadpool":
            print("Corret!")
        elif answer6 == (""):
            print("Hello? Are you there?")
        else:
            print("The answer is Deadpool.")
        breakpoint
        print("Thank you for playing the quiz.")
    #Ask the user if they would like to exit the quiz  
    if start == "no":
        exit = input("Would you like to exit the game?")
        exit.lower
        if exit == "yes":
            print("All good! Maybe next time.")
            break
        if exit == "no":
            print("Let's try that again.")


            
