import json
import csv

# Open the JSON file and load its content
with open('route.json', 'r') as json_file:
    json_data = json.load(json_file)

# Specify the CSV file name where the data will be written
csv_file_name = 'route.csv'

# Determine the CSV column names
csv_columns = ['postKey', 'CurrentSalesman', 'RouteCode', 'RouteDescription', 'RouteName']

# Open the CSV file for writing
with open(csv_file_name, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for key, data in json_data.items():
        data['postKey'] = key  # Include the postKey in the data to be written to the CSV
        writer.writerow(data)
