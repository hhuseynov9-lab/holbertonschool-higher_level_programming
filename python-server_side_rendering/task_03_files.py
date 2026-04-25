from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)

def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # CSV-dəki id və price-ı düzgün tipə çevirək
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
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
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

    # 2. ID filtrləmə
    if product_id:
        product_id = int(product_id)
        filtered_products = [p for p in products if p['id'] == product_id]
        if not filtered_products:
            error = "Product not found"
            return render_template('product_display.html', error=error)
        products = filtered_products

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)