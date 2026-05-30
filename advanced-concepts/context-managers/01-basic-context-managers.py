"""Question: Create a custom context manager class that measures and prints the execution time of a code block. Use it to time a loop that calculates the sum of numbers from 1 to N."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
# 
# Tips for success:
# - A context manager class requires two special magic methods: `__enter__` and `__exit__`.
# - You will need the `time` module to capture the start and end times.
# - The `with` statement will automatically call `__enter__` at the start of the block and `__exit__` at the end.
# 
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - A context manager class needs `__enter__` (called at the start of the `with` block) and `__exit__` (called at the end).
# - Record the start time in `__enter__` and return the object (usually `self`).
# - Calculate and print the elapsed time in `__exit__`.
# - Use the `with` statement to automatically trigger the setup and teardown.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by writing the actual code block that we want to measure. 
# We'll write a simple loop that sums numbers from 1 to 1,000,000. 
# We won't worry about timing it just yet; we just want to make sure the logic works.

total = 0
for i in range(1, 1000001):
    total += i

print(f"The sum is: {total}")

# What we accomplished in this step:
# - Created the workload (a busy loop) that we want to analyze.
# - Verified the logic executes successfully.


# Step 2
# Explanation: Now let's manually time this code block. We will import the `time` module, 
# record the time right before the loop starts, and record it again right after the loop finishes. 
# By subtracting the start time from the end time, we get the elapsed time.

import time

start_time = time.time()

total = 0
for i in range(1, 1000001):
    total += i

end_time = time.time()
elapsed = end_time - start_time

print(f"The sum is: {total}")
print(f"Execution took {elapsed:.4f} seconds.")

# What we accomplished in this step:
# - Manually instrumented our code to calculate execution time.
# - Printed the formatted elapsed time to the console.


# Step 3
# Explanation: Manually adding start and end time variables every time we want to measure 
# something is tedious. Python provides the `with` statement to handle "setup" and "teardown" 
# logic automatically. To use it, we create a class with an `__enter__` method (for setup) 
# and an `__exit__` method (for teardown). Let's build our `Timer` class.

import time

class Timer:
    def __enter__(self):
        # Setup phase: Record the start time when the 'with' block begins
        self.start_time = time.time()
        return self  # It is standard practice to return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Teardown phase: Record the end time when the 'with' block ends
        self.end_time = time.time()
        elapsed = self.end_time - self.start_time
        print(f"Execution took {elapsed:.4f} seconds.")

# What we accomplished in this step:
# - Defined a custom context manager class.
# - Implemented `__enter__` to handle the setup (starting the clock).
# - Implemented `__exit__` to handle the teardown (stopping the clock and printing).


# Step 4
# Explanation: Now we can use our custom `Timer` context manager. By placing our busy loop 
# inside a `with Timer():` block, Python will automatically call `__enter__` before the loop, 
# and `__exit__` after the loop finishes. This keeps our actual business logic incredibly clean!

import time

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        elapsed = self.end_time - self.start_time
        print(f"Execution took {elapsed:.4f} seconds.")

print("Starting the timed block...")

with Timer():
    total = 0
    for i in range(1, 1000001):
        total += i
    print(f"The sum is: {total}")

print("Timed block finished.")

# What we accomplished in this step:
# - Applied our custom context manager using the `with` statement.
# - Separated the timing logic completely from the calculation logic.


# Step 5
# Explanation: What happens if an error occurs inside the `with` block? The true power of 
# a context manager is that `__exit__` is *guaranteed* to run, even if an exception is raised! 
# The parameters `exc_type`, `exc_value`, and `traceback` in `__exit__` will contain information 
# about the error. Let's add a custom name parameter to our Timer to make it more useful, 
# and briefly show how it handles errors gracefully.

import time

class Timer:
    def __init__(self, description="Block"):
        self.description = description

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        elapsed = self.end_time - self.start_time
        
        if exc_type is not None:
            print(f"[{self.description}] failed with an error, but still ran for {elapsed:.4f} seconds.")
            return False  # Returning False lets the exception propagate normally
        else:
            print(f"[{self.description}] completed successfully in {elapsed:.4f} seconds.")

# What we accomplished in this step:
# - Added an `__init__` method to accept a description string.
# - Added basic exception handling inside `__exit__` to prove it runs even on failure.


# Step 6
# Explanation: For our final step, let's consolidate everything into a clean demonstration script. 
# We will use our `Timer` context manager to time two different code blocks to show how reusable 
# it is. We will include expected output comments to clearly show what the script does.

import time

class Timer:
    """A context manager that times the execution of a code block."""
    def __init__(self, description="Task"):
        self.description = description

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        elapsed = self.end_time - self.start_time
        print(f"[Timer] {self.description} took {elapsed:.4f} seconds.")
        # We return None (implicitly), which propagates any exceptions outward.

# Test our code:
print("--- Context Manager Demonstration ---")

# Block 1: Summing a million numbers
with Timer("Sum to 1 Million"):
    total_1 = 0
    for i in range(1, 1000001):
        total_1 += i
    print(f"Total 1: {total_1}")
# Expected output:
# Total 1: 500000500000
# [Timer] Sum to 1 Million took 0.0452 seconds. (Actual time will vary)


# Block 2: Summing five million numbers
with Timer("Sum to 5 Million"):
    total_2 = 0
    for i in range(1, 5000001):
        total_2 += i
    print(f"Total 2: {total_2}")
# Expected output:
# Total 2: 12500002500000
# [Timer] Sum to 5 Million took 0.2315 seconds. (Actual time will vary)

# What we accomplished in this step:
# - Created a professional, reusable context manager.
# - Timed multiple, distinct blocks of code effortlessly.
# - Documented the expected behavior for easy verification.


# CONGRATULATIONS! 🎉
# You have successfully built your own Python context manager!
# 
# Key takeaways:
# - The `with` statement is a powerful tool for abstracting away setup and teardown logic.
# - Any class that implements `__enter__` and `__exit__` can be used with `with` (this is called the Context Manager Protocol).
# - The `__exit__` method is guaranteed to run, making it perfect for closing files, releasing locks, closing database connections, or stopping timers, even if an error crashes your program!
# 
# Keep experimenting! Try adding an intentional error (like `1 / 0`) inside one of the `with` blocks 
# and watch how the `__exit__` timer message still prints before the program crashes.
# 
# Remember: The best way to learn is by doing! 🚀
