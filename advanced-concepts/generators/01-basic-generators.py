"""Question: Create a generator function that yields the Fibonacci sequence up to a given limit. Use it to print the first 10 Fibonacci numbers."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
# 
# Tips for success:
# - Understand the difference between `return` (which ends a function) and `yield` (which pauses it).
# - Use a loop inside your generator to continuously calculate the next Fibonacci number.
# - Remember that you must iterate over the generator (like using a `for` loop) to actually extract the values.
# 
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Use `yield` instead of `return` to produce a value without ending the function.
# - Keep track of the current and next Fibonacci numbers in variables (e.g., `a, b = 0, 1`).
# - You can iterate over the generator with a `for` loop or `next()`.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by writing a regular function that returns a list of Fibonacci 
# numbers. This is how we traditionally solve the problem. We calculate all the numbers, 
# store them in a list in our computer's memory, and then return the entire list at once.

def fibonacci_list(max_count):
    sequence = []
    a, b = 0, 1
    for _ in range(max_count):
        sequence.append(a)
        a, b = b, a + b
    return sequence

result = fibonacci_list(5)
print(f"List result: {result}")

# What we accomplished in this step:
# - Wrote a standard function to generate the sequence.
# - Stored all values in a list before returning them (which uses memory).


# Step 2
# Explanation: Now, let's convert that function into a generator. We do this simply by 
# replacing the list and `return` statement with the `yield` keyword. When Python sees `yield`, 
# it knows this is a generator. Instead of calculating everything at once, it yields one 
# number, pauses its execution, and waits to be asked for the next number.

def fibonacci_list(max_count):
    sequence = []
    a, b = 0, 1
    for _ in range(max_count):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def fibonacci_generator(max_count):
    a, b = 0, 1
    for _ in range(max_count):
        yield a
        a, b = b, a + b

print("Generator result using a for loop:")
for number in fibonacci_generator(5):
    print(number)

# What we accomplished in this step:
# - Created our first generator using the `yield` keyword.
# - Avoided storing the entire sequence in memory.
# - Showed how to easily iterate through the generated values using a `for` loop.


# Step 3
# Explanation: A `for` loop hides a bit of the magic. To really see how a generator 
# pauses and resumes, let's manually fetch values from it using the built-in `next()` function. 
# Notice how the generator "remembers" the values of `a` and `b` between each call to `next()`.

def fibonacci_list(max_count):
    sequence = []
    a, b = 0, 1
    for _ in range(max_count):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def fibonacci_generator(max_count):
    a, b = 0, 1
    for _ in range(max_count):
        yield a
        a, b = b, a + b

print("Manual generation using next():")
gen = fibonacci_generator(3)
print(next(gen))  # Runs until the first yield, then pauses
print(next(gen))  # Resumes, runs the loop again until the next yield
print(next(gen))  # Resumes, runs one last time

# What we accomplished in this step:
# - Used the `next()` function to manually advance the generator.
# - Demonstrated that local variables (`a` and `b`) retain their state between yields.


# Step 4
# Explanation: Writing a full function with `yield` is great for complex logic, but Python 
# also offers a shorthand for simple generators called a "generator expression." It looks 
# almost exactly like a list comprehension, but it uses parentheses `()` instead of square 
# brackets `[]`. Let's create a quick one to generate squares of numbers.

def fibonacci_list(max_count):
    sequence = []
    a, b = 0, 1
    for _ in range(max_count):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def fibonacci_generator(max_count):
    a, b = 0, 1
    for _ in range(max_count):
        yield a
        a, b = b, a + b

# Generator expression for squares
squares_gen = (x * x for x in range(1, 4))

print("Generator expression results:")
print(next(squares_gen))
print(next(squares_gen))
print(next(squares_gen))

# What we accomplished in this step:
# - Learned the syntax for generator expressions `(...)`.
# - Saw how we can create lazy-evaluated sequences in a single line of code.


# Step 5
# Explanation: For our final step, let's consolidate our code into a clean, professional 
# demonstration. We will remove the old list function and focus entirely on our generators, 
# printing our required 10 Fibonacci numbers and formatting the expected output as comments.

def fibonacci_generator(max_count):
    """Yields the Fibonacci sequence up to max_count elements."""
    a, b = 0, 1
    for _ in range(max_count):
        yield a
        a, b = b, a + b

# Test our code:
print("--- 1. Fibonacci Generator (First 10) ---")
for num in fibonacci_generator(10):
    print(num, end=" ")
# Expected output: 0 1 1 2 3 5 8 13 21 34
print("\n")


print("--- 2. Manual iteration with next() ---")
fib_gen = fibonacci_generator(3)
print(f"First value: {next(fib_gen)}")   # Expected output: First value: 0
print(f"Second value: {next(fib_gen)}")  # Expected output: Second value: 1
print(f"Third value: {next(fib_gen)}")   # Expected output: Third value: 1
print()


print("--- 3. Generator Expression ---")
# Generates cubes of numbers from 1 to 3
cubes_gen = (x ** 3 for x in range(1, 4))
for cube in cubes_gen:
    print(cube, end=" ")
# Expected output: 1 8 27
print("\n")

# What we accomplished in this step:
# - Organized our work into a clean test block.
# - Met the original requirement of printing the first 10 Fibonacci numbers.
# - Documented the expected behavior for easy verification.


# CONGRATULATIONS! 🎉
# You have successfully mastered Python generators!
# 
# Key takeaways:
# - Generators are incredibly memory-efficient. Because they only produce one item at a time 
#   (lazy evaluation), you can use them to process millions of items without crashing your computer.
# - The `yield` keyword is the heart of a generator function. It hands a value back to the caller 
#   but keeps the function alive, retaining its state for the next call.
# - You can advance a generator manually using the `next()` function, or automatically using a `for` loop.
# - Generator expressions `(...)` offer a fast, readable way to create simple generators on the fly.
# 
# Keep experimenting! Try modifying the generator to run forever (using `while True:`) 
# and use a `break` statement in your `for` loop to stop it when it reaches a certain value.
# 
# Remember: The best way to learn is by doing! 🚀
