"""Question: Write a program that checks a person's age and prints a message based on whether they are an adult, teenager, or child."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Think through the logic and the order of your conditions.
# - Test with different age values to ensure every category works.
# - Use `if`, `elif`, and `else` to structure your decisions.
#
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Use `if`, `elif`, and `else` to check different conditions.
# - Comparison operators like `>`, `<`, `>=`, `<=` are your friends.
# - Test with different ages (e.g., 10, 15, 30) to see how the program behaves.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by creating a variable for `age`. We will use a simple `if` 
# statement to check if the age is 18 or greater. If the condition evaluates to True, 
# the indented code block beneath it will run.
age = 20

if age >= 18:
    print("You are an adult.")

# What we accomplished in this step:
# - Created an integer variable to hold the age.
# - Wrote our first conditional statement using `if`.
# - Used the `>=` (greater than or equal to) comparison operator.


# Step 2
# Explanation: Our first program is great, but it does nothing if the person is under 18. 
# Let's add an `else` clause. The `else` block catches everything that makes the `if` 
# condition False. We will change the age to 15 to test this new pathway.
age = 15

if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult yet.")

# What we accomplished in this step:
# - Added an `else` statement to handle the alternative scenario.
# - Ensured our program always provides feedback, regardless of the age.


# Step 3
# Explanation: "Not an adult yet" is a bit vague. We want to specifically identify teenagers.
# We can introduce `elif` (short for "else if") to check another condition before falling 
# back to `else`. Because Python checks these in order, if `age >= 18` is False, it moves 
# down and checks if `age >= 13`.
age = 15

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

# What we accomplished in this step:
# - Introduced the `elif` keyword for multiple conditions.
# - Created a categorized structure: Adult, Teenager, and Child.


# Step 4
# Explanation: What if someone accidentally enters a negative number for their age? 
# Currently, our code would call them a "child". Let's add another `elif` to handle 
# valid children (age 0 to 12), and use the final `else` to catch invalid negative numbers.
age = -5

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
elif age >= 0:
    print("You are a child.")
else:
    print("Invalid age entered.")

# What we accomplished in this step:
# - Refined our logic to handle edge cases (like negative numbers).
# - Made our program more robust and accurate.


# Step 5
# Explanation: In the real world, we usually get data from users. We can use the `input()` 
# function for this. Because `input()` always returns a string (text), we must convert it 
# to an integer using `int()` before doing math comparisons. 
# (Note: We use a hardcoded string here so the program runs smoothly, but you can swap 
# it out for real input in your own terminal!)
user_input = "25"  # In reality, this would be: user_input = input("Enter your age: ")

# Convert the string to an integer
age = int(user_input)

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
elif age >= 0:
    print("You are a child.")
else:
    print("Invalid age entered.")

# What we accomplished in this step:
# - Learned how user input is captured as a string.
# - Demonstrated type conversion (`int()`) to safely evaluate the data.


# Step 6
# Explanation: For our final step, let's consolidate everything into a clean demonstration.
# We will test our logic manually with several different ages by changing the variable 
# directly. This proves our code works in all possible scenarios.

# Test our code:
print("--- Age Categorization Tests ---")

# Test 1: Adult
age_1 = 30
print(f"Testing age {age_1}:")
if age_1 >= 18:
    print("Result: You are an adult.")          # Expected output: Result: You are an adult.
elif age_1 >= 13:
    print("Result: You are a teenager.")
elif age_1 >= 0:
    print("Result: You are a child.")
else:
    print("Result: Invalid age entered.")

# Test 2: Teenager
age_2 = 14
print(f"\nTesting age {age_2}:")
if age_2 >= 18:
    print("Result: You are an adult.")
elif age_2 >= 13:
    print("Result: You are a teenager.")        # Expected output: Result: You are a teenager.
elif age_2 >= 0:
    print("Result: You are a child.")
else:
    print("Result: Invalid age entered.")

# Test 3: Child
age_3 = 8
print(f"\nTesting age {age_3}:")
if age_3 >= 18:
    print("Result: You are an adult.")
elif age_3 >= 13:
    print("Result: You are a teenager.")
elif age_3 >= 0:
    print("Result: You are a child.")           # Expected output: Result: You are a child.
else:
    print("Result: Invalid age entered.")

# Test 4: Invalid
age_4 = -2
print(f"\nTesting age {age_4}:")
if age_4 >= 18:
    print("Result: You are an adult.")
elif age_4 >= 13:
    print("Result: You are a teenager.")
elif age_4 >= 0:
    print("Result: You are a child.")
else:
    print("Result: Invalid age entered.")       # Expected output: Result: Invalid age entered.

# What we accomplished in this step:
# - Created a comprehensive test block.
# - Verified every single branch of our if/elif/else structure.
# - Used f-strings to format our output clearly.


# CONGRATULATIONS! 🎉
# You have successfully implemented control flow logic in Python!
# 
# Key takeaways:
# - `if` statements allow your program to make decisions based on data.
# - `elif` (else if) lets you chain multiple conditions together.
# - `else` acts as a catch-all for anything that didn't meet the previous conditions.
# - Comparison operators (`>=`, `<`, etc.) are essential for numeric logic.
# - When working with `input()`, always remember to convert the text into an integer 
#   if you need to perform numerical checks!
# 
# Remember: The best way to learn is by doing! 🚀
