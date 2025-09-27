#!/usr/bin/python3

def copy_by_line():
    """
    opens file for reading.
    opens/creates file for writing.
    reads source file line by line.
    writes each line to destination file.
    handles exception where source file doesn't exist.
    """
    try:
        with open('source.txt', 'r') as source_file:
            with open('destination.txt', 'w') as dest_file:
                for line in source_file:
                    dest_file.write(line)

    except FileNotFoundError:
        print("Error: source.txt not found.")

copy_by_line()
