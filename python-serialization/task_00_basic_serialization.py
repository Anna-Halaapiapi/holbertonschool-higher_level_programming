#!/usr/bin/python3
"""
This module provides serialize_and_save_to_file and
load_and_deserialize functions.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    serializes and saves data to the specified file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """
    loads and deserializes data from the specified file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
