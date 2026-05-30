"""Question: Write tests for a function that checks if a string is a palindrome using pytest. Include tests for valid palindromes, non-palindromes, and empty strings."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
# 
# Tips for success:
# - Use simple `assert` statements instead of complex assertion methods.
# - Remember that all your test functions must start with `test_`.
# - Look into the `@pytest.mark.parametrize` decorator to easily test multiple cases without repeating code.
# 
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Write the `is_palindrome` function first.
# - pytest allows you to use plain `assert` statements instead of special assertion methods.
# - Test functions must start with `test_`.
# - Use `import pytest` and the `@pytest.mark.parametrize` decorator to test multiple inputs at once.
# - Run the tests by executing `pytest` in the terminal.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by writing the function we want to test. A palindrome is a word 
# that reads the same forwards and backwards (like "racecar"). We will write a simple 
# `is_palindrome` function that removes spaces and converts the string to lowercase before 
# checking if it equals its reverse.

def is_palindrome(text):
    clean_text = text.replace(" ", "").lower()
    return clean_text == clean_text[::-1]

# What we accomplished in this step:
# - Created the target function that we will be testing.
# - Used Python's slice notation `[::-1]` to easily reverse a string.


# Step 2
# Explanation: Now we will write our first test. The beauty of `pytest` is its simplicity. 
# We don't need to create a class or inherit from anything. We just write a function 
# that starts with `test_` and use Python's built-in `assert` keyword. If the condition 
# after `assert` is True, the test passes. If it is False, the test fails.

def is_palindrome(text):
    clean_text = text.replace(" ", "").lower()
    return clean_text == clean_text[::-1]

def test_valid_palindrome():
    # We simply assert that the function returns True for a known palindrome.
    assert is_palindrome("racecar") == True

# What we accomplished in this step:
# - Wrote our first basic `pytest` function.
# - Learned that `pytest` uses standard Python `assert` statements.


# Step 3
# Explanation: A robust test suite needs to cover various edge cases. Let's add more test 
# functions to check for non-palindromes, empty strings, and strings with capital letters 
# and spaces to ensure our cleaning logic works.

def is_palindrome(text):
    clean_text = text.replace(" ", "").lower()
    return clean_text == clean_text[::-1]

def test_valid_palindrome():
    assert is_palindrome("racecar") == True

def test_invalid_palindrome():
    assert is_palindrome("hello") == False

def test_empty_string():
    assert is_palindrome("") == True  # An empty string is technically a palindrome

def test_palindrome_with_spaces_and_capitals():
    assert is_palindrome("Taco Cat") == True

# What we accomplished in this step:
# - Expanded our test suite to cover multiple different scenarios.
# - Verified the internal cleaning logic (spaces and uppercase letters) of our function.


# Step 4
# Explanation: Writing a separate function for every single word is repetitive. `pytest` 
# offers an incredible feature called `parametrize`. By importing `pytest` and using the 
# `@pytest.mark.parametrize` decorator, we can define a list of inputs and expected outputs, 
# and `pytest` will run the same test function for every item in the list!

import pytest

def is_palindrome(text):
    clean_text = text.replace(" ", "").lower()
    return clean_text == clean_text[::-1]

# We define the variable names as a string, then provide a list of tuples with the data.
@pytest.mark.parametrize("test_input,expected_result", [
    ("racecar", True),
    ("hello", False),
    ("", True),
    ("Taco Cat", True),
    ("Python", False)
])
def test_is_palindrome_cases(test_input, expected_result):
    assert is_palindrome(test_input) == expected_result

# What we accomplished in this step:
# - Imported the `pytest` library to use its advanced features.
# - Refactored multiple test functions into a single, clean parametrized test.
# - Made our test suite much easier to scale in the future.


# Step 5
# Explanation: For our final step, let's consolidate everything into a clean script. 
# We will include comments showing exactly how to run this file from the terminal and 
# what the expected output looks like when `pytest` discovers and runs our tests successfully.

import pytest

def is_palindrome(text):
    """Checks if a given string reads the same forwards and backwards."""
    clean_text = text.replace(" ", "").lower()
    return clean_text == clean_text[::-1]

@pytest.mark.parametrize("test_input,expected_result", [
    ("madam", True),
    ("racecar", True),
    ("Taco Cat", True),
    ("hello", False),
    ("world", False),
    ("", True),
    ("a", True)
])
def test_is_palindrome(test_input, expected_result):
    """Tests the is_palindrome function against multiple inputs."""
    assert is_palindrome(test_input) == expected_result

# To run these tests, you do NOT run the script with 'python 01-pytest-basics.py'.
# Instead, you run pytest from your terminal:
# $ pytest 01-pytest-basics.py -v

# Expected output:
# ============================= test session starts ==============================
# collected 7 items
# 
# 01-pytest-basics.py::test_is_palindrome[madam-True] PASSED               [ 14%]
# 01-pytest-basics.py::test_is_palindrome[racecar-True] PASSED             [ 28%]
# 01-pytest-basics.py::test_is_palindrome[Taco Cat-True] PASSED            [ 42%]
# 01-pytest-basics.py::test_is_palindrome[hello-False] PASSED              [ 57%]
# 01-pytest-basics.py::test_is_palindrome[world-False] PASSED              [ 71%]
# 01-pytest-basics.py::test_is_palindrome[-True] PASSED                    [ 85%]
# 01-pytest-basics.py::test_is_palindrome[a-True] PASSED                   [100%]
# 
# ============================== 7 passed in 0.03s ===============================

# What we accomplished in this step:
# - Created a professional, highly readable `pytest` test suite.
# - Demonstrated how `pytest` automatically names each parametrized test run.
# - Provided clear instructions on how to execute the test runner.


# CONGRATULATIONS! 🎉
# You have successfully written and executed tests using pytest!
# 
# Key takeaways:
# - `pytest` is widely loved because it requires much less boilerplate code than `unittest`.
# - You simply write functions starting with `test_` and use standard Python `assert` statements.
# - The `@pytest.mark.parametrize` decorator is a game-changer for testing multiple inputs 
#   and edge cases without repeating your test logic.
# - To run `pytest`, you execute it directly from the command line, and it automatically discovers 
#   all your tests.
# 
# Keep experimenting! Try changing one of the expected results in the parametrize list to the 
# wrong boolean value, run `pytest` again, and see how beautifully it formats the error message!
# 
# Remember: The best way to learn is by doing! 🚀
