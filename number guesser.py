import random


#game code
while True:

    print("\f\f-=:<({[Guess the Number]})>:=-")

    #ask for min number of random
    #repeat asking until it gets only number value.

    

    only_number = False
    while only_number == False:
        min_num = input("set the minimum number\t:")
        if min_num.isdigit():
            only_number = True
            min_num = int(min_num)
        else:
            print("ERROR: please enter ONLY number")

    #do the same thing above but for the max value
    only_number = False
    while only_number == False:
        max_num = input("set the maximum number: ")
        if not max_num.isdigit():
            print("ERROR: please enter ONLY number")
        elif int(max_num) <= min_num:
            print("ERROR: please enter a bigger value than minimum")
        else:
            only_number = True
            max_num = int(max_num)

    #game start
    print("")
    print("number range: " + str(min_num) + " ~ " + str(max_num))

    #set the random value between the input min,max value
    random_number = random.randint(min_num, max_num)

    #asks user to guess a random value
    #repeats until it gets an answer.
    #tells if the guess number is bigger or smaller than the answer number
    correct = False
    while correct == False:

        #check the input value only contain number
        only_number = False
        while only_number == False:
            guess = input("Guess a number I'm thinking: ")
            if not guess.isdigit():
                print("ERROR: please enter ONLY number")
            else:
                only_number = True
                guess = int(guess)

        #big/small hint
        if guess > random_number:
            print("smaller than " + str(guess))
        elif guess < random_number:
            print("bigger than " + str(guess))
        #ends loop because user guess correct number
        elif guess == random_number:
            correct = True

    #ending credit
    print("\fThe number was " + str(random_number))
    print("Congratulations! you win the game!")
    #user can do it again with entering "y"
    again = input("do it again? (y/n): ")
    if again != "y":
        break