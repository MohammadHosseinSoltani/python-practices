"""Question: Use unittest.mock to replace a function that fetches data from an external API with a mock that returns predictable test data. Test that your code handles the mocked response correctly."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
# 
# Tips for success:
# - Look up the `unittest.mock.patch` decorator and understand how it replaces objects during tests.
# - Remember that when you patch a function, it gets replaced by a `MagicMock` object.
# - You can control what the mock returns by setting its `return_value` attribute.
# - You can make the mock raise errors or return a sequence of values by setting its `side_effect` attribute.
# 
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - First write the function that normally calls the external dependency (simulated with `time.sleep` or similar).
# - Use `from unittest.mock import patch`.
# - Apply the `@patch('module.function')` decorator to replace the dependency during the test.
# - Set `mock_function.return_value` to the fake data you want returned.
# - Check that your code processes the mocked data correctly with assertions.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by writing our "production" code. We will simulate a function 
# called `fetch_user_from_db` that takes 2 seconds to run (simulating a slow database or API). 
# Then, we will write a `greet_user` function that depends on this slow function to get a user's name.

import time

def fetch_user_from_db(user_id):
    """Simulates a slow database query."""
    print(f"Connecting to database for user {user_id}...")
    time.sleep(2)  # Simulates network delay
    return {"id": user_id, "name": "Real User"}

def greet_user(user_id):
    """Business logic that relies on the slow database."""
    user_data = fetch_user_from_db(user_id)
    return f"Hello, {user_data['name']}!"

# What we accomplished in this step:
# - Created a slow dependency (`fetch_user_from_db`).
# - Created a function we actually want to test (`greet_user`) that depends on the slow code.


# Step 2
# Explanation: If we test `greet_user` normally, the test will take 2 seconds to run. 
# Imagine if we had 500 tests like this—our test suite would take 16 minutes! 
# Let's write a standard test using `unittest` to prove it works, but notice how slow it is.

import time
import unittest

def fetch_user_from_db(user_id):
    print(f"\nConnecting to database for user {user_id}...")
    time.sleep(2)
    return {"id": user_id, "name": "Real User"}

def greet_user(user_id):
    user_data = fetch_user_from_db(user_id)
    return f"Hello, {user_data['name']}!"

class TestUserService(unittest.TestCase):
    
    def test_greet_user_slow(self):
        # This works, but it waits 2 seconds every time.
        result = greet_user(101)
        self.assertEqual(result, "Hello, Real User!")

# What we accomplished in this step:
# - Wrote a standard unit test.
# - Identified the problem: un-mocked dependencies make tests slow and unreliable (what if the DB is down?).


# Step 3
# Explanation: Now we will use `unittest.mock.patch`. The `@patch` decorator intercepts 
# the call to `fetch_user_from_db` and replaces it with a fake "Mock" object during the test. 
# We tell the mock exactly what to return using `.return_value`. Because the real function 
# is never called, the test runs instantly!

import time
import unittest
from unittest.mock import patch

def fetch_user_from_db(user_id):
    print(f"\nConnecting to database for user {user_id}...")
    time.sleep(2)
    return {"id": user_id, "name": "Real User"}

def greet_user(user_id):
    user_data = fetch_user_from_db(user_id)
    return f"Hello, {user_data['name']}!"

class TestUserService(unittest.TestCase):
    
    # We patch the function where it is USED.
    # The string path must match the module where the function lives.
    # Since it's in this same file (usually '__main__'), we patch it here.
    @patch('__main__.fetch_user_from_db')
    def test_greet_user_fast(self, mock_fetch):
        # Configure the mock to return fake data instantly
        mock_fetch.return_value = {"id": 999, "name": "Mocked Alice"}
        
        result = greet_user(999)
        
        # Verify our business logic processed the mocked data correctly
        self.assertEqual(result, "Hello, Mocked Alice!")
        # We can also verify the mock was actually called!
        mock_fetch.assert_called_once_with(999)

# What we accomplished in this step:
# - Imported and used `@patch`.
# - Passed the mock object as an argument (`mock_fetch`) to the test method.
# - Used `.return_value` to bypass the `time.sleep()`.
# - Used `assert_called_once_with()` to ensure our code communicated with the dependency correctly.


# Step 4
# Explanation: Sometimes returning a simple value isn't enough. What if we want to test 
# how our code handles an error? Or what if the function is called twice and we want 
# different answers each time? We use `side_effect` instead of `return_value` for this.

import time
import unittest
from unittest.mock import patch

def fetch_user_from_db(user_id):
    time.sleep(2)
    return {"id": user_id, "name": "Real User"}

def greet_user(user_id):
    try:
        user_data = fetch_user_from_db(user_id)
        return f"Hello, {user_data['name']}!"
    except ConnectionError:
        return "Database unavailable. Please try again later."

class TestUserService(unittest.TestCase):
    
    @patch('__main__.fetch_user_from_db')
    def test_greet_user_error_handling(self, mock_fetch):
        # We configure the mock to RAISE an exception instead of returning data
        mock_fetch.side_effect = ConnectionError("Timeout")
        
        result = greet_user(101)
        
        # Verify our try/except block handled the error correctly
        self.assertEqual(result, "Database unavailable. Please try again later.")

# What we accomplished in this step:
# - Handled exceptions in our business logic.
# - Used `mock.side_effect` to simulate a network failure or database crash during the test.


# Step 5
# Explanation: For our final step, let's consolidate everything into a clean demonstration. 
# We will include tests for both successful data fetching (using `return_value`) and 
# error handling (using `side_effect`). We will include the test runner block at the bottom.

import time
import unittest
from unittest.mock import patch

# --- Production Code ---
def fetch_user_from_db(user_id):
    """Simulates a slow database or API call."""
    time.sleep(2)  
    return {"id": user_id, "name": "Real User"}

def greet_user(user_id):
    """Business logic that relies on external data."""
    try:
        user_data = fetch_user_from_db(user_id)
        return f"Hello, {user_data['name']}!"
    except ConnectionError:
        return "Database unavailable. Please try again later."

# --- Test Code ---
class TestUserService(unittest.TestCase):
    """Test suite using mocks to isolate dependencies."""
    
    @patch('__main__.fetch_user_from_db')
    def test_greet_user_success(self, mock_fetch):
        # Setup the mock
        mock_fetch.return_value = {"id": 1, "name": "Mocked Alice"}
        
        # Execute the code under test
        result = greet_user(1)
        
        # Verify the outcome
        self.assertEqual(result, "Hello, Mocked Alice!")
        mock_fetch.assert_called_once_with(1)

    @patch('__main__.fetch_user_from_db')
    def test_greet_user_database_error(self, mock_fetch):
        # Setup the mock to simulate a crash
        mock_fetch.side_effect = ConnectionError("DB is down")
        
        # Execute the code under test
        result = greet_user(99)
        
        # Verify our error handling works
        self.assertEqual(result, "Database unavailable. Please try again later.")
        mock_fetch.assert_called_once_with(99)

# To run these tests: python 01-mock-examples.py
if __name__ == '__main__':
    print("Running mocked tests (Notice how they finish instantly!)...\n")
    unittest.main(exit=False)
    
# Expected output:
# Running mocked tests (Notice how they finish instantly!)...
# 
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s
# 
# OK

# What we accomplished in this step:
# - Created a professional test suite that tests both the "happy path" and the "sad path".
# - Ensured tests are lightning fast because the slow dependency is mocked out.


# CONGRATULATIONS! 🎉
# You have successfully learned how to use mocking to isolate your tests!
# 
# Key takeaways:
# - Mocks replace real dependencies, making tests faster and completely isolated from the network or database.
# - The `@patch` decorator passes a `MagicMock` object into your test function as an argument.
# - Use `return_value` when you want the mock to instantly hand back some fake data.
# - Use `side_effect` when you want the mock to raise an exception or return different values on consecutive calls.
# - Always use `assert_called_once_with()` to verify that your code interacted with the mock correctly!
# 
# Keep experimenting! Try passing a list to `side_effect` (e.g., `mock_fetch.side_effect = [{"name": "A"}, {"name": "B"}]`) 
# and call the function twice in the test to see how it returns the next item in the list each time.
# 
# Remember: The best way to learn is by doing! 🚀
