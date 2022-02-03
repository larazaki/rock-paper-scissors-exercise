


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#


#WELCOME MESSAGE

print("Welcome 'Player One' to my Rock-Paper-Scissors game...")

# ASK FOR USER INPUT

user_choice = input("Please choose one of: 'rock', 'paper', scissors':")

print("You chose:", user_choice)


#VALIDATIONS

validChoice = user_choice.lower()

if validChoice != ("rock" or "paper" or "scissors"):
    print("The choice you entered wasn't valid, sorry!")
    quit()

#COMPUTER CHOICE

import random

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)

print("The computer chose:", computer_choice)


#DETERMINE THE WINNER





#FINAL RESULTS



