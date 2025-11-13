import os

"""
This module provides the generate_invitations function.
"""


def generate_invitations(template, attendees):
    """
    populates template with attendees data, saves to new files.
    """
    # check input types
    if not isinstance(template, str):
        print("Error: template is not a string.")
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

    # process each attendee
    updated_templates = []
    for attendee in attendees:
        new_item = template
        for key in attendee:
            if attendee[key] is None:
                value = "N/A"
            else:
                value = str(attendee[key])
            new_item = new_item.replace("{" + key + "}", value)
        updated_templates.append(new_item)

    # generate output files
    for index, item in enumerate(updated_templates, start=1):
        file_name = 'output_' + str(index) + '.txt'
        if os.path.exists(file_name):
            print(f"File {file_name} already exists, unable to generate.")
            continue
        try:

            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(item)
        except Exception:
            print(f"Unable to generate {file_name}")
            continue
