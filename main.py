import random
import os

list1 = [1,2,3,4,5,6,7,8,9,10]
gameover = False
while gameover != True:
    os.system('cls')
    number1 = random.choice(list1)
    numberGuessed = False
    print("I'm thinking of a number between 1 and 10...")
    print("Can you guess it?")
    guesses = 1
    while numberGuessed != True:
        isNumber = False
        while isNumber == False:
            guess1 = input("")
            if guess1 == "1":
                
                isNumber = True
            elif guess1 == "2":

                isNumber = True
            elif guess1 == "3":

                isNumber = True
            elif guess1 == "4":

                isNumber = True
            elif guess1 == "5":

                isNumber = True
            elif guess1 == "6":

                isNumber = True
            elif guess1 == "7":

                isNumber = True
            elif guess1 == "8":

                isNumber = True
            elif guess1 == "9":

                isNumber = True
            elif guess1 == "10":
                isNumber = True
            else:
                print("That's not a option...")
        guess = int(guess1)
        #testing only allowing for two options
        if guess == 1 or guess == 2 or guess == 3 or guess == 4 or guess == 5 or guess == 6 or guess == 7 or guess == 8 or guess == 9 or guess == 10:
            print("")
        else:
            print("")
        #end testing

        if guess > number1:
            print("Too high!")
            guesses = guesses + 1
        elif guess < number1:
            print("Too low!")
            guesses = guesses + 1
        else:
            print("You got it! It took you this number of tries:" , guesses)
            numberGuessed = True
            times_played = 0

            x = open("top_scores.txt", "r")
            times_played = x.read()
            print("You've played", times_played, "times.")
            z = int(times_played) + 1
            x.close()

            q = open("top_scores.txt", 'w+')
            times_played = q.write(str(z))
            q.close()

    print("Would you like to go again? (y)es or (n)o?")
    response_status = False
    while response_status == False:
        response = str(input())
        if response == "y":
            guesses = 1
            response_status = True
            gameover = False
            os.system('cls' if os.name == 'nt' else 'clear')
        elif response == "n":
            gameover = True
            response_status = True
        else:
            print("That's not an option.")
            response_status = False
















