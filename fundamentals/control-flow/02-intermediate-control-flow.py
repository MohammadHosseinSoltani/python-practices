"""Question: Write a program that asks the user for a percentage score (0-100) and prints the corresponding letter grade (A, B, C, D, F). Use nested conditionals to handle invalid input (non-numeric or out-of-range) and give the user a chance to re-enter a valid score."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Use a `while` loop to keep asking the user until a valid input is given.
# - Use a `try/except` block to handle cases where the user types letters instead of numbers.
# - Use an `if/elif/else` structure to check the different grading tiers.
#
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Use a `while True:` loop to repeatedly ask for input.
# - Convert the input to an integer with `int()`, but wrap it in a `try/except ValueError` to catch non-numeric entries.
# - If the input is valid, use `if/elif/else` to determine the grade: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).
# - If the input is out of the 0-100 range or not a number, print an error and let the loop run again.
# - Exit the loop only when a valid score is entered and the grade is printed.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by creating a function with a basic `while True` loop. 
# This loop will repeatedly ask the user for input. To prevent our program from 
# getting stuck in an infinite loop during this early test phase, we will immediately 
# print what was entered and use the `break` keyword to exit the loop.

def calculate_grade_step1():
    while True:
        score_input = input("Enter a percentage score (0-100): ")
        print(f"You entered: {score_input}")
        
        # We break immediately just to test our loop safely
        break

# What we accomplished in this step:
# - We set up an infinite `while` loop to continually prompt the user.
# - We captured the user's input.
# - We used `break` to safely exit the loop.


# Step 2
# Explanation: Now we'll add the core grading logic. We will assume the user behaves 
# perfectly and types a valid number. We convert the input to an integer using `int()` 
# and use an `if/elif/else` chain to determine the correct letter grade. Once the 
# grade is printed, we break out of the loop.

def calculate_grade_step2():
    while True:
        score_input = input("Enter a percentage score (0-100): ")
        
        # Assume the input is a valid number for now
        score = int(score_input)
        
        if score >= 90:
            print("Grade: A")
        elif score >= 80:
            print("Grade: B")
        elif score >= 70:
            print("Grade: C")
        elif score >= 60:
            print("Grade: D")
        else:
            print("Grade: F")
            
        # Exit the loop now that we have successfully printed the grade
        break

# What we accomplished in this step:
# - We converted the string input into an integer.
# - We implemented the grading logic using an `if/elif/else` structure.
# - We broke the loop upon successful completion.


# Step 3
# Explanation: Users don't always behave perfectly! If they type "eighty" instead 
# of "80", our `int()` conversion will crash the program with a ValueError. Let's 
# wrap the conversion in a `try/except` block. If an error happens, we print a 
# warning and use `continue` to jump back to the start of the loop and ask again.

def calculate_grade_step3():
    while True:
        score_input = input("Enter a percentage score (0-100): ")
        
        try:
            # Attempt to convert the input to an integer
            score = int(score_input)
        except ValueError:
            # If they typed text, catch the error and warn them
            print("Invalid input! Please enter a numeric value.")
            continue  # Skip the rest of the loop and start over
        
        if score >= 90:
            print("Grade: A")
        elif score >= 80:
            print("Grade: B")
        elif score >= 70:
            print("Grade: C")
        elif score >= 60:
            print("Grade: D")
        else:
            print("Grade: F")
            
        break

# What we accomplished in this step:
# - We used `try/except` to gracefully handle bad, non-numeric input.
# - We introduced the `continue` keyword to restart the loop on failure.


# Step 4
# Explanation: Even if the user types a number, they might type "-5" or "150". 
# These are out of bounds for a standard percentage. We need to add range validation 
# right after we successfully get the integer. If it's out of range, we warn the 
# user and `continue` to ask again.

def calculate_grade_step4():
    while True:
        score_input = input("Enter a percentage score (0-100): ")
        
        try:
            score = int(score_input)
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            continue
            
        # Range validation
        if score < 0 or score > 100:
            print("Error: Score must be between 0 and 100. Please try again.")
            continue
        
        if score >= 90:
            print("Grade: A")
        elif score >= 80:
            print("Grade: B")
        elif score >= 70:
            print("Grade: C")
        elif score >= 60:
            print("Grade: D")
        else:
            print("Grade: F")
            
        break

# What we accomplished in this step:
# - We added a logical check (`< 0` or `> 100`) to validate the numerical range.
# - We combined data-type validation with logical range validation.


# Step 5
# Explanation: Let's consolidate our function into a clean, final version with 
# descriptive comments. We will provide an example run block below it so you can 
# see exactly how the program handles different scenarios.

def calculate_grade():
    """Asks the user for a score, validates it, and prints the letter grade."""
    print("--- Grade Calculator ---")
    
    while True:
        score_input = input("Enter a percentage score (0-100): ")
        
        # Step A: Validate that the input is an integer
        try:
            score = int(score_input)
        except ValueError:
            print(">> Invalid input! Please enter a numeric value.\n")
            continue
            
        # Step B: Validate that the integer is within the correct range
        if score < 0 or score > 100:
            print(">> Error: Score must be between 0 and 100. Please try again.\n")
            continue
        
        # Step C: Calculate the grade
        if score >= 90:
            letter = "A"
        elif score >= 80:
            letter = "B"
        elif score >= 70:
            letter = "C"
        elif score >= 60:
            letter = "D"
        else:
            letter = "F"
            
        print(f">> Success! A score of {score}% is a '{letter}' grade.\n")
        break  # Exit the loop

# Test our code:
# To run this yourself, simply uncomment the function call below:
# calculate_grade()

# Example run:
# ---------------------------------------------------------
# --- Grade Calculator ---
# Enter a percentage score (0-100): hello
# >> Invalid input! Please enter a numeric value.
#
# Enter a percentage score (0-100): 105
# >> Error: Score must be between 0 and 100. Please try again.
#
# Enter a percentage score (0-100): -10
# >> Error: Score must be between 0 and 100. Please try again.
#
# Enter a percentage score (0-100): 85
# >> Success! A score of 85% is a 'B' grade.
# ---------------------------------------------------------

# What we accomplished in this step:
# - We polished the formatting to make the user interface cleaner.
# - We extracted the grade string to a variable (`letter`) to keep the print statement DRY (Don't Repeat Yourself).
# - We demonstrated a simulated, multi-step interactive session.


# CONGRATULATIONS! 🎉
# You have successfully built a robust interactive program!
# You learned how to use a `while True:` loop to enforce continuous prompting,
# how to safely attempt data conversions using `try/except`, and how to layer 
# multiple levels of validation (type checking and range checking) before 
# committing to the core business logic (grading). 
# Handling bad input gracefully is a hallmark of professional software development!
# Remember: The best way to learn is by doing! 🚀
