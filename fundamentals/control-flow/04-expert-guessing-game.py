"""Question: Build a number-guessing game that generates a random number between 1 and 100. The player gets a limited number of attempts. After each guess, tell the player whether the guess is too high, too low, or correct. After the game ends (win or lose), ask if they want to play again. Use loops, conditionals, error handling, and the random module."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Import the `random` module and use `random.randint(1, 100)` to generate the secret number.
# - Use a `while` loop to keep track of the player's attempts.
# - Use an `if/elif/else` structure for comparing the user's guess to the secret number.
# - Use a `try/except` block to handle non-numeric input gracefully so the game doesn't crash.
#
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Use `import random` and `random.randint(1, 100)` to generate the secret number.
# - Use a `while` loop that runs while the player still has attempts left.
# - Inside the loop, ask for a guess, convert it with `int()`, and compare with the secret number.
# - If the guess is too high, print 'Too high!'; if too low, print 'Too low!'; if correct, print a congratulations message and break.
# - After the loop, ask 'Play again? (yes/no)' and restart the game if the answer is yes.
# - Handle non-numeric guesses with a `try/except` so the player doesn't lose an attempt for a typo.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by generating a random number and printing it out (just 
# for our own testing). We will then ask the player for a single guess, convert it 
# to an integer, compare it to the secret number, and print the result.

import random

print("--- Number Guessing Game ---")
secret_number = random.randint(1, 100)

# We print the secret number temporarily to make testing easier
print(f"(Testing) The secret number is {secret_number}")

guess_input = input("Guess a number between 1 and 100: ")
guess = int(guess_input)

if guess < secret_number:
    print("Too low!")
elif guess > secret_number:
    print("Too high!")
else:
    print("Correct! You win!")

# What we accomplished in this step:
# - We successfully imported the `random` module and generated a number.
# - We captured the user's input and performed a basic conditional comparison.


# Step 2
# Explanation: One guess isn't much of a game. Let's wrap our guessing logic in a 
# `while` loop to give the player a limited number of attempts (e.g., 7). We will 
# keep track of the attempts used and break out of the loop if they guess correctly. 
# We'll also add an end-game check to see if they ran out of attempts.

import random

print("--- Number Guessing Game ---")
secret_number = random.randint(1, 100)
print(f"(Testing) The secret number is {secret_number}")

attempts_allowed = 7
attempts_used = 0
won = False

while attempts_used < attempts_allowed:
    guess_input = input(f"\nAttempt {attempts_used + 1}/{attempts_allowed}. Guess a number (1-100): ")
    guess = int(guess_input)
    attempts_used += 1
    
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Correct! You win!")
        won = True
        break

if not won:
    print(f"\nGame Over! The secret number was {secret_number}.")

# What we accomplished in this step:
# - We introduced a `while` loop bounded by a maximum number of attempts.
# - We added a `won` flag to cleanly determine if the player won or lost after the loop ends.


# Step 3
# Explanation: What happens if the player accidentally types "five" instead of "5"? 
# Our `int()` conversion will crash the game. Let's add a `try/except` block. If 
# they enter bad input, we will print an error message and use `continue` to restart 
# the loop. Crucially, we won't increment `attempts_used`, so they don't lose a turn!

import random

print("--- Number Guessing Game ---")
secret_number = random.randint(1, 100)
print(f"(Testing) The secret number is {secret_number}")

attempts_allowed = 7
attempts_used = 0
won = False

while attempts_used < attempts_allowed:
    guess_input = input(f"\nAttempt {attempts_used + 1}/{attempts_allowed}. Guess a number (1-100): ")
    
    try:
        guess = int(guess_input)
    except ValueError:
        print("Invalid input! Please enter a whole number. (No attempt used)")
        continue
        
    attempts_used += 1
    
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Correct! You win!")
        won = True
        break

if not won:
    print(f"\nGame Over! The secret number was {secret_number}.")

# What we accomplished in this step:
# - We added robust error handling to prevent game crashes.
# - We implemented fair game mechanics by not punishing the player for typos.


# Step 4
# Explanation: Let's make the game replayable. We will wrap the entire game logic 
# inside a new, outer `while True:` loop. At the end of a round, we will ask the 
# player if they want to play again. If they type anything other than 'yes', we 
# will break the outer loop and end the program.

import random

while True:
    print("\n--- Number Guessing Game ---")
    secret_number = random.randint(1, 100)
    print(f"(Testing) The secret number is {secret_number}")
    
    attempts_allowed = 7
    attempts_used = 0
    won = False
    
    while attempts_used < attempts_allowed:
        guess_input = input(f"\nAttempt {attempts_used + 1}/{attempts_allowed}. Guess a number (1-100): ")
        
        try:
            guess = int(guess_input)
        except ValueError:
            print("Invalid input! Please enter a whole number. (No attempt used)")
            continue
            
        attempts_used += 1
        
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Correct! You got it in {attempts_used} attempts!")
            won = True
            break
            
    if not won:
        print(f"\nGame Over! The secret number was {secret_number}.")
        
    # Ask to play again
    play_again = input("\nWould you like to play again? (yes/no): ").lower()
    if play_again != 'yes' and play_again != 'y':
        print("Thanks for playing! Goodbye.")
        break

# What we accomplished in this step:
# - We created a "game loop" architecture by nesting the core game inside a replay loop.
# - We handled replay string input by converting it to lowercase for easier comparison.


# Step 5
# Explanation: For our final step, we will clean up our code by moving the game 
# logic into its own function. We will also remove the "testing" print statement 
# so the game is actually a secret! Finally, we provide an example run block.

import random

def play_game():
    """Runs a single round of the number guessing game."""
    print("\n" + "="*30)
    print("   NUMBER GUESSING GAME")
    print("="*30)
    print("I am thinking of a number between 1 and 100.")
    
    secret_number = random.randint(1, 100)
    attempts_allowed = 7
    attempts_used = 0
    won = False
    
    while attempts_used < attempts_allowed:
        guess_input = input(f"\n[Attempt {attempts_used + 1}/{attempts_allowed}] Your guess: ")
        
        try:
            guess = int(guess_input)
        except ValueError:
            print("-> Please enter a valid number! (No attempt used)")
            continue
            
        # Optional: Warn if out of bounds (doesn't consume attempt)
        if guess < 1 or guess > 100:
            print("-> Please stay between 1 and 100! (No attempt used)")
            continue
            
        attempts_used += 1
        
        if guess < secret_number:
            print("-> Too low!")
        elif guess > secret_number:
            print("-> Too high!")
        else:
            print(f"\n🎉 CORRECT! You found the number in {attempts_used} attempts! 🎉")
            won = True
            break
            
    if not won:
        print(f"\n💀 GAME OVER! The secret number was {secret_number}. 💀")

def main():
    """Main game loop handling the replay logic."""
    while True:
        play_game()
        
        replay = input("\nPlay again? (yes/no): ").strip().lower()
        if replay not in ['yes', 'y']:
            print("\nThanks for playing! See you next time.")
            break

# Test our code:
# Uncomment the function call below to start the interactive game
# main()

# Example run:
# ==============================
#    NUMBER GUESSING GAME
# ==============================
# I am thinking of a number between 1 and 100.
# 
# [Attempt 1/7] Your guess: fifty
# -> Please enter a valid number! (No attempt used)
#
# [Attempt 1/7] Your guess: 50
# -> Too low!
#
# [Attempt 2/7] Your guess: 75
# -> Too high!
#
# [Attempt 3/7] Your guess: 62
# -> Too high!
#
# [Attempt 4/7] Your guess: 56
# 🎉 CORRECT! You found the number in 4 attempts! 🎉
#
# Play again? (yes/no): no
#
# Thanks for playing! See you next time.

# What we accomplished in this step:
# - We encapsulated the logic neatly into `play_game()` and `main()` functions.
# - We added an out-of-bounds check as an extra layer of user-friendliness.
# - We created a clean, polished, interactive terminal experience.


# CONGRATULATIONS! 🎉
# You have successfully built a fully interactive mini-project! 
# You combined everything you've learned about control flow: while loops, 
# nested conditionals, importing external modules (like `random`), robust error 
# handling with `try/except`, and creating outer "game loops" for replayability. 
# This architecture is the foundation of almost all interactive software applications.
# Remember: The best way to learn is by doing! 🚀
