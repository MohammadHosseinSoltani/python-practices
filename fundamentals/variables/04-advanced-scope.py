"""Question: Explore variable scope in Python. Demonstrate how variables inside a function are local by default, how to read a global variable without modifying it, and how to use the `global` keyword to modify a global variable from within a function."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Try creating a global variable `count = 0` outside of any function.
# - Write a function that attempts to modify `count` (like `count = count + 1`). Watch out for the `UnboundLocalError`!
# - Learn how to use the `global` keyword inside your function to fix the error.
# 
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Try creating a global variable `count = 0`.
# - Write a function that attempts to increment `count` by 1. What happens?
# - If you only need to *read* the global variable (not modify it), you can access it directly inside a function.
# - To modify a global variable, you must declare `global count` at the top of your function.
# - Remember that abusing global variables can make your code harder to debug; use them sparingly.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by defining a global variable named `score` and a 
# simple function to print it. In Python, if we only want to *read* a global 
# variable, we don't need any special keywords. The function will automatically 
# look outside its local scope to find the variable.

score = 50

def display_score():
    # We can read the global variable 'score' without any issues
    print(f"The current score is: {score}")

display_score()

# What we accomplished in this step:
# - We created a global variable.
# - We successfully read and printed the global variable from inside a local function scope.


# Step 2
# Explanation: Now we'll add a new function that attempts to *change* our 
# global variable. If we try to do `score = score + 100`, Python gets confused. 
# Because we are assigning a value to `score`, Python assumes `score` must be 
# a local variable. But it hasn't been created locally yet! This results in an 
# UnboundLocalError. We will wrap it in a try-except block so our script doesn't crash.

score = 50

def display_score():
    print(f"The current score is: {score}")

def update_score_failing():
    try:
        # Python thinks 'score' is local because of the assignment (=), 
        # but we are trying to use it before it has a local value.
        score = score + 100
    except UnboundLocalError as error_message:
        print(f"Oops! We got an error: {error_message}")

display_score()
update_score_failing()

# What we accomplished in this step:
# - We attempted to modify a global variable directly.
# - We observed and caught an `UnboundLocalError`, learning that assignment makes Python assume a variable is local.


# Step 3
# Explanation: To fix the error from Step 2, we need to explicitly tell Python 
# that we want to use the global version of `score`, not create a local one. 
# We do this using the `global` keyword at the beginning of our function.

score = 50

def display_score():
    print(f"The current score is: {score}")

def update_score_failing():
    try:
        score = score + 100
    except UnboundLocalError as error_message:
        print(f"Oops! We got an error: {error_message}")

def update_score_global():
    # This tells Python: "When I say 'score', I mean the one outside the function!"
    global score
    score = score + 100
    print(f"Success! Inside update_score_global, score is now: {score}")

display_score()
update_score_failing()
update_score_global()
display_score()

# What we accomplished in this step:
# - We introduced the `global` keyword.
# - We successfully modified a global variable from within a function's local scope.


# Step 4
# Explanation: While the `global` keyword works, using it too much is generally 
# considered bad practice because it makes code hard to track and debug. A much 
# better, safer practice is to pass the variable into the function as a parameter, 
# and return the new value. Let's add a function that does exactly this.

score = 50

def display_score():
    print(f"The current score is: {score}")

def update_score_failing():
    try:
        score = score + 100
    except UnboundLocalError as error_message:
        print(f"Oops! We got an error: {error_message}")

def update_score_global():
    global score
    score = score + 100
    print(f"Success! Inside update_score_global, score is now: {score}")

def update_score_better(current_score):
    # We take the value as an input, modify it locally, and hand it back.
    # No global keywords needed!
    new_score = current_score + 100
    return new_score

# What we accomplished in this step:
# - We learned the "best practice" approach for modifying data: parameters and return values.
# - We wrote a pure function that avoids relying on external state.


# Step 5
# Explanation: Let's consolidate all our scenarios into a final script with a 
# clean testing block so we can see the full story of variable scope in action.

score = 50

def display_score():
    print(f"Reading global score: {score}")

def update_score_failing():
    try:
        score = score + 100
    except UnboundLocalError as error_message:
        print(f"Failing update error: {error_message}")

def update_score_global():
    global score
    score = score + 100
    print(f"Global keyword update: score changed to {score}")

def update_score_better(current_score):
    new_score = current_score + 100
    print(f"Better practice update: returning new score {new_score}")
    return new_score

# Test our code:
print("--- SCENARIO 1: Reading a global variable ---")
display_score()
# Expected output: Reading global score: 50

print("\n--- SCENARIO 2: Failing to modify without 'global' ---")
update_score_failing()
# Expected output: Failing update error: cannot access local variable 'score' where it is not associated with a value

print("\n--- SCENARIO 3: Modifying using 'global' ---")
update_score_global()
# Expected output: Global keyword update: score changed to 150
display_score()
# Expected output: Reading global score: 150

print("\n--- SCENARIO 4: The better practice (parameters and returns) ---")
# We pass the current score (150) in, and catch the returned value (250)
score = update_score_better(score)
display_score()
# Expected output: Reading global score: 250

# What we accomplished in this step:
# - We structured a clean, complete demonstration of variable scope.
# - We verified all our approaches with print statements and comments showing expected outputs.


# CONGRATULATIONS! 🎉
# You have successfully navigated the tricky waters of variable scope in Python!
# You now understand the difference between local and global scope, why the 
# `UnboundLocalError` occurs, and how to resolve it using the `global` keyword.
# More importantly, you learned that passing parameters and returning values is 
# often a cleaner, safer alternative to relying on global variables.
# Keep experimenting with creating your own functions and passing data between them.
# Remember: The best way to learn is by doing! 🚀
