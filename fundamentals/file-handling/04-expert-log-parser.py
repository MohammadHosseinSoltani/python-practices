"""Question: Build a mini log parser. The program should read a given log file, extract all lines that contain the word 'ERROR', write those lines to a new file named 'errors_only.log', and print a summary that includes the total number of lines scanned and the number of errors found. If the input file does not exist, log the error to 'error_log.txt' and exit gracefully."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Open files securely using the `with` statement.
# - Iterate through the file line by line to keep memory usage low.
# - Use the `in` keyword to easily check if the substring 'ERROR' exists within a line.
# - Reuse the safe file reading and logging patterns you learned in the previous exercises.
#
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Read the input file line by line using a `for` loop: `for line in file:`.
# - Check if 'ERROR' is in the line with `if 'ERROR' in line:`.
# - Keep counters: `total_lines` and `error_count`.
# - Write matching lines to 'errors_only.log' immediately as you find them.
# - Wrap the file opening in `try/except` to handle a missing input file, and call `log_error()` if needed.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by creating a realistic scenario. We need a sample log 
# file to parse. We will write a small script to generate this file with a mix of 
# INFO, WARNING, and ERROR lines. Then, we will define the empty shell of our 
# parser function.

def create_sample_log():
    sample_data = """[2023-11-01 10:00:01] INFO: System started successfully.
[2023-11-01 10:05:12] WARNING: High memory usage detected.
[2023-11-01 10:12:45] ERROR: Database connection failed.
[2023-11-01 10:15:00] INFO: Retry attempt 1...
[2023-11-01 10:15:05] ERROR: Retry failed. System shutting down."""
    
    with open('server.log', 'w') as file:
        file.write(sample_data)

def parse_log(input_file):
    print(f"Preparing to parse: {input_file}")

# Test our initial setup
create_sample_log()
parse_log('server.log')

# What we accomplished in this step:
# - We generated a sample `server.log` file containing mixed severity messages.
# - We created the skeleton for our `parse_log` function.


# Step 2
# Explanation: Now we will open the log file and read it line by line. Reading line by 
# line is much better for log files because they can be huge, and reading them all at 
# once could crash the computer. We will also introduce a counter to track the total lines.

def create_sample_log():
    sample_data = """[2023-11-01 10:00:01] INFO: System started successfully.
[2023-11-01 10:05:12] WARNING: High memory usage detected.
[2023-11-01 10:12:45] ERROR: Database connection failed.
[2023-11-01 10:15:00] INFO: Retry attempt 1...
[2023-11-01 10:15:05] ERROR: Retry failed. System shutting down."""
    with open('server.log', 'w') as file:
        file.write(sample_data)

def parse_log(input_file):
    total_lines = 0
    
    with open(input_file, 'r') as file:
        for line in file:
            total_lines += 1
            # We use .strip() to remove the hidden newline character at the end of the line
            print(f"Line {total_lines}: {line.strip()}")
            
    print(f"\nTotal lines scanned: {total_lines}")

create_sample_log()
parse_log('server.log')

# What we accomplished in this step:
# - We successfully iterated through the file line by line.
# - We kept track of the total number of lines processed.


# Step 3
# Explanation: We don't want to print every line; we only care about errors. 
# We will use the `in` operator to check if the string 'ERROR' is present in the line. 
# We will add a second counter to track how many errors we find.

def create_sample_log():
    sample_data = """[2023-11-01 10:00:01] INFO: System started successfully.
[2023-11-01 10:05:12] WARNING: High memory usage detected.
[2023-11-01 10:12:45] ERROR: Database connection failed.
[2023-11-01 10:15:00] INFO: Retry attempt 1...
[2023-11-01 10:15:05] ERROR: Retry failed. System shutting down."""
    with open('server.log', 'w') as file:
        file.write(sample_data)

def parse_log(input_file):
    total_lines = 0
    error_count = 0
    
    print("Extracting errors...")
    with open(input_file, 'r') as file:
        for line in file:
            total_lines += 1
            
            # Check if this line contains an error
            if 'ERROR' in line:
                error_count += 1
                print(f"Found: {line.strip()}")
                
    print(f"\nSummary: Scanned {total_lines} lines, found {error_count} errors.")

create_sample_log()
parse_log('server.log')

# What we accomplished in this step:
# - We used conditional logic (`if 'ERROR' in line`) to filter the data.
# - We added a specific counter for the targeted lines.


# Step 4
# Explanation: The goal is to write these errors to a new file, not just print them. 
# We will open a second file called `errors_only.log` in write mode (`'w'`). 
# We can actually nest our `with` statements, opening the read file and the write 
# file at the same time!

def create_sample_log():
    sample_data = """[2023-11-01 10:00:01] INFO: System started successfully.
[2023-11-01 10:05:12] WARNING: High memory usage detected.
[2023-11-01 10:12:45] ERROR: Database connection failed.
[2023-11-01 10:15:00] INFO: Retry attempt 1...
[2023-11-01 10:15:05] ERROR: Retry failed. System shutting down."""
    with open('server.log', 'w') as file:
        file.write(sample_data)

def parse_log(input_file):
    total_lines = 0
    error_count = 0
    output_file = 'errors_only.log'
    
    # We open the input file for reading and the output file for writing simultaneously
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            total_lines += 1
            if 'ERROR' in line:
                error_count += 1
                # Write the exact line (which already has a newline character) to the new file
                outfile.write(line)
                
    print(f"Summary: Scanned {total_lines} lines, found {error_count} errors.")
    print(f"Errors successfully saved to '{output_file}'.")

create_sample_log()
parse_log('server.log')

# What we accomplished in this step:
# - We learned how to open multiple files concurrently using a single `with` block.
# - We extracted filtered data from one file and immediately wrote it to another.


# Step 5
# Explanation: Our parser is almost perfect, but what if the file we are asked to parse 
# does not exist? We need to reuse our knowledge from the advanced file handling exercise. 
# We will add a helper function to log errors, and wrap our parsing logic in a 
# `try/except` block to catch `FileNotFoundError`.

import datetime

def log_error(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('error_log.txt', 'a') as log_file:
        log_file.write(f"[{timestamp}] ERROR: {message}\n")

def parse_log(input_file):
    total_lines = 0
    error_count = 0
    output_file = 'errors_only.log'
    
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                total_lines += 1
                if 'ERROR' in line:
                    error_count += 1
                    outfile.write(line)
                    
        print(f"Summary: Scanned {total_lines} lines, found {error_count} errors.")
        print(f"Errors successfully saved to '{output_file}'.")
        
    except FileNotFoundError:
        print(f"Failed to parse: The file '{input_file}' does not exist.")
        log_error(f"Parser failed - File not found: '{input_file}'")


# Step 6
# Explanation: Let's consolidate everything into a final, robust script. We will generate 
# the sample log, parse it successfully, and then purposefully attempt to parse a missing 
# file to demonstrate our error handling. We will include expected outputs in the comments.

import datetime

def log_error(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('error_log.txt', 'a') as log_file:
        log_file.write(f"[{timestamp}] ERROR: {message}\n")

def create_sample_log():
    sample_data = """[2023-11-01 10:00:01] INFO: System started successfully.
[2023-11-01 10:05:12] WARNING: High memory usage detected.
[2023-11-01 10:12:45] ERROR: Database connection failed.
[2023-11-01 10:15:00] INFO: Retry attempt 1...
[2023-11-01 10:15:05] ERROR: Retry failed. System shutting down."""
    with open('server.log', 'w') as file:
        file.write(sample_data)

def parse_log(input_file):
    total_lines = 0
    error_count = 0
    output_file = 'errors_only.log'
    
    print(f"--- Parsing '{input_file}' ---")
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                total_lines += 1
                if 'ERROR' in line:
                    error_count += 1
                    outfile.write(line)
                    
        print(f"Summary: Scanned {total_lines} lines, found {error_count} errors.")
        print(f"Errors successfully saved to '{output_file}'.\n")
        
    except FileNotFoundError:
        print(f"Failed to parse: The file '{input_file}' does not exist.")
        log_error(f"Parser failed - File not found: '{input_file}'")
        print("Error logged to 'error_log.txt'.\n")

# Test our parser:
if __name__ == "__main__":
    # Create the test environment
    create_sample_log()
    
    # Test 1: Parse a valid file
    parse_log('server.log')
    
    # Show the contents of the generated errors file
    print("Contents of 'errors_only.log':")
    with open('errors_only.log', 'r') as err_file:
        print(err_file.read().strip())
    print("\n")
    
    # Test 2: Parse a missing file
    parse_log('ghost_server.log')

    # Expected Output Example:
    # --- Parsing 'server.log' ---
    # Summary: Scanned 5 lines, found 2 errors.
    # Errors successfully saved to 'errors_only.log'.
    #
    # Contents of 'errors_only.log':
    # [2023-11-01 10:12:45] ERROR: Database connection failed.
    # [2023-11-01 10:15:05] ERROR: Retry failed. System shutting down.
    #
    # --- Parsing 'ghost_server.log' ---
    # Failed to parse: The file 'ghost_server.log' does not exist.
    # Error logged to 'error_log.txt'.

# What we accomplished in this step:
# - We completed a real-world utility that filters data from one file to another.
# - We integrated robust error handling and logging.
# - We proved our program works correctly for both success and failure states.

# ===============================================================================
# CONGRATULATIONS! 🎉
# You've built a complete, professional mini log parser! 
# You learned how to efficiently process large files line-by-line, extract specific 
# information based on string matching, and write the filtered results to a new file, 
# all while managing multiple file contexts simultaneously. You also reinforced best 
# practices by handling missing files gracefully and writing the failures to an audit log. 
# This exact pattern is used constantly in server administration and data engineering.
# Remember: The best way to learn is by doing! 🚀
