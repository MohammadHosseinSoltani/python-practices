"""Question: Create variables of different types (integer, float, string) and print their values and types."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
# 
# Tips for success:
# - Read the question carefully to understand what is being asked.
# - Start simple by defining one variable at a time.
# - Test your code frequently by running it to see what prints out.
# 
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Think about what types of data you can store (like whole numbers, decimals, and text).
# - Use the `type()` function to check types (e.g., `print(type(my_variable))`).
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by creating a simple integer variable. In Python, we do not need 
# to declare the type of a variable beforehand. We just give it a descriptive name, use the 
# assignment operator `=`, and give it a whole number.
student_age = 25
print(student_age)

# What we accomplished in this step:
# - Created our first variable using snake_case naming.
# - Assigned an integer (whole number) value to it.
# - Used the print() function to display its value.


# Step 2
# Explanation: Now we'll add a float variable. A float is simply a number that has a 
# decimal point. We will also introduce the `type()` function to peek under the hood 
# and see how Python internally classifies this data.
student_age = 25
print(student_age)

test_score = 95.5
print(test_score)
print(type(test_score))

# What we accomplished in this step:
# - Created a float variable for a decimal number.
# - Printed the float's value.
# - Used type() to confirm that Python recognizes it as a float.


# Step 3
# Explanation: Next, let's create a string variable. Strings are used to store text and 
# must be surrounded by either single or double quotes. We will print the string and its type.
student_age = 25
print(student_age)

test_score = 95.5
print(test_score)
print(type(test_score))

student_name = "Alice"
print(student_name)
print(type(student_name))

# What we accomplished in this step:
# - Created a string variable to hold text.
# - Printed the string and explicitly checked its type.


# Step 4
# Explanation: Having isolated variables is great, but programming is really about making 
# them work together. We will use an "f-string" (formatted string) to seamlessly combine 
# our string, integer, and float into one readable sentence.
student_age = 25
test_score = 95.5
student_name = "Alice"

message = f"{student_name} is {student_age} years old and scored {test_score} on the test."
print(message)

# What we accomplished in this step:
# - Created an f-string by placing an 'f' before the opening quote.
# - Inserted different types of variables directly into a string using curly braces {}.
# - Printed a complete, dynamic sentence.


# Step 5
# Explanation: Let's take a moment to use `type()` to print the type of each variable 
# explicitly and clearly. Understanding how to check data types is one of the most important 
# debugging skills you will develop as a programmer.
student_age = 25
test_score = 95.5
student_name = "Alice"

print("Variable Types:")
print(type(student_age))
print(type(test_score))
print(type(student_name))

# What we accomplished in this step:
# - Grouped our type checks together.
# - Verified that we have an 'int', a 'float', and a 'str'.


# Step 6
# Explanation: For our final step, let's bring everything together in a clear, 
# well-documented test block. We'll add descriptive messages to our print statements 
# and show the expected output as comments, so we know exactly what our program is doing.
student_age = 25
test_score = 95.5
student_name = "Alice"

# Test our code:
print("--- Variable Values ---")
print(f"Name: {student_name}")        # Expected output: Name: Alice
print(f"Age: {student_age}")          # Expected output: Age: 25
print(f"Score: {test_score}")         # Expected output: Score: 95.5

print("\n--- Variable Types ---")
print(f"Type of student_name: {type(student_name)}")  # Expected output: <class 'str'>
print(f"Type of student_age: {type(student_age)}")    # Expected output: <class 'int'>
print(f"Type of test_score: {type(test_score)}")      # Expected output: <class 'float'>

# What we accomplished in this step:
# - Consolidated our code into a professional, easy-to-read format.
# - Added expected outputs as comments for clarity.
# - Demonstrated a complete understanding of basic variables and types!


# CONGRATULATIONS! 🎉
# You have successfully created and manipulated the core data types in Python.
# 
# Key takeaways:
# - Variables are created simply by assigning a value to a name using '='.
# - Integers (int) hold whole numbers, floats (float) hold decimals, and strings (str) hold text.
# - The type() function is an invaluable tool for exploring what kind of data you have.
# - f-strings allow you to effortlessly mix different variable types into readable text.
# 
# Keep experimenting! Try changing the values, adding new variables of your own, 
# or creating a completely different scenario (like a shopping cart or a game character).
# 
# Remember: The best way to learn is by doing! 🚀
