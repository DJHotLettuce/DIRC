import csv
import json
import sys

if(len(sys.argv) < 2):
    print("Missing filename")
    exit()

csvFile = sys.argv[1]

# Step 1: Read the CSV file
with open(csvFile, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

# Step 2: Write to JSON file
jsonFileName = csvFile[:-4] + ".json"
with open(jsonFileName, 'w') as jsonfile:
    json.dump(data, jsonfile, indent=4)
