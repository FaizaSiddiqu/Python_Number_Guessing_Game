# Number guessing game (logic building)
# 1- User will define alower and upper number range(1 to 50)
# 2- system select a ramdom number
# 3- user will guess the number
# 4- If the guess is high , system shoul prompt  the user for lower guess
# 5- If the guess is lower , system should prompt the user for higher guess
# 6- user onlu have 5 chances to select a number
# 7- If the user is correct , the user wins and the game ends

# import random

# print("--------Welcome to the Number Guessing Game! \n You have 5 attempts to guess the number between 1 to 50--------")
# number_to_guess = random.randrange(1, 50)            # generate a random range (number) betwwen 1 to 50
                                            
# chances = 5

# guess_counter = 0                  # initialize the guess counter

# while guess_counter < chances:                     # loop until the guess counter is less than the chances 
#     guess_counter += 1                            # increement the guess counter
#     my_guess = int(input("Enter your guess: "))

#     if my_guess == number_to_guess:
#         print(f"The number is {number_to_guess} and you found it right in {guess_counter} attempts")
#         break

#     elif guess_counter >= chances and my_guess != number_to_guess:
#         print(f"Oops Sorry! the number is {number_to_guess} better luck next time")

#     elif my_guess < number_to_guess:
#         print("Your guess is too low, try again!")

#     elif my_guess > number_to_guess:
#         print("Your guess is too high, try again!")





import streamlit as st
import random

# Set up the title and instructions
st.title("Number Guessing Game")
st.write("Welcome to the Number Guessing Game! You have 5 attempts to guess the number between 1 to 50.")

# Initialize session state variables if they don't exist
if 'number_to_guess' not in st.session_state:
    st.session_state['number_to_guess'] = random.randint(1, 50)
if 'guess_counter' not in st.session_state:
    st.session_state['guess_counter'] = 0
if 'game_over' not in st.session_state:
    st.session_state['game_over'] = False

# Function to reset the game
def reset_game():
    st.session_state['number_to_guess'] = random.randint(1, 50)
    st.session_state['guess_counter'] = 0
    st.session_state['game_over'] = False

# User input for guesses
user_guess = st.number_input("Enter your guess:", min_value=1, max_value=50, key="guess")

# Button to submit guess
if st.button('Submit Guess'):
    if st.session_state['game_over']:
        st.write("Game over! Please reset the game to play again.")
    else:
        st.session_state['guess_counter'] += 1
        if user_guess == st.session_state['number_to_guess']:
            st.success(f"Congratulations! You've guessed the number in {st.session_state['guess_counter']} attempts.")
            st.session_state['game_over'] = True
        elif st.session_state['guess_counter'] >= 5:
            st.error(f"Oops! The number was {st.session_state['number_to_guess']}. Better luck next time!")
            st.session_state['game_over'] = True
        elif user_guess < st.session_state['number_to_guess']:
            st.warning("Your guess is too low, try again!")
        else:
            st.warning("Your guess is too high, try again!")

# Button to reset the game
if st.button('Reset Game'):
    reset_game()
    st.experimental_rerun()

# Display the number of attempts left
if not st.session_state['game_over']:
    st.write(f"Attempts left: {5 - st.session_state['guess_counter']}")
