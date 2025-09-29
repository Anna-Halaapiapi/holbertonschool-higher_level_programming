#!/usr/bin/python3
"""
This script adds all command line arguments to a Python list,
and then saves them to a JSON file:
"""

import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


# try open JSON file and load contents to local var as python object
try:
    json_file = load_from_json_file('add_item.json')

# if file doesn't exist, create it
except FileNotFoundError:
    with open('add_item.json', 'w', encoding='utf-8') as f:
        json.dump([], f)  # add new list to JSON file
    json_file = []  # create new list in local var

# add command line args local var
json_file.extend(sys.argv[1:])
# save local var list back to JSON file
save_to_json_file(json_file, 'add_item.json')
