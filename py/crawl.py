import json
import requests
from tqdm import  tqdm

# Load the courses JSON file
with open('/Users/masenov/Documents/GitHub/umd_schedule/data/courses_fall.json', 'r') as file:
    courses = json.load(file)

# Initialize a dictionary to store the results
course_sections = {}

# Iterate through each course
for course in tqdm(courses):
    course_id = course.get("course_id")
    if not course_id:
        continue

    # Make the API call
    url = f"https://api.umd.io/v1/courses/{course_id}/sections?semester=202508"
    try:
        response = requests.get(url)
        response.raise_for_status()
        course_sections[course_id] = response.json()
    except requests.RequestException as e:
        print(f"Failed to fetch sections for {course_id}: {e}")

# Save the results to a new JSON file
with open('/Users/masenov/Documents/GitHub/umd_schedule/data/course_sections_fall.json', 'w') as output_file:
    json.dump(course_sections, output_file, indent=2)
