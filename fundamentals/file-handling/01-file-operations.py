"""Question: Write a program that creates a text file, writes a few lines to it, reads the content back, and prints it. Use the `with` statement for safe file handling."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
# 
# Tips for success:
# - Remember that you need to open the file in write mode ('w') before you can write to it.
# - You must then open it in read mode ('r') to see what you wrote.
# - Always use the `with` statement when opening files; it automatically closes them for you, preventing memory leaks!
# 
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Use `open('filename.txt', 'w')` to create/write a file.
# - Use `open('filename.txt', 'r')` to read a file.
# - The `with` statement automatically closes the file for you.
# - Use `.write()` to add text and `.read()` to retrieve the entire content.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by creating a brand new text file and writing a single line to it. 
# We use the built-in `open()` function. The first argument is the filename, and the second 
# argument is the mode: 'w' stands for write. 
# Crucially, we use the `with` statement. This ensures that as soon as the indented block finishes, 
# Python automatically closes the file, saving the data safely to the hard drive.
file_name = "test_document.txt"

with open(file_name, "w") as file:
    file.write("Hello, this is our first line of text.\n")

# What we accomplished in this step:
# - Created a text file on our computer using the 'w' (write) mode.
# - Used the `with` block to ensure safe file handling.
# - Wrote a string to the file, including a newline character (`\n`).


# Step 2
# Explanation: Now we'll add more lines. Notice that when we open a file in 'w' mode, 
# it completely overwrites any existing file with that name. So, we will write our first 
# line again, followed by a couple of new ones.
file_name = "test_document.txt"

with open(file_name, "w") as file:
    file.write("Hello, this is our first line of text.\n")
    file.write("Learning file operations is very useful.\n")
    file.write("This is the third line.\n")

# What we accomplished in this step:
# - Called `.write()` multiple times to add several lines.
# - Used `\n` to ensure each sentence goes on its own line.


# Step 3
# Explanation: Writing data is only half the battle; we need to read it back! 
# We will use another `with` block, but this time we will open the file in 'r' (read) mode. 
# We'll use the `.read()` method, which grabs the entire contents of the file as one giant string.
file_name = "test_document.txt"

# Writing the file
with open(file_name, "w") as file:
    file.write("Hello, this is our first line of text.\n")
    file.write("Learning file operations is very useful.\n")
    file.write("This is the third line.\n")

# Reading the entire file
with open(file_name, "r") as file:
    entire_content = file.read()
    
print("--- Reading entire file at once ---")
print(entire_content)

# What we accomplished in this step:
# - Opened the file in 'r' (read) mode.
# - Read the entire file contents into a variable.
# - Printed the contents to the console.


# Step 4
# Explanation: Sometimes files are massive, and reading them all at once uses too much memory. 
# A safer, more common approach is to read the file line by line. We can do this easily by 
# treating the file object itself as an iterable in a `for` loop. 
# Note: we use `end=""` in our print statement because the line from the file already has a `\n` at the end!
file_name = "test_document.txt"

# Writing the file
with open(file_name, "w") as file:
    file.write("Hello, this is our first line of text.\n")
    file.write("Learning file operations is very useful.\n")
    file.write("This is the third line.\n")

# Reading the file line by line
print("--- Reading file line by line ---")
with open(file_name, "r") as file:
    for line in file:
        print(line, end="")

# What we accomplished in this step:
# - Looped directly over the file object to process it line by line.
# - Managed the extra newline characters using `end=""`.


# Step 5
# Explanation: What if we want to add data to an existing file without deleting what's already there? 
# We use 'a' (append) mode. Let's append a new line to our file, and then read the file 
# one last time to prove the old data and the new data are both there.
file_name = "test_document.txt"

# Initial writing (overwrites everything)
with open(file_name, "w") as file:
    file.write("Hello, this is our first line of text.\n")
    file.write("Learning file operations is very useful.\n")
    file.write("This is the third line.\n")

# Appending to the file
with open(file_name, "a") as file:
    file.write("This line was added using append mode!\n")

# Reading back the updated file
print("--- Reading after append ---")
with open(file_name, "r") as file:
    print(file.read())

# What we accomplished in this step:
# - Used the 'a' mode to safely add data to the end of an existing file.
# - Verified the change by reading the file again.


# Step 6
# Explanation: For our final step, let's consolidate everything into a clean demonstration script.
# We will create the file, read it, append to it, and read it again. 
# This represents a complete, professional workflow for basic file I/O.

# Test our code:
file_name = "test_document.txt"

print("Step A: Creating the file...")
with open(file_name, "w") as file:
    file.write("Line 1: Setup complete.\n")
    file.write("Line 2: Ready for processing.\n")

print("\nStep B: Reading file contents:")
with open(file_name, "r") as file:
    content = file.read()
    print(content, end="")  
    # Expected output: 
    # Line 1: Setup complete.
    # Line 2: Ready for processing.

print("\nStep C: Appending new data...")
with open(file_name, "a") as file:
    file.write("Line 3: Processing finished.\n")

print("\nStep D: Reading updated file line by line:")
with open(file_name, "r") as file:
    for line in file:
        print(line, end="")
        # Expected output:
        # Line 1: Setup complete.
        # Line 2: Ready for processing.
        # Line 3: Processing finished.

# What we accomplished in this step:
# - Combined all file operation modes ('w', 'r', 'a') into one cohesive script.
# - Displayed expected outputs to easily verify the program's success.


# CONGRATULATIONS! 🎉
# You have successfully learned how to interact with the file system using Python!
# 
# Key takeaways:
# - Always use the `with` statement to manage files safely; it handles closing them automatically!
# - Mode 'w' writes to a file, but will erase any existing content.
# - Mode 'a' appends to a file, keeping existing content safe.
# - Mode 'r' reads a file.
# - You can read a file all at once using `.read()`, or loop through it line-by-line using a `for` loop.
# 
# Keep experimenting! Try modifying the code to ask the user for input using `input()`, 
# and save their responses directly into a new text file.
# 
# Remember: The best way to learn is by doing! 🚀
