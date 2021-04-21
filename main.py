import csv
import json

csv_file_path = "bom.csv"
json_file_path = "bom.json"

data = []

# Open a csv reader called DictReader
with open(csv_file_path, encoding='utf-8') as csvf:
    csv_reader = csv.DictReader(csvf)
    # Convert each row into a dictionary
    # and add it to the data array
    for rows in csv_reader:
        data.append(rows)
# Open a json writer, and use the json.dumps()
# function to dump data
with open(json_file_path, 'w', encoding='utf-8') as jsonf:
    jsonf.write(json.dumps(data, indent=4))