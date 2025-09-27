#!/usr/bin/python3

def read_and_print():
    try:
        with open('sample.txt', 'r') as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print("Error: sample.txt not found.")

read_and_print()
