import requests
import json
import time

def course_request(subject, classLevels):
    # Base URL components
    host = "https://classes.cornell.edu"
    api_version = "2.0"
    method = "search/classes"
    #method2 = "config/subjects" #Only for configuration

    # Parameters
    roster = "FA23"
    #subject = "MATH"
    #classLevels = [1000, 2000]

<<<<<<< Updated upstream
    # Construct the URL
    base_url = "{}/api/{}/{}.json".format(host, api_version, method)
    params = {
        'roster': roster,
        'subject': subject,
     'classLevels[]': classLevels,
    }

    # Make the API request
    response = requests.get(base_url, params=params)
    return response.json()
=======
# Construct the URL
base_url = f"{host}/api/{api_version}/{method}.json"
params = {
    'roster': roster,
    'subject': subject,
    'classLevels[]': classLevels,
    "q": "Machine Learning" #THIS PART IS WHERE THE KEYWORD IS DEFINED, BUT IT LEADS TO AN API ERROR WHEN UNCOMMENTED
}
>>>>>>> Stashed changes

def getcourse(data):
    list = []
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
                        instructor_name = "{} {}".format(instructors[0].get('firstName', 'N/A'), instructors[0].get('lastName', 'N/A'))
                    else:
                        instructor_name = 'N/A'
                    
                    if title_long not in list:
                        list.append(title_long)

                        print("Course Name: {}".format(title_long))
                        if units_min != units_max:
                            print("Units: {} to {}".format(units_min, units_max))
                        else:
                            print("Units: {}".format(units_min))
                        print("Instructor: {}".format(instructor_name))
                        print("Course: {} {}".format(course.get('subject', 'N/A'), course.get('catalogNbr', 'N/A')))
                        print("------------------------------")

def getcourse_simple(data):

    if data.get('status') == 'error':
        print("No courses found...")
        return 
    
    classes = data.get('data', {}).get('classes', [])
    printed_courses = set()
    for course in classes:
        title_long = course.get('titleLong', 'N/A')
        enrollGroups = course.get('enrollGroups', [{}])
        for group in enrollGroups:
            classSections = group.get('classSections', [{}])
            for section in classSections:
                meetings = section.get('meetings', [{}])
                for meeting in meetings:
                    instructors = meeting.get('instructors', [{}])
                    if instructors:
                        instructor_name = "{} {}".format(instructors[0].get('firstName', 'N/A'), instructors[0].get('lastName', 'N/A'))
                    else:
                        instructor_name = 'N/A'
                    
                    course_name = "{}, {}".format(title_long, instructor_name)
                    if course_name not in printed_courses:
                        printed_courses.add(course_name)
                        print(course_name)

def get_all_courses(subjects):
    #print('input    ', subjects)
    #print('input type    ', type(subjects))
    explain(subjects)
    time.sleep(1)
    for subject_code, subject_name in subjects.items():
        print(" ")
        print("################## Getting courses for {} in 1000, 2000, & 3000".format(subject_name))
        print("")
        data = course_request(subject_code, [1000, 2000, 3000])
        getcourse_simple(data)

def explain(subjects):
    print(" ")
    print(" ")
    for subject_code, subject_name in subjects.items():
        print("#################### You selected {} - {} ####################".format(subject_code, subject_name))
    print(" ")

    
#get_all_courses({'CS': 'Computer Science'})