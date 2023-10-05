## WEBSCRAPING USING KEYWORDS, OUTPUTS FIELDS OF STUDY RELATED TO KEYWORD

import requests
from bs4 import BeautifulSoup

# Define the URL of the Cornell University course catalog site
url = "https://classes.cornell.edu/browse/roster/FA23"

# Send an HTTP GET request to the URL
response = requests.get(url)

key = input('Keyword: ')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Specify the keyword(s) you want to search for
    keywords = ["computer science", "mathematics", "biology"]  # Add your desired keywords here
    keywords.append(key)

    # Find and print course information based on keywords
    for keyword in keywords:
        courses = soup.find_all(text=lambda text: keyword.lower() in text.lower())
        print(f"Courses related to '{keyword}':")
        for course in courses:
            print(course.strip())
        print()
else:
    print("Failed to retrieve the page. Check the URL and try again.")
