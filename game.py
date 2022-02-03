


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#


#WELCOME MESSAGE

print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

# ASK FOR USER INPUT

user_choice = input("Please choose one of: 'rock', 'paper', scissors':")

print("You chose:", user_choice)


#VALIDATIONS
#Change user input to lowercase in order to check input validity

validChoice = user_choice.lower()

if validChoice not in ["rock", "paper", "scissors"]:
    print("The choice you entered wasn't valid, sorry!")
    quit()

#COMPUTER CHOICE
#Randomly generate the computer's choice

import random

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)

print("The computer chose:", computer_choice)


#DETERMINE THE WINNER
#Rock trumps scissors, Paper trumps rock, Scissors trumps paper
#Same choice results in a tie

win = "tie"

if validChoice == computer_choice:
    print("It's a tie!")
elif validChoice == "rock":
    if computer_choice == "scissors":
        print("Rock crushes scissors! You win!")
        win = "win"
    else:
        print("Paper covers rock! You lose!")
        win = "loss"
elif validChoice == "paper":
    if computer_choice == "rock":
        print("Paper covers rock! You win!")
        win = "win"
    else:
        print("Scissors cut paper! You lose!")
        win = "loss"
else:
    if computer_choice == "paper":
        print("Scissors cut paper! You win!")
        win = "win"
    else:
        print("Rock crushes scissors! You lose!")
        win = "loss"




#FINAL RESULTS
#Show final results to user

print("-------------------")
if win == "tie":
    print("It was a tie!")
elif win == "win":
    print("You won. Congratulations!")
else:
    print("Oh, the computer won. It's ok!")
print("-------------------")
print("Thanks for playing. Please play again!")

