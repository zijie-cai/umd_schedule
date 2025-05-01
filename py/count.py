import json
import csv

# Load course sections data
with open('data/course_sections_spring.json', 'r') as f:
    course_sections = json.load(f)

# Load building coordinates from map.csv
building_coords = {}
with open('data/map.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        building_coords[row['code']] = {
            'lat': float(row['lat']),
            'long': float(row['long'])
        }

# Count classes per building
building_data = {}
for course, sections in course_sections.items():
    for section in sections:
        # Assuming `meeting_building` is a key in the section
        meeting_building = section['meetings'][0].get('building')
        if meeting_building:
            if meeting_building not in building_data:
                building_data[meeting_building] = {
                    'num_classes': 0,
                    'lat': building_coords.get(meeting_building, {}).get('lat'),
                    'long': building_coords.get(meeting_building, {}).get('long')
                }
            building_data[meeting_building]['num_classes'] += 1

# Save the output to a JSON file
with open('data/building_class_counts_spring.json', 'w') as f:
    json.dump(building_data, f, indent=4)

