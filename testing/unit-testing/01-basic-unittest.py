"""Question: Write unit tests for a simple add function using the unittest module. Include tests for normal addition, negative numbers, and zero values."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
# 
# Tips for success:
# - Import the `unittest` module at the top of your file.
# - Create a class that inherits from `unittest.TestCase`.
# - Write methods inside that class that start with `test_` (e.g., `test_add_positive_numbers`).
# - Use assertion methods like `self.assertEqual(actual, expected)` to verify the output.
# 
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - First write the function you want to test (e.g., `def add(a, b): return a + b`).
# - Create a test class that inherits from `unittest.TestCase`.
# - Each test method must start with `test_` so the test runner can find it.
# - Use `self.assertEqual(actual, expected)` to check if the function behaves correctly.
# - Run the tests with `unittest.main()` at the bottom of the script.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by writing the actual function we want to test. 
# It is a very simple `add` function that takes two arguments and returns their sum.
# In a real project, this function might be in a different file, but we will keep it here for simplicity.

def add(a, b):
    return a + b

# What we accomplished in this step:
# - Created the target function that our unit tests will evaluate.


# Step 2
# Explanation: Now we will set up our testing environment. We need to import the `unittest` module 
# and create a class that inherits from `unittest.TestCase`. We will write a basic test method. 
# For now, we will just call our function and print the result manually without using assertions, 
# just to make sure our test class can access the function.

import unittest

def add(a, b):
    return a + b

class TestMathOperations(unittest.TestCase):
    
    def test_basic_addition(self):
        result = add(2, 3)
        print(f"Manual check: 2 + 3 = {result}")

# What we accomplished in this step:
# - Imported the `unittest` module.
# - Created a test class inheriting from `TestCase`.
# - Wrote a method starting with `test_` so the test runner can discover it.


# Step 3
# Explanation: Printing results and manually checking them defeats the purpose of automated testing! 
# We need the computer to check the result for us. We will replace the print statement with 
# `self.assertEqual(actual, expected)`. If the two values match, the test passes silently. 
# If they don't, the test fails and alerts us.

import unittest

def add(a, b):
    return a + b

class TestMathOperations(unittest.TestCase):
    
    def test_basic_addition(self):
        # We call the function and check if the result equals 5
        self.assertEqual(add(2, 3), 5)

# What we accomplished in this step:
# - Replaced manual inspection with an automated assertion.
# - Used `self.assertEqual` to verify the function's output.


# Step 4
# Explanation: A good test suite covers multiple scenarios, including edge cases. 
# Let's add more test methods to ensure our `add` function works correctly with 
# negative numbers and zeroes. Remember, every method name must start with `test_`.

import unittest

def add(a, b):
    return a + b

class TestMathOperations(unittest.TestCase):
    
    def test_basic_addition(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative_addition(self):
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-5, 10), 5)

    def test_zero_addition(self):
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(0, 0), 0)

# What we accomplished in this step:
# - Expanded our test coverage to include negative numbers and zeroes.
# - Demonstrated that a single test class can hold multiple test methods.


# Step 5
# Explanation: Right now, if we run the script, nothing happens because we haven't told Python 
# to execute the tests! We need to add `unittest.main()` at the very bottom of our script. 
# This command tells the test runner to look for any class inheriting from `TestCase`, find all 
# methods starting with `test_`, and run them.

import unittest

def add(a, b):
    return a + b

class TestMathOperations(unittest.TestCase):
    
    def test_basic_addition(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative_addition(self):
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-5, 10), 5)

    def test_zero_addition(self):
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(0, 0), 0)

if __name__ == '__main__':
    # We pass exit=False here just so it runs smoothly in all environments (like Jupyter or specific IDEs)
    unittest.main(exit=False)

# What we accomplished in this step:
# - Added the standard `if __name__ == '__main__':` block.
# - Called `unittest.main()` to execute the test suite automatically.


# Step 6
# Explanation: For our final step, let's consolidate the code and add comments showing the expected 
# output. When the tests pass, `unittest` outputs a dot `.` for each passing test, followed by an "OK".

import unittest

def add(a, b):
    """Adds two numbers together."""
    return a + b

class TestMathOperations(unittest.TestCase):
    """Test suite for math operations."""
    
    def test_basic_addition(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(100, 200), 300)

    def test_negative_addition(self):
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-5, 10), 5)

    def test_zero_addition(self):
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(0, 0), 0)

# Test our code by running this script:
if __name__ == '__main__':
    print("Running unit tests...\n")
    unittest.main(exit=False)
    
# Expected output:
# Running unit tests...
#
# ...
# ----------------------------------------------------------------------
# Ran 3 tests in 0.001s
# 
# OK

# What we accomplished in this step:
# - Created a complete, professional, and well-documented unit test script.
# - Formatted the expected output so you know exactly what a passing test suite looks like.


# CONGRATULATIONS! 🎉
# You have successfully written and executed your first automated unit tests in Python!
# 
# Key takeaways:
# - The `unittest` module is built into Python, meaning you can start testing immediately without installing anything.
# - Test classes must inherit from `unittest.TestCase`.
# - Test methods MUST start with the word `test_`. If they don't, the test runner will ignore them!
# - Assertions (like `self.assertEqual`, `self.assertTrue`, etc.) are how you tell the computer to automatically verify the results.
# - `unittest.main()` is the trigger that runs the whole suite.
# 
# Keep experimenting! Try intentionally breaking the `add` function (e.g., `return a - b`) and run the 
# script again to see what a failing test output looks like!
# 
# Remember: The best way to learn is by doing! 🚀
