import csv
import json
import os

def csv_to_json(csv_file_path, json_file_path):
    # Check if the CSV file exists
    if not os.path.exists(csv_file_path):
        print(f"Error: The file {csv_file_path} does not exist.")
        return

    # Create a dictionary
    data_dict = {}

    # Step 2
    # Open a CSV file handler
    with open(csv_file_path, encoding='utf-8') as csv_file_handler:
        csv_reader = csv.DictReader(csv_file_handler)

        # Check if 'Serial Number' column exists
        if 'STT' not in csv_reader.fieldnames:
            print("Error: 'STT' column not found in the CSV file.")
            return

        # Convert each row into a dictionary
        # and add the converted data to the data_variable
        for rows in csv_reader:
            # Assuming a column named 'Serial Number'
            # to be the primary key
            key = rows['STT']
            data_dict[key] = rows

    # Open a JSON file handler and use json.dumps
    # method to dump the data
    # Step 3
    with open(json_file_path, 'w', encoding='utf-8') as json_file_handler:
        # Step 4
        json_file_handler.write(json.dumps(data_dict, indent=4))

# Driver code
# Be careful while providing the path of the CSV file
# Provide the file path relative to your machine

# Step 1
csv_file_path = input('Enter the absolute path of the CSV file: ')
json_file_path = input('Enter the absolute path of the JSON file: ')

csv_to_json(csv_file_path, json_file_path)