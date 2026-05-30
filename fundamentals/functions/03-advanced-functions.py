"""Question: Write a recursive function that calculates the factorial of a number. Then, write an iterative version of the same function. Compare the two approaches by calculating the factorial of a few numbers and discussing the base case in recursion."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Identify the base case for recursion (when should the function stop calling itself?).
# - Think about the relationship between `n!` and `(n-1)!`.
# - For the iterative version, think about how to use a loop to accumulate the result.
#
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - For the recursive function: the factorial of 0 is 1 (base case). Otherwise, return `n * factorial(n-1)`.
# - For the iterative function: initialize a result to 1, then use a `for` loop from 1 to n, multiplying the result by each number.
# - Be careful with negative numbers – handle them by returning a message or raising an error.
# - Test with numbers like 0, 1, 5, and 10 to verify both versions return the same results.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by writing the iterative version of our factorial function. 
# "Iterative" simply means we will use a loop. We initialize a result variable to 1, 
# then loop from 1 up to (and including) our number `n`, multiplying the result by 
# each step.

def factorial_iterative(n):
    result = 1
    # We use n + 1 because the range function stops before the second argument
    for i in range(1, n + 1):
        result = result * i
    return result

print("--- Step 1: Iterative Factorial ---")
print(f"Iterative factorial of 5: {factorial_iterative(5)}")
print(f"Iterative factorial of 0: {factorial_iterative(0)}")

# What we accomplished in this step:
# - We wrote a standard iterative function using a `for` loop.
# - We verified that it correctly handles standard positive integers and 0.


# Step 2
# Explanation: Now we'll add the recursive version. A recursive function is one that 
# calls itself. Every recursive function must have a "base case" to stop the loop, 
# otherwise it will run forever (causing a RecursionError). For factorials, the base 
# case is when `n` is 0. If it's not 0, we multiply `n` by the factorial of `n - 1`.

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

def factorial_recursive(n):
    # Base case: stop calling ourselves when n reaches 0
    if n == 0:
        return 1
    
    # Recursive case: n * (n-1)!
    return n * factorial_recursive(n - 1)

print("\n--- Step 2: Recursive Factorial ---")
print(f"Recursive factorial of 5: {factorial_recursive(5)}")
print(f"Recursive factorial of 0: {factorial_recursive(0)}")

# What we accomplished in this step:
# - We built a recursive function by identifying the base case (n == 0).
# - We successfully used function self-invocation to calculate the result.


# Step 3
# Explanation: What happens if a user passes a negative number? Factorials are only 
# defined for non-negative integers. Our iterative loop would just return 1, and our 
# recursive function would run forever trying to reach 0! Let's add input validation 
# to both functions to raise a ValueError if `n` is negative.

def factorial_iterative(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
        
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

def factorial_recursive(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
        
    if n == 0:
        return 1
        
    return n * factorial_recursive(n - 1)

print("\n--- Step 3: Input Validation ---")
try:
    factorial_recursive(-3)
except ValueError as error:
    print(f"Successfully caught error: {error}")

# What we accomplished in this step:
# - We protected both functions against invalid (negative) inputs.
# - We safely prevented our recursive function from entering an infinite loop.


# Step 4
# Explanation: Let's create a comparison table. We will loop through a range of 
# numbers and print the results from both functions side-by-side. This proves that 
# while the underlying logic (iteration vs recursion) is completely different, the 
# mathematical outputs are identical.

def factorial_iterative(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)

print("\n--- Step 4: Comparison Table ---")
print("n  | Iterative | Recursive")
print("-" * 28)
for num in range(6):
    iter_val = factorial_iterative(num)
    rec_val = factorial_recursive(num)
    print(f"{num}  | {iter_val:<9} | {rec_val}")

# What we accomplished in this step:
# - We visually compared the two approaches over multiple test cases.
# - We formatted the output cleanly to verify they produce identical results.


# Step 5
# Explanation: We'll wrap everything into a final, clean script. We'll add docstrings 
# to our functions explaining their approach, and we'll create a dedicated test block 
# at the bottom with expected outputs clearly labeled in the comments.

def factorial_iterative(n):
    """
    Calculate factorial iteratively using a loop.
    Returns n! for n >= 0. Raises ValueError for negative inputs.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    """
    Calculate factorial recursively using function self-invocation.
    Returns n! for n >= 0. Raises ValueError for negative inputs.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    # Base case
    if n == 0:
        return 1
        
    # Recursive case
    return n * factorial_recursive(n - 1)


# Test our functions:
print("\n--- Step 5: Final Demonstration ---")

test_numbers = [0, 1, 4, 7]

print("Comparing Iterative vs Recursive approaches:\n")
for number in test_numbers:
    iter_result = factorial_iterative(number)
    rec_result = factorial_recursive(number)
    
    print(f"Factorial of {number}:")
    print(f"  Iterative -> {iter_result}")
    print(f"  Recursive -> {rec_result}")
    print(f"  Match?    -> {iter_result == rec_result}\n")

# Expected output:
# Comparing Iterative vs Recursive approaches:
#
# Factorial of 0:
#   Iterative -> 1
#   Recursive -> 1
#   Match?    -> True
#
# Factorial of 1:
#   Iterative -> 1
#   Recursive -> 1
#   Match?    -> True
#
# Factorial of 4:
#   Iterative -> 24
#   Recursive -> 24
#   Match?    -> True
#
# Factorial of 7:
#   Iterative -> 5040
#   Recursive -> 5040
#   Match?    -> True

# What we accomplished in this step:
# - We finalized both functions with professional docstrings.
# - We ran a definitive automated test loop comparing the two methodologies.


# CONGRATULATIONS! 🎉
# You've unlocked one of the most mind-bending concepts in computer science: Recursion!
# You learned that recursive functions call themselves, and that a solid "base case" 
# is absolutely critical to prevent infinite loops. You also saw that iterative 
# (loop-based) and recursive approaches can often solve the exact same problem.
# Recursion is incredibly powerful when dealing with tree structures or traversing 
# file directories. Keep practicing!
# Remember: The best way to learn is by doing! 🚀
