"""Question: Write a function that safely reads a text file and returns its content. The function should handle the file not being found, permission errors, and any other unexpected exceptions gracefully. If the file is missing, log the error to a separate 'error_log.txt' file (append mode) with a timestamp, and return an empty string."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Use `try/except` blocks to handle multiple exception types separately.
# - Import the `datetime` module to generate timestamps for your log entries.
# - Open your separate 'error_log.txt' file in append mode ('a') so you don't overwrite previous errors.
#
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Use `try/except FileNotFoundError` to catch a missing file.
# - Use `try/except PermissionError` to catch cases where the file exists but can't be read.
# - Use a bare `except Exception as e` to catch any other unexpected errors.
# - When logging, open 'error_log.txt' in append mode (`'a'`) and write the timestamp and error details.
# - Use `datetime.datetime.now()` to generate the timestamp.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by writing a basic function, `safe_read_file(filename)`, 
# that opens a file in read mode and returns its content. To prove it works, we will 
# temporarily create a small text file and read it back. We won't worry about handling 
# any errors just yet.

def safe_read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content

# Create a sample text file for testing
with open('sample_data.txt', 'w') as file:
    file.write("Hello, advanced file handling!")

# Read the file to make sure our function works
print("Step 1 Output:")
print(safe_read_file('sample_data.txt'))
print()

# What we accomplished in this step:
# - We defined a simple function to read file contents.
# - We tested it by generating and reading a valid text file.


# Step 2
# Explanation: What happens if the file doesn't exist? Our basic function would crash. 
# Now we'll add a `try/except FileNotFoundError` block. If the file is missing, we 
# will catch the exception, print a friendly message to the screen, and return an 
# empty string so the rest of our program can safely continue.

def safe_read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Oops! The file '{filename}' was not found.")
        return ""

with open('sample_data.txt', 'w') as file:
    file.write("Hello, advanced file handling!")

print("Step 2 Output:")
print("Reading valid file:")
print(safe_read_file('sample_data.txt'))

print("Reading missing file:")
content = safe_read_file('missing_file.txt')
print(f"Returned content: '{content}'")
print()

# What we accomplished in this step:
# - We introduced a `try/except` block specifically targeting `FileNotFoundError`.
# - We prevented the program from crashing when asked to read a non-existent file.


# Step 3
# Explanation: Sometimes a file exists, but our program doesn't have the operating 
# system permissions to read it. We can chain another `except` block specifically 
# for `PermissionError` to handle this scenario safely.

def safe_read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Oops! The file '{filename}' was not found.")
        return ""
    except PermissionError:
        print(f"Access denied! You don't have permission to read '{filename}'.")
        return ""

# (Testing is the same as above, but now we are protected against permission issues too)

# What we accomplished in this step:
# - We learned how to handle multiple, distinct exceptions in a single `try` block.
# - We added specific handling for permission-related errors.


# Step 4
# Explanation: Printing errors to the screen is fine for simple scripts, but professional 
# applications log errors to a file so developers can review them later. We will import 
# `datetime` and write a helper function, `log_error(message)`, that appends a 
# timestamped message to 'error_log.txt'.

import datetime

def log_error(message):
    # Generate a readable timestamp string
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Open the log file in append mode ('a') so we don't erase past logs
    with open('error_log.txt', 'a') as log_file:
        log_file.write(f"[{timestamp}] ERROR: {message}\n")

def safe_read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Oops! The file '{filename}' was not found.")
        return ""
    except PermissionError:
        print(f"Access denied! You don't have permission to read '{filename}'.")
        return ""

# What we accomplished in this step:
# - We imported the `datetime` module.
# - We created a reusable logging function that uses append mode ('a') to keep a running history.


# Step 5
# Explanation: Let's integrate everything. Instead of printing errors to the screen, 
# our `safe_read_file` function will call our new `log_error` helper. We will also 
# add a catch-all `except Exception as e` to log any other unpredictable errors. 
# Finally, we will demonstrate reading a valid file and a missing file, and show 
# what the log file looks like.

import datetime

def log_error(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('error_log.txt', 'a') as log_file:
        log_file.write(f"[{timestamp}] ERROR: {message}\n")

def safe_read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        log_error(f"File not found: '{filename}'")
        return ""
    except PermissionError:
        log_error(f"Permission denied: '{filename}'")
        return ""
    except Exception as e:
        # Catch-all for any other unexpected errors
        log_error(f"Unexpected error reading '{filename}': {e}")
        return ""

# Test our function:
if __name__ == "__main__":
    # Create a valid file to read
    with open('sample_data.txt', 'w') as file:
        file.write("Hello, robust file handling!")

    print("Attempting to read valid file...")
    valid_content = safe_read_file('sample_data.txt')
    print(f"Success! Content: {valid_content}")

    print("\nAttempting to read missing file...")
    missing_content = safe_read_file('does_not_exist.txt')
    print(f"Function returned: '{missing_content}' (Check error_log.txt for details)")

    # Read the log file to show what was recorded
    print("\n--- Contents of error_log.txt ---")
    with open('error_log.txt', 'r') as log_file:
        print(log_file.read().strip())
    print("---------------------------------")

    # Expected Output Example:
    # Attempting to read valid file...
    # Success! Content: Hello, robust file handling!
    #
    # Attempting to read missing file...
    # Function returned: '' (Check error_log.txt for details)
    #
    # --- Contents of error_log.txt ---
    # [2023-10-25 14:30:15] ERROR: File not found: 'does_not_exist.txt'
    # ---------------------------------

# What we accomplished in this step:
# - We integrated the error logger seamlessly into our file-reading logic.
# - We added a generic fallback exception handler to make the function completely crash-proof.
# - We demonstrated a full application flow with error tracking.

# ===============================================================================
# CONGRATULATIONS! 🎉
# You have successfully built a robust, professional-grade file reading utility! 
# By combining multiple exception handling blocks (`FileNotFoundError`, `PermissionError`, 
# and generic `Exception`), you ensured your program degrades gracefully instead of 
# abruptly crashing. You also learned how to implement a persistent error logging 
# system using file append mode and timestamps. These concepts are foundational to 
# writing reliable, production-ready code.
# Remember: The best way to learn is by doing! 🚀
