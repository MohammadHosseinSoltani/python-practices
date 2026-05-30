"""Question: Define a function called greet that takes a name as an argument and prints a greeting message. Then call the function with different names."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Think about what the function needs to do and what data it requires.
# - Use the `def` keyword to define your function.
# - Remember that you must call the function after defining it to see it work!
#
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Use the `def` keyword to define a function (e.g., `def my_function():`).
# - The function should accept one parameter (the name). Place it inside the parentheses.
# - Use a print statement inside the function to display the greeting.
# - Call the function with different names to test it (e.g., `greet("Alice")`).
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by defining our function. We use the `def` keyword, followed 
# by the name we want to give our function (`greet`) and a set of parentheses. We finish 
# the line with a colon. For now, we will use the `pass` keyword inside the body, which 
# tells Python "do nothing for now." This is a great way to skeleton out our code.
def greet():
    pass

# What we accomplished in this step:
# - Used the `def` keyword to declare a new function named `greet`.
# - Used `pass` to create a syntactically valid empty function.


# Step 2
# Explanation: Now we'll add a parameter to our function. A parameter acts as a placeholder 
# variable for the data the function expects to receive when it is called. We will name 
# this parameter `name` so our function knows who it is greeting.
def greet(name):
    pass

# What we accomplished in this step:
# - Added a `name` parameter inside the function's parentheses.
# - Prepared the function to accept external data.


# Step 3
# Explanation: Let's replace the `pass` statement with actual code. We want our function 
# to do something when it runs. We will use an f-string to combine a friendly greeting 
# with the `name` parameter, and then print that combined string to the screen.
def greet(name):
    print(f"Hello, {name}! Welcome to Python programming.")

# What we accomplished in this step:
# - Replaced the `pass` placeholder with actual logic.
# - Used an f-string to dynamically insert the `name` parameter into a printed message.


# Step 4
# Explanation: A function won't do anything on its own until we actually call (or execute) it. 
# Let's call our `greet` function a couple of times. We do this by writing the function's name 
# followed by parentheses, passing in different string values (arguments) for the `name` parameter.
def greet(name):
    print(f"Hello, {name}! Welcome to Python programming.")

greet("Alice")
greet("Bob")

# What we accomplished in this step:
# - Called the `greet` function twice.
# - Passed different arguments ("Alice" and "Bob") into the function to see different outputs.


# Step 5
# Explanation: Printing inside a function is helpful, but in real-world programming, we often 
# want a function to process data and hand the result back to us so we can use it elsewhere. 
# We achieve this using the `return` keyword instead of `print`. Let's modify our function 
# to return the string, and then we will capture that result in a variable and print it ourselves.
def greet(name):
    return f"Hello, {name}! Welcome to Python programming."

alice_message = greet("Alice")
print(alice_message)

# What we accomplished in this step:
# - Replaced `print` with `return` to send data back to the caller.
# - Captured the returned value in a variable (`alice_message`).
# - Printed the captured variable to prove it worked.


# Step 6
# Explanation: For our final step, let's consolidate everything into a clean demonstration. 
# We will keep our function that returns a value, and we will test it with a few different names. 
# We'll print the results with expected output comments so we can clearly see what the code does.

def greet(name):
    # Creates and returns a personalized greeting string
    return f"Hello, {name}! Welcome to Python programming."

# Test our code:
print("--- Function Demonstration ---")

# Test 1
message_1 = greet("Alice")
print(message_1)  # Expected output: Hello, Alice! Welcome to Python programming.

# Test 2
message_2 = greet("Bob")
print(message_2)  # Expected output: Hello, Bob! Welcome to Python programming.

# Test 3
message_3 = greet("Charlie")
print(message_3)  # Expected output: Hello, Charlie! Welcome to Python programming.

# What we accomplished in this step:
# - Organized our function and testing logic clearly.
# - Called the function multiple times with different arguments.
# - Documented the expected outputs using comments for easy verification.


# CONGRATULATIONS! 🎉
# You have successfully defined and used your first Python function!
# 
# Key takeaways:
# - The `def` keyword is essential for defining reusable blocks of code (functions).
# - Functions can accept input data through 'parameters' (like `name`).
# - We execute a function by 'calling' it and passing in specific values called 'arguments'.
# - The `return` keyword is a powerful way to send computed data back to the main program, 
#   making your functions much more versatile than just using `print`.
# 
# Keep experimenting! Try adding a second parameter to the function (like `age` or `city`) 
# and update the returned string to include that new information.
# 
# Remember: The best way to learn is by doing! 🚀
