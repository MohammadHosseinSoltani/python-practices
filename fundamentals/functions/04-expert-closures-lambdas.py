"""Question: Explore advanced function concepts: write a higher-order function that returns a closure (a function that remembers a value from its enclosing scope). Then, demonstrate using lambda functions for short, inline calculations. Compare both approaches."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Understand that a closure allows a nested function to remember variables from its parent function.
# - Practice using the `lambda` keyword for creating anonymous, inline functions.
# - Try writing a function that creates and returns another function.
#
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - A closure is a function that 'closes over' a variable from its enclosing scope.
# - To create a closure, define a nested function that uses a variable from the outer function, then return the nested function.
# - A lambda function is a tiny anonymous function defined with `lambda arguments: expression`.
# - Try writing a `make_multiplier(x)` function that returns a new function that multiplies its input by `x`.
# - Use a lambda to create the same multiplier function inline: `lambda x: lambda n: n * x`.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by looking at a standard function that takes two arguments 
# and multiplies them together. This is the traditional way we perform operations, 
# requiring both pieces of data at the exact same time.

def multiply(a, b):
    return a * b

print("--- Step 1: Standard Function ---")
print(f"Multiplying 2 and 5: {multiply(2, 5)}")

# What we accomplished in this step:
# - We created a basic, two-parameter function.
# - We observed that both arguments must be provided simultaneously to get a result.


# Step 2
# Explanation: Sometimes we want to configure a function now, but use it later. 
# We can do this by creating a "higher-order function" (a function that returns 
# another function). Here, `make_multiplier` takes `x`, creates an inner function 
# that takes `n`, and returns that inner function.

def multiply(a, b):
    return a * b

def make_multiplier(x):
    def multiplier(n):
        return n * x
    # Notice we return the function itself, not a call to the function (no parentheses)
    return multiplier

print("\n--- Step 2: Higher-Order Function ---")
# We configure our multiplier with the number 2
doubler = make_multiplier(2)

# We can now use 'doubler' as a function later in our code
print(f"Using our doubler on 5: {doubler(5)}")
print(f"Using our doubler on 10: {doubler(10)}")

# What we accomplished in this step:
# - We wrote a function that returns another function.
# - We "pre-configured" a mathematical operation and saved it to a variable (`doubler`).


# Step 3
# Explanation: How does the `doubler` function know that `x` is 2 long after 
# `make_multiplier` has finished running? This is the magic of a "closure". 
# The inner function "closes over" (remembers) the environment in which it was 
# created. We can actually peek inside Python's hidden attributes to prove this!

def multiply(a, b):
    return a * b

def make_multiplier(x):
    def multiplier(n):
        return n * x
    return multiplier

doubler = make_multiplier(2)
tripler = make_multiplier(3)

print("\n--- Step 3: Inspecting Closures ---")
print(f"Doubler on 5: {doubler(5)}")
print(f"Tripler on 5: {tripler(5)}")

# Inspecting the __closure__ attribute (expert level trick!)
doubler_memory = doubler.__closure__[0].cell_contents
tripler_memory = tripler.__closure__[0].cell_contents

print(f"The doubler function secretly remembers the value: {doubler_memory}")
print(f"The tripler function secretly remembers the value: {tripler_memory}")

# What we accomplished in this step:
# - We learned the definition of a closure.
# - We inspected the `__closure__` attribute to see the exact data our functions are remembering.


# Step 4
# Explanation: Python offers a shortcut for creating small, nameless functions 
# called "lambdas". We can use a lambda to recreate our closure in a single line. 
# The syntax is `lambda arguments: expression`. We will write a lambda that takes 
# `x` and returns another lambda that takes `n`.

def multiply(a, b):
    return a * b

def make_multiplier(x):
    def multiplier(n):
        return n * x
    return multiplier

doubler = make_multiplier(2)
tripler = make_multiplier(3)

# Creating the exact same logic using lambdas
make_multiplier_lambda = lambda x: lambda n: n * x

print("\n--- Step 4: Using Lambdas ---")
quadrupler = make_multiplier_lambda(4)
print(f"Using lambda quadrupler on 5: {quadrupler(5)}")

# What we accomplished in this step:
# - We introduced the `lambda` keyword for creating anonymous functions.
# - We successfully chained lambdas to replicate our higher-order closure function.


# Step 5
# Explanation: Let's consolidate everything into a clean testing script. We will 
# compare the traditional closure approach with the lambda approach side-by-side 
# to clearly see how they accomplish the exact same goal.

def make_multiplier_standard(x):
    """Standard approach using a nested function to create a closure."""
    def multiplier(n):
        return n * x
    return multiplier

# Lambda approach doing the exact same thing
make_multiplier_lambda = lambda x: lambda n: n * x

# Test our code:
print("\n--- Step 5: Final Comparison ---")

# Setup our standard closures
std_doubler = make_multiplier_standard(2)
std_tripler = make_multiplier_standard(3)

# Setup our lambda closures
lmb_doubler = make_multiplier_lambda(2)
lmb_tripler = make_multiplier_lambda(3)

print("Standard Closure Approach:")
print(f"  Double 10: {std_doubler(10)}")
# Expected output: Double 10: 20
print(f"  Triple 10: {std_tripler(10)}")
# Expected output: Triple 10: 30

print("\nLambda Closure Approach:")
print(f"  Double 10: {lmb_doubler(10)}")
# Expected output: Double 10: 20
print(f"  Triple 10: {lmb_tripler(10)}")
# Expected output: Triple 10: 30

# What we accomplished in this step:
# - We organized both approaches into a clean, comparative script.
# - We demonstrated that functional programming concepts can be written verbosely for clarity, or concisely for brevity.


# CONGRATULATIONS! 🎉
# You've just leveled up to expert-level Python functions!
# You learned about higher-order functions (functions that create functions), 
# closures (functions that remember data from their parent's scope), and 
# lambdas (anonymous, inline functions). These concepts are the foundation of 
# functional programming and are heavily used in advanced Python development, 
# particularly when writing decorators or dealing with asynchronous events.
# Remember: The best way to learn is by doing! 🚀
