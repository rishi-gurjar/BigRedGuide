import requests
import json

# Base URL components
host = "https://classes.cornell.edu"
api_version = "2.0"
method = "search/classes"

# Parameters
roster = "FA23"
subject = "MATH"
classLevels = [1000, 2000]

# Construct the URL
base_url = f"{host}/api/{api_version}/{method}.json"
params = {
    'roster': roster,
    'subject': subject,
    'classLevels[]': classLevels,
  #  "q": "Machine Learning" #THIS PART IS WHERE THE KEYWORD IS DEFINED, BUT IT LEADS TO AN API ERROR WHEN UNCOMMENTED
}

# Make the API request
response = requests.get(base_url, params=params)
data = response.json()
print(data)
list = []
def getcourse(data):
    classes = data.get('data', {}).get('classes', [])
    for course in classes:
        title_long = course.get('titleLong', 'N/A')
        enrollGroups = course.get('enrollGroups', [{}])
        for group in enrollGroups:
            units_min = group.get('unitsMinimum', 'N/A')
            units_max = group.get('unitsMaximum', 'N/A')
            classSections = group.get('classSections', [{}])
            for section in classSections:
                meetings = section.get('meetings', [{}])
                for meeting in meetings:
                    instructors = meeting.get('instructors', [{}])
                    if instructors:
                        instructor_name = f"{instructors[0].get('firstName', 'N/A')} {instructors[0].get('lastName', 'N/A')}"
                    else:
                        instructor_name = 'N/A'
                    
                    if title_long not in list:
                        list.append(title_long)

                        print(f"Course Name: {title_long}")
                        if units_min != units_max:
                            print(f"Units: {units_min} to {units_max}")
                        else:
                            print(f"Units: {units_min}")
                        print(f"Instructor: {instructor_name}")
                        print(f"Course: {course.get('subject', 'N/A')} {course.get('catalogNbr', 'N/A')}")
                        print("------------------------------")

# Call the function to get the course details
#getcourse(data)
