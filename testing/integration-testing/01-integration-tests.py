"""Question: Write an integration test that verifies a simple data storage system. The system should write user data to a file and read it back. Test that data written can be correctly retrieved after being saved."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
# 
# Tips for success:
# - Create the component functions first (e.g., save and load functions).
# - Write a test that calls both functions in sequence.
# - Use setup and teardown methods in your test class to cleanly manage test files.
# 
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Create a `save_user` function that writes a dictionary to a file in JSON format.
# - Create a `load_user` function that reads the JSON file back and returns the dictionary.
# - Use `import json`, `import os`, and `import tempfile` for clean test file management.
# - In your test, save some data, load it back, and assert it matches what you saved.
# - Use `setUp` and `tearDown` methods in your test class to create and clean up a temporary file.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: We will begin by importing the necessary modules and writing our core functions.
# We need a function to save a dictionary to a file as JSON, and another function to read it back.
# These represent the two components of our system that we eventually want to test together.

import json
import os

def save_user(filepath, user_data):
    """Saves user dictionary data to a JSON file."""
    with open(filepath, 'w') as f:
        json.dump(user_data, f)

def load_user(filepath):
    """Loads user dictionary data from a JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)

# What we accomplished in this step:
# - Imported `json` and `os` modules.
# - Created `save_user` to persist data.
# - Created `load_user` to retrieve data.


# Step 2
# Explanation: Before writing a formal integration test, it is often helpful to manually test
# that our two functions work together. We will create a small block of code to save a user, 
# load it, and print the results to verify everything functions as expected.

import json
import os

def save_user(filepath, user_data):
    """Saves user dictionary data to a JSON file."""
    with open(filepath, 'w') as f:
        json.dump(user_data, f)

def load_user(filepath):
    """Loads user dictionary data from a JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)

# Manual integration test
test_file = "manual_test.json"
original_data = {"id": 1, "name": "Alice", "role": "admin"}

save_user(test_file, original_data)
loaded_data = load_user(test_file)

print(f"Original: {original_data}")
print(f"Loaded:   {loaded_data}")
print(f"Match?    {original_data == loaded_data}")

# Clean up our mess
if os.path.exists(test_file):
    os.remove(test_file)

# What we accomplished in this step:
# - Manually verified that `save_user` and `load_user` integrate correctly.
# - Confirmed that the dictionary loaded matches the dictionary saved.
# - Cleaned up the file after verifying the result.


# Step 3
# Explanation: Now let's turn our manual test into an automated integration test using `unittest`.
# We will create a test class and write a basic test method that calls both functions and 
# uses assertions to guarantee the data matches.

import json
import os
import unittest

def save_user(filepath, user_data):
    """Saves user dictionary data to a JSON file."""
    with open(filepath, 'w') as f:
        json.dump(user_data, f)

def load_user(filepath):
    """Loads user dictionary data from a JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)

class TestUserStorageIntegration(unittest.TestCase):
    def test_save_and_load_user(self):
        # Hardcoded test file for this simple automated test
        test_file = "basic_test.json"
        user_data = {"id": 2, "name": "Bob", "role": "user"}
        
        # Integration: calling save then load in sequence
        save_user(test_file, user_data)
        result = load_user(test_file)
        
        # Verify the components worked together successfully
        self.assertEqual(user_data, result)
        
        # Manual cleanup inside the test
        if os.path.exists(test_file):
            os.remove(test_file)

# What we accomplished in this step:
# - Imported `unittest`.
# - Created a `TestCase` class with an integration test.
# - Replaced manual `print` statements with `self.assertEqual`.


# Step 4
# Explanation: Our previous test had a flaw: if the test failed at `self.assertEqual`, the code 
# execution would stop, and the cleanup step would never run, leaving a test file behind. 
# To fix this, we will use `unittest`'s `setUp` and `tearDown` methods, along with `tempfile`, 
# to ensure our test environment is created securely and always cleaned up, even if tests fail.

import json
import os
import unittest
import tempfile

def save_user(filepath, user_data):
    """Saves user dictionary data to a JSON file."""
    with open(filepath, 'w') as f:
        json.dump(user_data, f)

def load_user(filepath):
    """Loads user dictionary data from a JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)

class TestUserStorageIntegration(unittest.TestCase):
    def setUp(self):
        # Create a unique temporary file
        self.fd, self.test_file = tempfile.mkstemp(suffix=".json")
        # Close the file descriptor so our functions can safely open the file
        os.close(self.fd)

    def tearDown(self):
        # This will ALWAYS run, even if the test fails
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_and_load_user(self):
        user_data = {"id": 3, "name": "Charlie", "role": "manager"}
        
        # Perform the integration actions
        save_user(self.test_file, user_data)
        result = load_user(self.test_file)
        
        # Assert the data remained intact
        self.assertEqual(user_data, result)

# What we accomplished in this step:
# - Introduced the `tempfile` module to generate safe, unique temporary filenames.
# - Added `setUp` to prepare the test environment before every test.
# - Added `tearDown` to guarantee cleanup after every test, preventing left-over files.


# Step 5
# Explanation: Finally, we will consolidate everything into a clean demonstration script.
# We include the test runner block at the bottom so the file can be executed directly from the
# command line to run our test suite.

import json
import os
import unittest
import tempfile

def save_user(filepath, user_data):
    """Saves user dictionary data to a JSON file."""
    with open(filepath, 'w') as f:
        json.dump(user_data, f)

def load_user(filepath):
    """Loads user dictionary data from a JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)

class TestUserStorageIntegration(unittest.TestCase):
    def setUp(self):
        """Prepares a temporary file for testing."""
        self.fd, self.test_file = tempfile.mkstemp(suffix=".json")
        os.close(self.fd)

    def tearDown(self):
        """Cleans up the temporary file after the test completes."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_and_load_user_integration(self):
        """
        Integration Test: 
        Verifies that save_user and load_user work correctly together.
        """
        user_data = {"id": 4, "name": "Diana", "role": "developer"}
        
        # 1. Write the data using our save component
        save_user(self.test_file, user_data)
        
        # 2. Read the data using our load component
        result = load_user(self.test_file)
        
        # 3. Assert that the integration of both components preserved our data perfectly
        self.assertEqual(user_data, result)

# Test our class:
if __name__ == '__main__':
    unittest.main()

# Expected output:
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.001s
#
# OK

# What we accomplished in this step:
# - Added proper docstrings to our test methods for clarity.
# - Added the `unittest.main()` execution block to run the test suite.
# - Successfully created a robust, self-cleaning integration test.


# CONGRATULATIONS! 🎉
# You've successfully written a robust integration test! 
# 
# Key takeaways from this exercise:
# - Integration testing verifies how different components (saving and loading) interact together in the real world.
# - Using `setUp` and `tearDown` ensures your tests do not leave "garbage" files behind, making your test suite reliable.
# - The `tempfile` module is an essential tool for testing code that interacts with the file system.
# - JSON persistence can be easily tested by verifying dictionaries before and after file operations.
#
# Keep experimenting! Try adding error handling to the functions and testing what happens if a file doesn't exist.
# Remember: The best way to learn is by doing! 🚀
