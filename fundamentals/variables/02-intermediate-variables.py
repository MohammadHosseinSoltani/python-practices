"""Question: Swap the values of two variables without using a temporary third variable. Then, create variables of different types and combine them into a single descriptive sentence using an f-string."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Think about how Python allows you to assign multiple variables on a single line (tuple unpacking) to perform the swap.
# - When combining different variable types (like numbers and text) into a sentence, remember how f-strings automatically handle the conversion.
#
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - To swap two variables in Python, you can write `a, b = b, a`.
# - If you want to combine numbers with text, you can either use `str()` inside the f-string or just put the variable in curly braces – f-strings handle the conversion for you.
# - Think about what types of data you could use: an integer for age, a float for score, a string for name, etc.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start with the first part of the challenge: swapping variables. 
# Before we can swap them, we need to create them. We will create two variables, `x` 
# and `y`, give them distinct initial values, and print them out so we have a baseline 
# to compare against later.

x = 5
y = 10

print("Before swap:")
print(f"x = {x}")
print(f"y = {y}")

# What we accomplished in this step:
# - Created two initial variables.
# - Printed their starting states using simple f-strings.


# Step 2
# Explanation: In many older programming languages, swapping two variables requires 
# creating a temporary third variable to hold one of the values while you overwrite it. 
# Python is much more elegant! By using a feature called "tuple unpacking", we can 
# swap the values on a single line of code. Let's do that and print the results to 
# prove it worked.

x = 5
y = 10

print("Before swap:")
print(f"x = {x}")
print(f"y = {y}")

# Perform the swap using tuple unpacking
x, y = y, x

print("\nAfter swap:")
print(f"x = {x}")
print(f"y = {y}")

# What we accomplished in this step:
# - Swapped the values of two variables seamlessly without a temporary variable.
# - Verified the swap was successful through printed output.


# Step 3
# Explanation: Now let's tackle the second part of the challenge. We need to create 
# variables of different types. Python is "dynamically typed," meaning we don't have 
# to declare the type ahead of time; Python figures it out based on the value we assign. 
# We will create a string for a name, an integer for an age, and a float for a score. 
# Let's print each one along with its type using the `type()` function.

x = 5
y = 10

x, y = y, x

# Create new variables of varying types
student_name = "Alice"
student_age = 25
student_score = 95.5

print("\nVariable Types:")
print(f"student_name is '{student_name}' and its type is {type(student_name)}")
print(f"student_age is {student_age} and its type is {type(student_age)}")
print(f"student_score is {student_score} and its type is {type(student_score)}")

# What we accomplished in this step:
# - Created a String, an Integer, and a Float.
# - Used the `type()` function to inspect how Python categorized our data.


# Step 4
# Explanation: Finally, we want to combine all of these different pieces of data into 
# a single, readable sentence. In the past, you might have had to manually convert 
# `student_age` and `student_score` into strings using `str()` before adding them to text. 
# But with modern f-strings, we just place the variable names inside curly braces `{}`, 
# and Python handles the conversion formatting for us automatically!

x = 5
y = 10

x, y = y, x

student_name = "Alice"
student_age = 25
student_score = 95.5

# Construct a single sentence using an f-string
summary_sentence = f"{student_name}, aged {student_age}, scored {student_score} points on the final exam."

print("\nCombined Sentence:")
print(summary_sentence)

# What we accomplished in this step:
# - Used an f-string to seamlessly inject multiple data types into a single text string.
# - Relied on Python's automatic type conversion within f-strings.


# Step 5
# Explanation: Our code is complete. Let's consolidate everything into a clean script, 
# removing the intermediate type checks to focus on the core requirements of the 
# exercise. We will provide a comprehensive test block below so you can see exactly 
# how the final output should look.

# Test our code:
if __name__ == "__main__":
    
    # Part 1: Swapping variables
    item_a = "Apple"
    item_b = "Banana"
    
    print("--- Swapping Variables ---")
    print(f"Start: item_a = {item_a}, item_b = {item_b}")
    
    item_a, item_b = item_b, item_a
    
    print(f"End  : item_a = {item_a}, item_b = {item_b}")
    # Expected output:
    # --- Swapping Variables ---
    # Start: item_a = Apple, item_b = Banana
    # End  : item_a = Banana, item_b = Apple

    
    # Part 2: Combining types
    player_name = "Zane"
    player_level = 42
    health_points = 87.5
    
    print("\n--- Combining Types ---")
    status_message = f"Player {player_name} (Level {player_level}) currently has {health_points} HP."
    print(status_message)
    # Expected output:
    # --- Combining Types ---
    # Player Zane (Level 42) currently has 87.5 HP.


# CONGRATULATIONS! 🎉
# You've mastered some very "Pythonic" techniques today!
#
# Key takeaways:
# - Swapping Variables: You learned the elegant `a, b = b, a` syntax, avoiding the clunky temporary variables required in other languages.
# - Dynamic Typing: You saw how Python automatically knows that `25` is an integer and `95.5` is a float just by looking at the value.
# - F-String Composition: You utilized formatted string literals (f-strings) to effortlessly mix strings, integers, and floats into a single, highly readable sentence.
#
# Remember: The best way to learn is by doing! 🚀
