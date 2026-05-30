"""Question: Explore Python's dynamic typing and type conversion in depth. Create a function that accepts any value and returns a dictionary describing it: its original value, its type, whether it's truthy or falsy, and what happens when you try to convert it to int, float, str, and bool. Handle conversion errors gracefully."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Build a function that uses `try/except` for each conversion attempt.
# - Check truthiness using the built-in `bool()` function.
# - Understand which types can be converted to which (e.g., you can't convert "hello" to an integer).
#
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Use a function `analyze_value(value)` that returns a dictionary.
# - For each conversion, wrap it in a `try/except` block: try `int(value)`, `float(value)`, `str(value)`, `bool(value)`.
# - If a conversion fails, store an error message like 'Conversion Error' instead of crashing.
# - Test your function with different inputs: `42`, `'hello'`, `3.14`, `''`, `0`, `'123'`, `None`, `[1,2]`.
# - Remember that `bool()` always works, but certain strings like `'hello'` cannot become integers.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by writing a skeleton for our function. We will take a single 
# argument `value`. We want to determine its type and its truthiness (whether Python 
# considers it True or False when evaluated in an if-statement). We will pack these 
# into a dictionary and return it.

def analyze_value(value):
    # Get the name of the type for cleaner output
    value_type = type(value).__name__
    
    # Evaluate its truthiness
    truthiness = bool(value)
    
    # Pack into a dictionary
    result = {
        'original_value': value,
        'type': value_type,
        'is_truthy': truthiness
    }
    
    return result

# What we accomplished in this step:
# - We created a function that accepts any data type.
# - We dynamically inspected the type of the value.
# - We evaluated its truthiness and stored everything in a dictionary.


# Step 2
# Explanation: Now we'll try to convert the value to an integer. Since we know some 
# conversions will fail (like int("hello") or int([1, 2])), we must wrap this attempt 
# in a try/except block. If it fails, we will store a safe error message instead of 
# letting the program crash.

def analyze_value(value):
    value_type = type(value).__name__
    truthiness = bool(value)
    
    result = {
        'original_value': value,
        'type': value_type,
        'is_truthy': truthiness
    }
    
    # Attempt integer conversion
    try:
        result['as_int'] = int(value)
    except (ValueError, TypeError):
        result['as_int'] = 'Conversion Error'
        
    return result

# What we accomplished in this step:
# - We added a safe attempt to convert the input to an integer.
# - We used a try/except block, catching ValueError and TypeError, to prevent crashes on invalid conversions.


# Step 3
# Explanation: We will continue expanding our function by doing the exact same thing 
# for floats. Converting to float has similar pitfalls to integer conversion, so we 
# wrap it in its own try/except block.

def analyze_value(value):
    value_type = type(value).__name__
    truthiness = bool(value)
    
    result = {
        'original_value': value,
        'type': value_type,
        'is_truthy': truthiness
    }
    
    # Attempt integer conversion
    try:
        result['as_int'] = int(value)
    except (ValueError, TypeError):
        result['as_int'] = 'Conversion Error'
        
    # Attempt float conversion
    try:
        result['as_float'] = float(value)
    except (ValueError, TypeError):
        result['as_float'] = 'Conversion Error'
        
    return result

# What we accomplished in this step:
# - We added a safe float conversion step.
# - We successfully isolated the `int` and `float` conversion attempts so one failing doesn't stop the other.


# Step 4
# Explanation: Next, we add string conversion. In Python, almost everything can be 
# converted to a string using `str()`, so this rarely fails. However, we'll still 
# structure it cleanly for our dictionary.

def analyze_value(value):
    value_type = type(value).__name__
    truthiness = bool(value)
    
    result = {
        'original_value': value,
        'type': value_type,
        'is_truthy': truthiness
    }
    
    # Attempt integer conversion
    try:
        result['as_int'] = int(value)
    except (ValueError, TypeError):
        result['as_int'] = 'Conversion Error'
        
    # Attempt float conversion
    try:
        result['as_float'] = float(value)
    except (ValueError, TypeError):
        result['as_float'] = 'Conversion Error'
        
    # Attempt string conversion
    try:
        result['as_str'] = str(value)
    except Exception as e:
        result['as_str'] = f'Error: {e}'
        
    return result

# What we accomplished in this step:
# - We added a string conversion to our analysis.
# - We see that `str()` is highly flexible and almost universally applicable in Python.


# Step 5
# Explanation: Finally, we'll add an explicit boolean conversion. Even though we 
# already checked truthiness at the top, showing it as a dedicated conversion step 
# makes our dictionary complete. `bool()` works on all built-in types in Python 
# without raising exceptions.

def analyze_value(value):
    value_type = type(value).__name__
    truthiness = bool(value)
    
    result = {
        'original_value': value,
        'type': value_type,
        'is_truthy': truthiness
    }
    
    # Attempt integer conversion
    try:
        result['as_int'] = int(value)
    except (ValueError, TypeError):
        result['as_int'] = 'Conversion Error'
        
    # Attempt float conversion
    try:
        result['as_float'] = float(value)
    except (ValueError, TypeError):
        result['as_float'] = 'Conversion Error'
        
    # Attempt string conversion
    try:
        result['as_str'] = str(value)
    except Exception as e:
        result['as_str'] = f'Error: {e}'
        
    # Explicit boolean conversion
    result['as_bool'] = bool(value)
        
    return result

# What we accomplished in this step:
# - We completed the type conversion analysis with an explicit `bool()` operation.
# - Our function is now fully equipped to safely analyze any Python data type!


# Step 6
# Explanation: Let's clean up our script and put it to the test. We will create a 
# list containing a variety of data types, pass them into our function, and print 
# the resulting dictionaries in a nicely formatted way to see how Python handles them.

def analyze_value(value):
    value_type = type(value).__name__
    
    result = {
        'original_value': value,
        'type': value_type,
        'is_truthy': bool(value)
    }
    
    try:
        result['as_int'] = int(value)
    except (ValueError, TypeError):
        result['as_int'] = 'Conversion Error'
        
    try:
        result['as_float'] = float(value)
    except (ValueError, TypeError):
        result['as_float'] = 'Conversion Error'
        
    try:
        result['as_str'] = str(value)
    except Exception as e:
        result['as_str'] = f'Error: {e}'
        
    result['as_bool'] = bool(value)
        
    return result

# Test our code:
print("--- Step 6: Testing Type Conversions ---\n")

test_values = [42, 'hello', 3.14, '', 0, '123', None, [1, 2]]

for item in test_values:
    # We use repr() to clearly show empty strings and None
    print(f"--- Analyzing: {repr(item)} ---")
    
    analysis = analyze_value(item)
    
    for key, val in analysis.items():
        print(f"{key}: {val}")
    print()

# Expected output snippets:
#
# --- Analyzing: 'hello' ---
# original_value: hello
# type: str
# is_truthy: True
# as_int: Conversion Error
# as_float: Conversion Error
# as_str: hello
# as_bool: True
#
# --- Analyzing: '' ---
# original_value: 
# type: str
# is_truthy: False
# as_int: Conversion Error
# as_float: Conversion Error
# as_str: 
# as_bool: False
#
# --- Analyzing: '123' ---
# original_value: 123
# type: str
# is_truthy: True
# as_int: 123
# as_float: 123.0
# as_str: 123
# as_bool: True

# What we accomplished in this step:
# - We executed our robust function against a wide array of Edge cases.
# - We observed how '123' converts perfectly, while 'hello' correctly returns 'Conversion Error'.
# - We saw that empty strings ('') and 0 evaluate to False (falsy), while others evaluate to True (truthy).


# CONGRATULATIONS! 🎉
# You've mastered dynamic typing and safe type conversions in Python!
# You learned how to evaluate truthiness, gracefully handle conversion 
# errors using try/except blocks, and build a robust function capable 
# of analyzing any data type thrown at it. Understanding how Python 
# treats different types is a crucial skill for preventing bugs.
# Remember: The best way to learn is by doing! 🚀
