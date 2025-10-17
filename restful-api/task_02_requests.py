#!/usr/bin/python3
"""
This module provides the fetch_and_print_posts and
fetch_and_save_posts functions.
"""

import json
import csv
import requests


def fetch_and_print_posts():
    """
    fetches all posts from JSONPlaceholder and prints response status code
    if response successful:
        converts response to JSON object (list of dicts)
        prints value of key 'title' in each dict
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f'Status Code: {r.status_code}')
    if r.status_code == 200:
        j = r.json()
        for item in j:
            print(item['title'])


def fetch_and_save_posts():
    """
    fetches all post from JSONPlaceholder
    if request sucessful:
        structures data into a list of dicts
        each dicts is a post with keys and values for id, title, and body
        writes data to CSV file with columns corresponding to the dict keys
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code == 200:
        j = r.json()
        formatted_list = []
        for item in j:
            formatted_list.append({
                'id': item['id'],
                'title': item['title'],
                'body': item['body']
            })
        try:
            with open('posts.csv', 'w', newline='', encoding='utf-8') as c:
                writer = csv.DictWriter(c, fieldnames=['id', 'title', 'body'])
                writer.writeheader()
                writer.writerows(formatted_list)
        except Exception:
            return
