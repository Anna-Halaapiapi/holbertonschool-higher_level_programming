#!/usr/bin/python3
"""
This module provides the convert_csv_to_json function.
"""


import csv
import json


def convert_csv_to_json(csv_file):
    """
    reads data from csv file
    converts data and saves in json file.
    returns True (success), else returns False (fail).
    """
    try:
        with open(csv_file, mode='r', newline='', encoding='utf-8') as cf:
            data = list(csv.DictReader(cf))

    except Exception:
        return False

    try:
        with open('data.json', mode='w', encoding='utf-8') as jf:
            json.dump(data, jf)
    except Exception:
        return False

    return True
