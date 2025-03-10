# Number guessing game (logic building)
# 1- User will define alower and upper number range(1 to 50)
# 2- system select a ramdom number
# 3- user will guess the number
# 4- If the guess is high , system shoul prompt  the user for lower guess
# 5- If the guess is lower , system should prompt the user for higher guess
# 6- user onlu have 5 chances to select a number
# 7- If the user is correct , the user wins and the game ends



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

# Display the number of attempts left
if not st.session_state['game_over']:
    st.write(f"Attempts left: {5 - st.session_state['guess_counter']}")


