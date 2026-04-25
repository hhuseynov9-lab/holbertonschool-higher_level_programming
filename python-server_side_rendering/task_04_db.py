from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)

def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

def read_sql():
    products = []
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row  # Bu, nəticəni lüğət (dict) kimi almağa kömək edir
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Products')
        rows = cursor.fetchall()
        for row in rows:
            products.append(dict(row))
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []
    error = None

    # 1. Source yoxlanışı
    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    elif source == 'sql':
        products = read_sql()
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

    # 2. ID filtrləmə (əgər URL-də id=X yazılıbsa)
    if product_id:
        try:
            product_id = int(product_id)
            filtered_products = [p for p in products if p['id'] == product_id]
            if not filtered_products:
                error = "Product not found"
                return render_template('product_display.html', error=error)
            products = filtered_products
        except ValueError:
            error = "Invalid ID format"
            return render_template('product_display.html', error=error)

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
