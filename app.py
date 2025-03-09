

import streamlit as st
import random

# Initialize session state variables
if 'random_number' not in st.session_state:
    st.session_state.random_number = None
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'max_attempts' not in st.session_state:
    st.session_state.max_attempts = None
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# Title
st.title("🎯 Number Guessing Game")

# Custom range selection
st.subheader("Set the range for the random number:")
min_value = st.number_input("Minimum Value:", value=1, step=1)
max_value = st.number_input("Maximum Value:", value=100, step=1)

# Difficulty selection
difficulty = st.selectbox("Select Difficulty:", ["Unlimited Attempts", "Easy (10 attempts)", "Medium (5 attempts)", "Hard (3 attempts)"])

# Set max attempts based on difficulty
if difficulty == "Unlimited Attempts":
    st.session_state.max_attempts = None
elif difficulty == "Easy (10 attempts)":
    st.session_state.max_attempts = 10
elif difficulty == "Medium (5 attempts)":
    st.session_state.max_attempts = 5
elif difficulty == "Hard (3 attempts)":
    st.session_state.max_attempts = 3

# Function to start/restart the game
def start_game():
    st.session_state.random_number = random.randint(min_value, max_value)
    st.session_state.attempts = 0
    st.session_state.game_over = False

# Start game button
if st.button("Start New Game"):
    start_game()

# Guess input (only allow if game is running)
if not st.session_state.game_over and st.session_state.random_number is not None:
    guess = st.number_input("Enter your guess:", min_value=min_value, max_value=max_value, step=1)

    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        if guess < st.session_state.random_number:
            st.warning("Too low! Try again.")
        elif guess > st.session_state.random_number:
            st.warning("Too high! Try again.")
        else:
            st.success(f"🎉 Correct! You guessed the number in {st.session_state.attempts} attempts.")
            st.session_state.game_over = True

        # Check if max attempts reached
        if st.session_state.max_attempts and st.session_state.attempts >= st.session_state.max_attempts:
            st.error(f"Game Over! The number was {st.session_state.random_number}.")
            st.session_state.game_over = True

# Display attempt count
st.write(f"Attempts: {st.session_state.attempts}")

# Reset button
if st.button("Reset Game"):
    start_game()