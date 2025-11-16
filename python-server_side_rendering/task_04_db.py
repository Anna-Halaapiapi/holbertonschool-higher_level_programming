#!/usr/bin/python3
"""
A basic flask app.
"""

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    # load json data
    with open('items.json', 'r') as f:
        data = json.load(f)

    # extract list
    items = data.get('items', [])
 
    # pass list to items.html to use
    return render_template('items.html', items=items)

@app.route('/products')
def products():
    source = request.args.get('source') # query parameter (string: 'json' or 'csv' or 'sql')
    p_id = request.args.get('id') # query parameter (string, optional)

    products, error = serialize(source, p_id)

    return render_template('product_display.html', products=products, error=error)

def serialize(source, p_id):
    """
    gets product data from json, csv, or sqlite db
    returns product(s) and err msg
    """
    # get list of dicts from appropriate file or sqlite db 'products' table
    if source == 'json':
        with open('products.json', 'r') as f:
            data = json.load(f)

    elif source == 'csv':
        with open('products.csv', mode='r', newline='', encoding='utf-8') as f:
            data = list(csv.DictReader(f))

    elif source == 'sql':
        data = query_products_table()
    
    else:
        return None, "Wrong source"

    # Case 1: ID not provided - return all products
    if not p_id:
        return data, None

    for item in data:
        # Case 2: Match found - return matched product only
        if str(item["id"]) == str(p_id):
            return [item], None

    # Case 3: No match found - return an error
    return None, "Product not found"

def query_products_table():
    """
    queries the products table in sqlite database
    returns list of dicts containing all data in products table.
    """
    conn = sqlite3.connect('products.db') # connect to db
    conn.row_factory = sqlite3.Row # gets sqlite3.Row object (not dict or tuple)
    cursor = conn.cursor() # create cursor
    cursor.execute("SELECT * FROM products") # query products table in db
    results = cursor.fetchall() # fetch all results (a list of sqlite3.Row objects)
    conn.close() # close connection
    return [dict(result) for result in results] # convert to python list of dicts

if __name__ == '__main__':
    app.run(debug=True, port=5000)
