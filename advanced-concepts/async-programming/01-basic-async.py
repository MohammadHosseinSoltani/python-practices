"""Question: Create an asynchronous function that simulates fetching data from three different sources concurrently. Use asyncio.gather to run them at the same time and print the results in order."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
# 
# Tips for success:
# - Understand how to define an asynchronous function using `async def`.
# - Use `await asyncio.sleep(seconds)` to simulate waiting for a network response without blocking the whole program.
# - Look into `asyncio.gather()` to see how you can run multiple async tasks at exactly the same time.
# 
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Define async functions with `async def`.
# - Use `await asyncio.sleep(seconds)` to simulate waiting for a network response.
# - Use `asyncio.gather()` to run multiple async functions concurrently.
# - Run the main entry point with `asyncio.run()`.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by writing a regular, synchronous function that simulates 
# fetching data using `time.sleep()`. We will call it three times sequentially. 
# This represents the old, blocking way of doing things. Notice how it takes 
# roughly 3 seconds to complete because each function call waits for the previous one.

import time

def fetch_data_sync(source):
    print(f"Starting fetch from {source}...")
    time.sleep(1)  # Simulates a slow network request
    print(f"Finished fetch from {source}.")

start_time = time.time()

fetch_data_sync("Source A")
fetch_data_sync("Source B")
fetch_data_sync("Source C")

end_time = time.time()
print(f"Total synchronous time: {end_time - start_time:.2f} seconds")

# What we accomplished in this step:
# - Established a baseline using synchronous programming.
# - Demonstrated how blocking operations (`time.sleep`) force tasks to run one after another.


# Step 2
# Explanation: Now we'll convert our function into an asynchronous one. We use the 
# `async def` syntax to define it, and replace the blocking `time.sleep()` with 
# `await asyncio.sleep()`. To actually run an async function, we cannot just call it 
# normally; we must pass it to `asyncio.run()`. For now, we will just run it once.

import time
import asyncio

async def fetch_data_async(source):
    print(f"Starting async fetch from {source}...")
    await asyncio.sleep(1)  # Non-blocking sleep!
    print(f"Finished async fetch from {source}.")

start_time = time.time()

# We use asyncio.run to execute our top-level async function
asyncio.run(fetch_data_async("Source A"))

end_time = time.time()
print(f"Total time for one async task: {end_time - start_time:.2f} seconds")

# What we accomplished in this step:
# - Introduced the `async def` and `await` keywords.
# - Replaced a blocking call with an awaitable, non-blocking call.
# - Used `asyncio.run()` to execute our asynchronous code.


# Step 3
# Explanation: To actually get the benefit of async programming, we need to run multiple 
# tasks concurrently. We will create a `main()` async function that uses `asyncio.gather()`. 
# This tells Python: "Start all of these tasks at the same time, and wait until they are all done."
# Notice how the total time drops from ~3 seconds to just ~1 second!

import time
import asyncio

async def fetch_data_async(source):
    print(f"Starting fetch from {source}...")
    await asyncio.sleep(1)
    print(f"Finished fetch from {source}.")

async def main():
    # gather() schedules all these tasks to run concurrently
    await asyncio.gather(
        fetch_data_async("Source A"),
        fetch_data_async("Source B"),
        fetch_data_async("Source C")
    )

start_time = time.time()
asyncio.run(main())
end_time = time.time()

print(f"Total concurrent time: {end_time - start_time:.2f} seconds")

# What we accomplished in this step:
# - Used `asyncio.gather()` to run multiple tasks concurrently.
# - Proved that async execution dramatically reduces waiting time for I/O bound operations.


# Step 4
# Explanation: In the real world, functions usually return data. We will update our fetch 
# function to return a string. When we use `asyncio.gather()`, it conveniently collects 
# all the returned values into a list, keeping them in the exact order we requested them!

import time
import asyncio

async def fetch_data_async(source):
    print(f"Fetching from {source}...")
    await asyncio.sleep(1)
    return f"Data from {source}"

async def main():
    # Store the results returned by gather()
    results = await asyncio.gather(
        fetch_data_async("Source A"),
        fetch_data_async("Source B"),
        fetch_data_async("Source C")
    )
    
    print("All tasks completed. Here are the results:")
    for result in results:
        print(f" - {result}")

asyncio.run(main())

# What we accomplished in this step:
# - Added return values to our asynchronous tasks.
# - Demonstrated how `asyncio.gather` returns an ordered list of results.


# Step 5
# Explanation: For our final step, let's consolidate everything into a clean, well-commented 
# demonstration. We will add slightly different sleep times to simulate real-world unpredictable 
# network latency, proving that `asyncio.gather` still waits for everything to finish and 
# still keeps the results in the correct order.

import time
import asyncio

async def fetch_data(source, delay):
    """Simulates fetching data from a source with a specific delay."""
    print(f"[{source}] Request initiated... (expected delay: {delay}s)")
    await asyncio.sleep(delay)
    print(f"[{source}] Request completed!")
    return f"Valid JSON data from {source}"

async def main():
    """Main entry point that manages our concurrent tasks."""
    print("Starting concurrent data fetch...")
    start_time = time.time()
    
    # We await gather, passing in our tasks. 
    # Source B takes the longest, so the program will wait a total of 1.5 seconds.
    results = await asyncio.gather(
        fetch_data("Source A", 0.5),
        fetch_data("Source B", 1.5),
        fetch_data("Source C", 1.0)
    )
    
    end_time = time.time()
    print(f"\nAll data fetched successfully in {end_time - start_time:.2f} seconds.")
    
    print("\nResults collected in order:")
    for i, data in enumerate(results, 1):
        print(f"{i}. {data}")

# Test our code:
if __name__ == "__main__":
    asyncio.run(main())
    
# Expected output:
# Starting concurrent data fetch...
# [Source A] Request initiated... (expected delay: 0.5s)
# [Source B] Request initiated... (expected delay: 1.5s)
# [Source C] Request initiated... (expected delay: 1.0s)
# [Source A] Request completed!
# [Source C] Request completed!
# [Source B] Request completed!
#
# All data fetched successfully in 1.50 seconds.
#
# Results collected in order:
# 1. Valid JSON data from Source A
# 2. Valid JSON data from Source B
# 3. Valid JSON data from Source C

# What we accomplished in this step:
# - Created a professional, robust asynchronous script.
# - Demonstrated how tasks finish at different times but results are still ordered correctly.
# - Used the standard `if __name__ == "__main__":` idiom for execution.


# CONGRATULATIONS! 🎉
# You have successfully written and executed asynchronous Python code!
# 
# Key takeaways:
# - `async def` and `await` are the foundation of modern Python asynchronous programming.
# - Async is ideal for I/O bound tasks (like downloading files, querying databases, or making API calls) 
#   because it allows Python to do other things while waiting.
# - Concurrency is not Parallelism! Async runs on a single thread, rapidly switching between tasks 
#   when one is paused (waiting).
# - `asyncio.gather()` is incredibly useful for dispatching multiple independent tasks and collecting their results.
# - `asyncio.run()` serves as the bridge between standard synchronous Python and your async functions.
# 
# Keep experimenting! Try adding more sources to the `gather` call, or see what happens if you 
# replace `await asyncio.sleep()` with a blocking `time.sleep()` (spoiler: it ruins the concurrency!).
# 
# Remember: The best way to learn is by doing! 🚀
