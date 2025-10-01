#!/usr/bin/env python3
"""
This module provides the serialize_to_xml and deserialize_from_xml
functions.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    serialises dictionary into XML and saves
    to filename.
    """
    try:
        # create root element
        data = ET.Element('data')

        # convert dict items into XML elements
        for key, value in dictionary.items():
            child = ET.Element(key)  # create child element for each key
            child.text = str(value)  # set the text of the child element
            data.append(child)  # append child to root

        # create element tree object from the root
        tree = ET.ElementTree(data)

        # write the tree to the file
        tree.write(filename)

    except Exception:
        return False


def deserialize_from_xml(filename):
    """
    read XML data from filename, return a
    deserialised python dictionary.
    """
    # read the XML file
    tree = ET.parse(filename)
    # get the root element
    root = tree.getroot()

    new_dict = {}
    # Navigate through the XML elements to reconstruct the dictionary
    for child in root:
        value = child.text  # returns str (original dict value)
        try:  # try convert str to int, float, else leave as str
            value = int(value)
        except ValueError:
            try:
                value = float(value)
            except ValueError:
                pass
        # add the tag (key) and converted value (value) to new dict
        new_dict[child.tag] = value
    # Return the constructed dictionary.
    return new_dict
