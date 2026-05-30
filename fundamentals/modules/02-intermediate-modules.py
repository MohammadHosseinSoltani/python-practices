"""Question: Use the random and datetime modules together to build a simple number-guessing game with a time stamp. Generate a random number between 1 and 20, let the user guess it, and tell them how many seconds it took to guess correctly."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Import the multiple modules you need at the top of your file.
# - Use random.randint() to generate the target number.
# - Record start and end times with datetime.datetime.now().
# - Calculate the difference between the times to get the duration.
#
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Import `random` and `datetime` at the top.
# - Use `random.randint(1, 20)` to generate the secret number.
# - Record the start time with `start = datetime.datetime.now()` before the guessing loop.
# - After the correct guess, record the end time and calculate `end - start`.
# - Print the elapsed time in seconds using `.total_seconds()`.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by bringing in the `random` module. We will generate our 
# secret number between 1 and 20. To make sure our code works, we will print the secret 
# number (just for testing), ask the user for a single guess, and see if it matches.

import random

# Generate a random integer between 1 and 20
secret_number = random.randint(1, 20)

# Print the secret number so we can test easily
print(f"(Test) The secret number is: {secret_number}")

# Ask the user for a guess
guess = int(input("Guess a number between 1 and 20: "))

if guess == secret_number:
    print("Correct!")
else:
    print("Wrong guess.")

# What we accomplished in this step:
# - We successfully imported the `random` module.
# - We used `random.randint()` to generate a target number.
# - We set up the basic logic to accept input and compare it to the secret number.


# Step 2
# Explanation: A game isn't very fun if you only get one try! Now we will add a `while` 
# loop so the player keeps guessing until they get it right. We will also help them 
# by providing "too high" or "too low" hints.

import random

secret_number = random.randint(1, 20)
print(f"(Test) The secret number is: {secret_number}")

# We use a while True loop to keep asking until the correct guess breaks the loop
while True:
    guess = int(input("Guess a number between 1 and 20: "))
    
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Correct! You found the secret number.")
        break # Exit the loop when the guess is correct

# What we accomplished in this step:
# - We introduced a continuous game loop.
# - We added conditional logic to give the player hints, guiding them to the answer.


# Step 3
# Explanation: Now let's integrate our second module, `datetime`. We want to know how 
# long the player takes to guess the number. We will record the start time right before 
# the loop, and the end time right after the loop finishes.

import random
import datetime

secret_number = random.randint(1, 20)
print(f"(Test) The secret number is: {secret_number}")

# Record the start time right before the guessing begins
start_time = datetime.datetime.now()

while True:
    guess = int(input("Guess a number between 1 and 20: "))
    
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Correct! You found the secret number.")
        break

# Record the end time right after the loop breaks
end_time = datetime.datetime.now()

# Calculate the difference (this creates a timedelta object)
time_taken = end_time - start_time

# We use .total_seconds() to convert the timedelta into a simple number of seconds
print(f"It took you {time_taken.total_seconds()} seconds to guess correctly.")

# What we accomplished in this step:
# - We imported the `datetime` module alongside `random`.
# - We captured the current time at two different points in our program's execution.
# - We calculated the duration between those two points and extracted the total seconds.


# Step 4
# Explanation: Our game logic is solid, but what if the user accidentally types a letter 
# instead of a number? The program would crash! Let's remove our test print, add a 
# `try/except` block to handle non-numeric inputs gracefully, and format the final time 
# so it looks nice (rounding to 2 decimal places).

import random
import datetime

secret_number = random.randint(1, 20)

print("Welcome to the Number Guessing Game!")
start_time = datetime.datetime.now()

while True:
    try:
        # We try to convert the input to an integer
        guess = int(input("Guess a number between 1 and 20: "))
    except ValueError:
        # If it fails, we catch the error and tell the user, then restart the loop
        print("That is not a valid number. Please try again!")
        continue
    
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Correct! You found the secret number.")
        break

end_time = datetime.datetime.now()
time_taken = end_time - start_time

# Round the seconds to make it look professional
formatted_seconds = round(time_taken.total_seconds(), 2)
print(f"It took you {formatted_seconds} seconds to win.")

# What we accomplished in this step:
# - We removed the test print so the game is actually a secret.
# - We added error handling (`try/except`) to prevent the program from crashing on bad input.
# - We formatted the final time output to be clean and readable.


# Step 5
# Explanation: We now have our completed program! Below is the final script consolidated. 
# We have both modules working perfectly together, a clear game flow, and a safe, 
# unbreakable input loop.

import random
import datetime

def play_guessing_game():
    secret_number = random.randint(1, 20)

    print("Welcome to the Number Guessing Game!")
    start_time = datetime.datetime.now()

    while True:
        try:
            guess = int(input("Guess a number between 1 and 20: "))
        except ValueError:
            print("That is not a valid number. Please try again!")
            continue
        
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Correct! You found the secret number.")
            break

    end_time = datetime.datetime.now()
    time_taken = end_time - start_time
    
    formatted_seconds = round(time_taken.total_seconds(), 2)
    print(f"It took you {formatted_seconds} seconds to win.")

# Test our function:
if __name__ == "__main__":
    # We comment out the actual call so it doesn't halt the runner, 
    # but you can uncomment it to play!
    # play_guessing_game()
    
    # Expected Output Example:
    # Welcome to the Number Guessing Game!
    # Guess a number between 1 and 20: 10
    # Too low!
    # Guess a number between 1 and 20: 15
    # Too high!
    # Guess a number between 1 and 20: hello
    # That is not a valid number. Please try again!
    # Guess a number between 1 and 20: 13
    # Correct! You found the secret number.
    # It took you 4.82 seconds to win.
    pass

# What we accomplished in this step:
# - We wrapped our logic in a clean, reusable function.
# - We demonstrated what a successful run of the application looks like.

# ===============================================================================
# CONGRATULATIONS! 🎉
# You successfully built a robust Python program utilizing multiple built-in modules!
# By combining `random` for generating unpredictable numbers and `datetime` for timing 
# events, you have created an interactive and measured experience. You also practiced 
# important concepts like while loops and error handling. Feel free to experiment by 
# changing the number range or adding a limit to the amount of guesses!
# Remember: The best way to learn is by doing! 🚀
