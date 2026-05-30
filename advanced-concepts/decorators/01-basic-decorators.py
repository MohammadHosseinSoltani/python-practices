"""Question: Create a simple decorator that measures and prints the execution time of a function. Apply it to a function that calculates the sum of numbers from 1 to N."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
# 
# Tips for success:
# - Understand that a decorator is simply a function that takes another function as an input and returns a new function.
# - You will need to use the `time` module to record the start and end times.
# - Think about how to "wrap" the original function call inside a new function to add the timing behavior.
# 
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Define an outer function that takes a function as its argument.
# - Inside it, define a `wrapper` function that adds the timing logic and calls the original function.
# - Return the wrapper function.
# - Use `@your_decorator` syntax just above the function definition to apply it.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by writing the core function we want to measure. 
# We will write `sum_to_n(n)`, which calculates the sum of all numbers from 1 to N.
# We'll test it with a small number to ensure it works correctly before we worry about timing.

def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

result = sum_to_n(100)
print(f"Sum to 100 is: {result}")

# What we accomplished in this step:
# - Created a basic function that performs a measurable amount of work.
# - Verified that the logic of our function is sound.


# Step 2
# Explanation: Now we want to know how long this function takes to run. 
# Before using any advanced Python features like decorators, let's just do it manually. 
# We will import the `time` module, record the time right before the function call, 
# record it again right after, and subtract the two to find the elapsed time.

import time

def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Manually timing the function
start_time = time.time()
result = sum_to_n(1000000)
end_time = time.time()

execution_time = end_time - start_time
print(f"Sum to 1000000 is: {result}")
print(f"Execution time: {execution_time} seconds")

# What we accomplished in this step:
# - Used `time.time()` to measure execution time manually.
# - Calculated and printed the elapsed time for a large operation.


# Step 3
# Explanation: Manually adding start and end time around every function call is tedious. 
# What if we wrote a "helper" function that takes ANY function and its arguments, 
# runs the timing logic, and returns the result? This is our "proto-decorator".

import time

def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def manual_timer(func, n):
    start_time = time.time()
    result = func(n)  # Calling the passed-in function
    end_time = time.time()
    
    print(f"Execution time for {func.__name__}: {end_time - start_time} seconds")
    return result

# Using our helper function
result = manual_timer(sum_to_n, 1000000)
print(f"Result: {result}")

# What we accomplished in this step:
# - Passed a function as an argument to another function (using first-class functions).
# - Abstracted the timing logic away from the main execution flow.


# Step 4
# Explanation: The previous step required us to change how we call `sum_to_n`. 
# A true decorator allows us to call `sum_to_n(1000000)` normally, but still get the timing.
# To do this, we write a function that takes a function, defines a `wrapper` inside it 
# that handles the timing and arguments (using *args and **kwargs for maximum flexibility), 
# and then returns that wrapper function.

import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time for {func.__name__}: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Manually decorating our function
sum_to_n = timing_decorator(sum_to_n)

# Now we call it normally, but it's actually calling the wrapper!
result = sum_to_n(1000000)
print(f"Result: {result}")

# What we accomplished in this step:
# - Created a true decorator structure (a function returning a function).
# - Used *args and **kwargs so the wrapper can accept any number of arguments.
# - Proved that assigning the wrapper back to the original function name works.


# Step 5
# Explanation: Manually reassigning the function `sum_to_n = timing_decorator(sum_to_n)` 
# works, but Python gives us a beautiful shortcut: the `@` symbol. 
# By placing `@timing_decorator` directly above our function definition, 
# Python applies the wrapper automatically behind the scenes!

import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time for {func.__name__}: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# The function is already decorated, just call it!
result = sum_to_n(1000000)
print(f"Result: {result}")

# What we accomplished in this step:
# - Used the elegant `@` syntax (syntactic sugar) to apply our decorator.
# - Made the code much cleaner and more readable.


# Step 6
# Explanation: For our final step, let's consolidate everything into a clean script. 
# We have our reusable decorator, and our decorated function. 
# Let's call the function with an even larger N to see the decorator in action clearly.

import time

def timing_decorator(func):
    """A decorator that prints the execution time of the function it wraps."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"[Timer] {func.__name__} took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper

@timing_decorator
def sum_to_n(n):
    """Calculates the sum of numbers from 1 to n."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Test our code:
print("--- Testing Decorator ---")

final_result = sum_to_n(5000000)
# Expected output:
# [Timer] sum_to_n took 0.1542 seconds to execute. (Exact time will vary based on computer speed)

print(f"Final Result: {final_result}")
# Expected output:
# Final Result: 12500002500000

# What we accomplished in this step:
# - Created a professional, well-documented decorator.
# - Applied it to a function that does some heavy lifting.
# - Confirmed that the decorator intercepts the call, times it, and then passes the result back perfectly.


# CONGRATULATIONS! 🎉
# You have successfully built and applied your own custom Python decorator!
# 
# Key takeaways:
# - Decorators allow you to modify or enhance a function's behavior without changing its internal code.
# - They are built using "higher-order functions" (functions that accept and return other functions).
# - The `wrapper` function inside a decorator uses `*args` and `**kwargs` to flexibly accept any arguments the original function needs.
# - The `@` syntax is just a convenient, readable way to apply this wrapping behavior.
# 
# Keep experimenting! Try applying this `@timing_decorator` to other functions you've written, 
# or try creating a new decorator that simply prints "Function started!" and "Function finished!" 
# around a function call.
# 
# Remember: The best way to learn is by doing! 🚀
