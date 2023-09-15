# # app.py
# from flask import Flask, render_template, request, redirect, url_for, flash
# import sqlite3

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'

# # Database connection
# def get_db_connection():
#     conn = sqlite3.connect('mens_rings.db')
#     conn.row_factory = sqlite3.Row
#     return conn

# # Routes
# @app.route('/')
# def index():
#     conn = get_db_connection()
#     products = conn.execute('SELECT * FROM products').fetchall()
#     conn.close()
#     return render_template('index.html', products=products)

# @app.route('/product/<int:product_id>')
# def product(product_id):
#     conn = get_db_connection()
#     product = conn.execute('SELECT * FROM products WHERE id = ?', (product_id,)).fetchone()
#     conn.close()
#     return render_template('product.html', product=product)

# @app.route('/checkout', methods=['GET', 'POST'])
# def checkout():
#     if request.method == 'POST':
#         # Handle checkout form submission and order creation
#         # You will need to validate and insert the order and order items into the database
#         flash('Order placed successfully!', 'success')
#         return redirect(url_for('index'))

#     return render_template('checkout.html')

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='abhijain12104',
        database='mens_jewelry_db'
    )

# Routes
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()
    return render_template('index.html', products=products)
# ...

# Route for the home page
@app.route('/home')
def home():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()
    return render_template('home.html', products=products)

# ...

@app.route('/rings')
def rings():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM products')
        products = cursor.fetchall()
        return render_template('rings.html', products=products)
    except Exception as e:
        # Handle database or other exceptions here
        return str(e)
    finally:
        conn.close()
        
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/product/<int:product_id>')
def product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM products WHERE id = %s', (product_id,))
    product = cursor.fetchone()
    conn.close()
    return render_template('product.html', product=product)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        # Handle checkout form submission and order creation
        # You will need to validate and insert the order and order items into the database
        flash('Order placed successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('checkout.html')






if __name__ == '__main__':
    app.run(debug=True)
