"""Question: Use the csv module to write a list of dictionaries to a CSV file, then read that file back and display the contents as a formatted table. The CSV should contain columns for 'Name', 'Score', and 'Level'."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Import the `csv` module at the top of your file.
# - Look into using `csv.DictWriter` for writing and `csv.DictReader` for reading.
# - Remember to handle file paths and always open files using the `with` statement.
#
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Use `with open('scores.csv', 'w', newline='') as f:` for writing.
# - Create a `csv.DictWriter` object, providing `fieldnames` and calling `writeheader()`.
# - Use `writer.writerows(data)` to write a list of dictionaries.
# - For reading, use `csv.DictReader` and loop through the rows.
# - Use string formatting (f-strings) to print the data as a neat table.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by simply defining the data we want to write. 
# We need a list of dictionaries, where each dictionary represents a row in our CSV.
# The keys will match our column names: 'Name', 'Score', and 'Level'.
# We will print the list to verify our data structure is correct.

player_data = [
    {'Name': 'Alice', 'Score': 850, 'Level': 5},
    {'Name': 'Bob', 'Score': 1200, 'Level': 8},
    {'Name': 'Charlie', 'Score': 420, 'Level': 2}
]

print("Data ready to be written:")
print(player_data)

# What we accomplished in this step:
# - We created a list of dictionaries representing our tabular data.
# - We verified the structure matches the columns we need.


# Step 2
# Explanation: Now we will import the `csv` module and write this data to a file.
# We use `csv.DictWriter` because it perfectly handles dictionaries. 
# We specify `newline=''` in the `open()` function to prevent blank lines between 
# rows on certain operating systems like Windows.

import csv

player_data = [
    {'Name': 'Alice', 'Score': 850, 'Level': 5},
    {'Name': 'Bob', 'Score': 1200, 'Level': 8},
    {'Name': 'Charlie', 'Score': 420, 'Level': 2}
]

# The keys of our dictionaries will be our column headers
columns = ['Name', 'Score', 'Level']

# Open the file in write mode ('w')
with open('scores.csv', 'w', newline='') as file:
    # Create the writer object
    writer = csv.DictWriter(file, fieldnames=columns)
    
    # Write the column headers to the first row
    writer.writeheader()
    
    # Write all the dictionary data
    writer.writerows(player_data)

print("Data successfully written to scores.csv")

# What we accomplished in this step:
# - We imported the `csv` module.
# - We used `DictWriter` to write a header row automatically based on our column list.
# - We used `writerows` to write the entire list of dictionaries to the CSV file at once.


# Step 3
# Explanation: Writing data is only half the task; now we need to read it back.
# We will open the same file in read mode ('r') and use `csv.DictReader`. 
# `DictReader` automatically uses the first row of the CSV as the dictionary keys.
# Let's print out the raw dictionaries to see what Python reads.

import csv

player_data = [
    {'Name': 'Alice', 'Score': 850, 'Level': 5},
    {'Name': 'Bob', 'Score': 1200, 'Level': 8},
    {'Name': 'Charlie', 'Score': 420, 'Level': 2}
]
columns = ['Name', 'Score', 'Level']

# Write the file
with open('scores.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(player_data)

print("Reading data back from scores.csv:\n")

# Read the file
with open('scores.csv', 'r') as file:
    # Create the reader object
    reader = csv.DictReader(file)
    
    # Loop through each row in the CSV
    for row in reader:
        print(row)

# What we accomplished in this step:
# - We opened our newly created CSV file in read mode.
# - We used `csv.DictReader` to automatically parse each row into a dictionary.
# - We printed the raw dictionary output for verification.


# Step 4
# Explanation: Printing raw dictionaries isn't very user-friendly. 
# Let's format the output into a clean, aligned table. 
# We can use Python's f-strings with alignment specifiers (like `<10` for left-aligned, 
# 10 characters wide) to make sure our columns line up perfectly.

import csv

player_data = [
    {'Name': 'Alice', 'Score': 850, 'Level': 5},
    {'Name': 'Bob', 'Score': 1200, 'Level': 8},
    {'Name': 'Charlie', 'Score': 420, 'Level': 2}
]
columns = ['Name', 'Score', 'Level']

with open('scores.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(player_data)

print("Formatted Table Output:\n")

with open('scores.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    # Print our custom table headers
    print(f"{'Name':<10} | {'Score':<7} | {'Level':<5}")
    print("-" * 30)
    
    # Print each formatted row
    for row in reader:
        print(f"{row['Name']:<10} | {row['Score']:<7} | {row['Level']:<5}")

# What we accomplished in this step:
# - We replaced the raw dictionary print statements with beautifully formatted f-strings.
# - We learned how to use string formatting specifiers to create uniform columns.


# Step 5
# Explanation: Let's consolidate everything into a neat, final script. 
# We will wrap our logic in functions to make the code reusable and clean.
# We will then call these functions in a final test demonstration block.

import csv

def write_scores(filename, data):
    """Writes a list of player dictionaries to a CSV file."""
    columns = ['Name', 'Score', 'Level']
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(data)

def display_scores(filename):
    """Reads a CSV file and prints the contents as a formatted table."""
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        
        print(f"{'Name':<10} | {'Score':<7} | {'Level':<5}")
        print("-" * 30)
        
        for row in reader:
            print(f"{row['Name']:<10} | {row['Score']:<7} | {row['Level']:<5}")

# Test our module:
if __name__ == "__main__":
    initial_data = [
        {'Name': 'Alice', 'Score': 850, 'Level': 5},
        {'Name': 'Bob', 'Score': 1200, 'Level': 8},
        {'Name': 'Charlie', 'Score': 420, 'Level': 2},
        {'Name': 'Diana', 'Score': 3100, 'Level': 15}
    ]
    
    file_path = 'scores.csv'
    
    # Execute the writing and reading operations
    write_scores(file_path, initial_data)
    display_scores(file_path)
    
    # Expected Output Example:
    # Name       | Score   | Level
    # ------------------------------
    # Alice      | 850     | 5    
    # Bob        | 1200    | 8    
    # Charlie    | 420     | 2    
    # Diana      | 3100    | 15   

# What we accomplished in this step:
# - We structured our file operations into dedicated, reusable functions.
# - We successfully managed a full write-and-read data cycle.
# - We verified the final table presentation matches our expectations.

# ===============================================================================
# CONGRATULATIONS! 🎉
# You've mastered intermediate file handling using Python's `csv` module!
# Working with `DictWriter` and `DictReader` is the most reliable way to handle CSV 
# data because you rely on column names rather than specific indices. Furthermore, you 
# learned how to present raw file data to the user in a readable, formatted table 
# using f-strings. This skill is incredibly useful for reporting and data analysis.
# Remember: The best way to learn is by doing! 🚀
