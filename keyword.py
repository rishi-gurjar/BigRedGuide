import requests

base_url = "https://classes.cornell.edu/api/2.0/"  # Replace <HOST> with the actual host
endpoint = "search/classes"
full_url = f"{base_url}{endpoint}"

params = {
    "roster": "FA21",
    "subject": "CS",  # Computer Science
    "q": "Machine Learning"  # Optional keyword
}

response = requests.get(full_url, params=params)

if response.status_code == 200:
    data = response.json()
    # Process the data
else:
    print(f"Failed to get data: {response.status_code}")
