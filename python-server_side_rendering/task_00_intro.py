#!/usr/bin/python3

import os

"""
This module provides the generate_invitations function.
"""


def generate_invitations(template, attendees):
    """
    populates template with attendees' data,
    saves the updated template to individual txt files.
    """
    # check input types
    if not isinstance(template, str):
        print("Error: templateis not a string.")
        return

    if not isinstance(attendees, list):
        print("Error: attendees is not a list.")
        return

    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("Error: attendees is not a list of dicts.")
            return

    # handle empty inputs
    if len(template) < 1:
        print("Template is empty, no output files generated.")
        return
    if len(attendees) < 1:
        print("No data provided, no output files generated.")
        return

    # populate templates with attendee details, write to files
    for index, attendee in enumerate(attendees, start=1):
        updated_template = template
        for p in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(p, "N/A")
            if value is None:
                value = "N/A"
            updated_template = updated_template.replace("{" + p + "}", value)
        file_name = 'output_' + str(index) + '.txt'
        if os.path.exists(file_name):
            print(f"Error: File {file_name} already exists.")
            continue
        try:
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(updated_template)
        except Exception:
            print(f"Error: Unable to generate {file_name}")
            continue
