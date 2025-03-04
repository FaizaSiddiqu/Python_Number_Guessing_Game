# Number guessing game (logic building)
# 1- User will define alower and upper number range(1 to 50)
# 2- system select a ramdom number
# 3- user will guess the number
# 4- If the guess is high , system shoul prompt  the user for lower guess
# 5- If the guess is lower , system should prompt the user for higher guess
# 6- user onlu have 5 chances to select a number
# 7- If the user is correct , the user wins and the game ends

import random

print("--------Welcome to the Number Guessing Game! \n You have 5 attempts to guess the number between 1 to 50--------")
number_to_guess = random.randrange(1, 50)            # generate a random range (number) betwwen 1 to 50
                                            
chances = 5

guess_counter = 0                  # initialize the guess counter

while guess_counter < chances:                     # loop until the guess counter is less than the chances 
    guess_counter += 1                            # increement the guess counter
    my_guess = int(input("Enter your guess: "))

    if my_guess == number_to_guess:
        print(f"The number is {number_to_guess} and you found it right in {guess_counter} attempts")
        break

    elif guess_counter >= chances and my_guess != number_to_guess:
        print(f"Oops Sorry! the number is {number_to_guess} better luck next time")

    elif my_guess < number_to_guess:
        print("Your guess is too low, try again!")

    elif my_guess > number_to_guess:
        print("Your guess is too high, try again!")




