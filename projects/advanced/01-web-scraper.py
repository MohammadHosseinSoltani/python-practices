"""Project: Build a simple web scraper that fetches quotes from 'quotes.toscrape.com', extracts the quote text and author, and displays them. The scraper should handle HTTP requests, parse HTML, and present the results in a readable format."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - You will need two external libraries for this: `requests` to fetch the web page, and `BeautifulSoup` (from `bs4`) to parse the HTML.
# - Inspect the target website (quotes.toscrape.com) using your browser's Developer Tools to find the HTML tags and classes that hold the quote text and the author's name.
# - Remember to handle potential network errors gracefully!
#
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Install the required libraries: `pip install requests beautifulsoup4`.
# - Use `requests.get(url)` to fetch the web page. Check `response.status_code` before proceeding.
# - Pass `response.text` to `BeautifulSoup` with `'html.parser'` to create a soup object.
# - Use `soup.select()` or `soup.find_all()` with the appropriate tags and classes (e.g., `soup.find_all('div', class_='quote')`).
# - For each quote block, extract the text (in a `<span>` with `class='text'`) and the author (in a `<small>` with `class='author'`).
# - Print the results cleanly with numbering.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by fetching the web page. We need to import the `requests` 
# library, define our target URL, and make a GET request. To verify that our 
# connection was successful, we will print the HTTP status code. A status code 
# of 200 means "OK" (success).
# (Note: If you haven't already, install the libraries via terminal: pip install requests beautifulsoup4)

import requests

url = "http://quotes.toscrape.com"
response = requests.get(url)

print(f"Connection Status Code: {response.status_code}")

# What we accomplished in this step:
# - Imported the `requests` library.
# - Defined our target URL.
# - Successfully made an HTTP GET request and retrieved the status code.


# Step 2
# Explanation: Now that we know we are connected, let's see what we actually received. 
# The `response` object contains an attribute called `.text` which holds the raw HTML 
# source code of the web page. We will print just the first 500 characters so we 
# don't overwhelm our terminal, but it confirms we have the data.

import requests

url = "http://quotes.toscrape.com"
response = requests.get(url)

print(f"Connection Status Code: {response.status_code}")

# Print a snippet of the raw HTML
raw_html = response.text
print("\nFirst 500 characters of the HTML:")
print(raw_html[:500])

# What we accomplished in this step:
# - Accessed the raw HTML content using `response.text`.
# - Verified that the text looks like valid HTML code.


# Step 3
# Explanation: Raw HTML is very hard to read and extract data from. We need to parse it. 
# We'll import `BeautifulSoup` from the `bs4` library. By passing our raw HTML and the 
# string `'html.parser'` to BeautifulSoup, we create a structured "soup" object. 
# By inspecting the website, we know that each quote is wrapped in a `div` tag with 
# the class `quote`. Let's find all of them and count how many are on the page.

import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com"
response = requests.get(url)

# Parse the HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Find all div elements that have the class 'quote'
# Note: we use class_ because 'class' is a reserved keyword in Python
quotes_blocks = soup.find_all('div', class_='quote')

print(f"Successfully found {len(quotes_blocks)} quotes on the page.")

# What we accomplished in this step:
# - Imported and utilized `BeautifulSoup`.
# - Parsed the raw HTML into a searchable structure.
# - Located specific HTML blocks using `find_all()` with a class filter.


# Step 4
# Explanation: Now we have a list of quote blocks, but we need to extract the specific 
# text and author from each one. By looking closely at a single quote block's HTML, 
# we can see the quote text is inside a `span` with `class='text'`, and the author 
# is inside a `small` tag with `class='author'`. We will loop through our blocks, 
# extract these specific pieces, and print them nicely.

import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
quotes_blocks = soup.find_all('div', class_='quote')

print("\n--- Extracted Quotes ---\n")

# Loop through each block and extract the details
for index, block in enumerate(quotes_blocks, 1):
    # .text extracts the readable text from between the HTML tags
    text = block.find('span', class_='text').text
    author = block.find('small', class_='author').text
    
    print(f"{index}. {text}")
    print(f"   - {author}\n")

# What we accomplished in this step:
# - Navigated deeper into the HTML structure.
# - Used the `.text` attribute to strip away HTML tags and get clean text.
# - Formatted the extracted data for a human-readable output.


# Step 5
# Explanation: Our scraper works perfectly when the internet and website are functioning. 
# But what if our Wi-Fi goes down, or the website crashes? We need to add error handling. 
# We will wrap our `requests.get()` inside a `try/except` block to catch network errors. 
# We will also add an `if` statement to ensure the status code is exactly 200 before 
# attempting to parse anything.

import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com"

try:
    # Adding a timeout is a good practice to prevent the script from hanging indefinitely
    response = requests.get(url, timeout=10)
    
    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes_blocks = soup.find_all('div', class_='quote')
        
        print("\n--- Extracted Quotes ---\n")
        
        for index, block in enumerate(quotes_blocks, 1):
            text = block.find('span', class_='text').text
            author = block.find('small', class_='author').text
            
            print(f"{index}. {text}")
            print(f"   - {author}\n")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        
except requests.exceptions.RequestException as e:
    # This catches timeouts, connection errors, and invalid URLs
    print(f"A network error occurred: {e}")

# What we accomplished in this step:
# - Secured our application against network failures using `try/except`.
# - Validated the HTTP status code before processing.
# - Added a timeout to the request for better performance and reliability.


# Step 6
# Explanation: For our final step, let's wrap our logic into a professional, reusable 
# function called `scrape_quotes()`. This keeps the global namespace clean and allows 
# us to run the scraper easily when the script is executed directly. We will also 
# include an example run comment block below it.

import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    """Fetches quotes and authors from quotes.toscrape.com and prints them to the console."""
    url = "http://quotes.toscrape.com"
    print(f"Connecting to {url}...")
    
    try:
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            print("Connection successful! Parsing data...\n")
            soup = BeautifulSoup(response.text, 'html.parser')
            quotes_blocks = soup.find_all('div', class_='quote')
            
            print("--- Top Quotes of the Day ---")
            
            for index, block in enumerate(quotes_blocks, 1):
                text = block.find('span', class_='text').text
                author = block.find('small', class_='author').text
                
                print(f"{index}. {text}")
                print(f"   - {author}\n")
                
            print("Scraping complete.")
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"A network error occurred: {e}")


if __name__ == "__main__":
    scrape_quotes()

# Example run:
#
# Connecting to http://quotes.toscrape.com...
# Connection successful! Parsing data...
#
# --- Top Quotes of the Day ---
# 1. “The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
#    - Albert Einstein
#
# 2. “It is our choices, Harry, that show what we truly are, far more than our abilities.”
#    - J.K. Rowling
#
# 3. “There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”
#    - Albert Einstein
#
# [ ... additional quotes ... ]
#
# Scraping complete.


# CONGRATULATIONS! 🎉
# You've successfully built a fully functioning web scraper!
#
# Key takeaways:
# - HTTP Requests: You learned how to programmatically connect to a website using the `requests` library.
# - HTML Parsing: You used `BeautifulSoup` to transform chaotic raw HTML into an easily navigable data structure.
# - Data Extraction: You practiced inspecting HTML to find the exact tags and classes needed to extract valuable data.
# - Web Scraping Ethics: This site (`toscrape.com`) is a sandbox designed for scraping. Remember that in the real world, you should always check a website's `robots.txt` file and Terms of Service before scraping, and avoid making too many rapid requests to prevent crashing their servers!
#
# Remember: The best way to learn is by doing! 🚀
