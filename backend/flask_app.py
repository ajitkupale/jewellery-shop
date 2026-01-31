# Mahajan Jewellers - Flask Application
# BCA Final Year Project

from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import pymysql
import bcrypt
import requests
from datetime import datetime, date
import os

# Initialize Flask App
app = Flask(__name__, 
            template_folder='../templates',
            static_folder='../static')

# Secret key for session management
app.secret_key = 'mahajan_jewellers_secret_key_2024'

# Database Configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'mahajan_jewellers',
    'cursorclass': pymysql.cursors.DictCursor
}

# Database Connection Function
def get_db_connection():
    """Create and return database connection"""
    return pymysql.connect(**DB_CONFIG)

# Function to hash password
def hash_password(password):
    """Hash password using bcrypt"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Function to verify password
def verify_password(password, hashed):
    """Verify password against hashed password"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

# Function to fetch gold and silver rates from free API
def fetch_rates_from_api():
    """Fetch current gold and silver rates from API"""
    try:
        # Using metals-api.com free tier (limited calls)
        # Alternative: goldapi.io or metalpriceapi.com
        
        # Free API for metal prices (example)
        # Note: Replace with actual working free API
        url = "https://api.metalpriceapi.com/v1/latest"
        params = {
            'api_key': 'demo',  # Use demo for testing
            'base': 'INR',
            'currencies': 'XAU,XAG'  # Gold and Silver
        }
        
        response = requests.get(url, params=params, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            # Convert to per gram rates
            gold_rate = round(data.get('rates', {}).get('XAU', 6500), 2)
            silver_rate = round(data.get('rates', {}).get('XAG', 75), 2)
            return gold_rate, silver_rate
        else:
            # Return fallback rates if API fails
            return 6500.00, 75.00
    except Exception as e:
        print(f"API Error: {e}")
        # Return fallback rates
        return 6500.00, 75.00

# Function to get today's rates
def get_todays_rates():
    """Get today's gold and silver rates from database or API"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Check if rates exist for today
    cursor.execute("SELECT gold_rate, silver_rate FROM daily_rates WHERE date = %s", (date.today(),))
    result = cursor.fetchone()
    
    if result:
        gold_rate = float(result['gold_rate'])
        silver_rate = float(result['silver_rate'])
    else:
        # Fetch from API and store
        gold_rate, silver_rate = fetch_rates_from_api()
        cursor.execute(
            "INSERT INTO daily_rates (gold_rate, silver_rate, date) VALUES (%s, %s, %s)",
            (gold_rate, silver_rate, date.today())
        )
        conn.commit()
    
    cursor.close()
    conn.close()
    
    return gold_rate, silver_rate

# ============ ROUTES ============

# Home Page - Login Selection
@app.route('/')
def index():
    """Home page with User and Admin login options"""
    return render_template('index.html')

# User Signup
@app.route('/user/signup', methods=['GET', 'POST'])
def user_signup():
    """User registration page"""
    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']
        email = request.form['email']
        password = request.form['password']
        
        # Hash password
        hashed_password = hash_password(password)
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        try:
            # Insert user into database
            cursor.execute(
                "INSERT INTO users (name, mobile, email, password) VALUES (%s, %s, %s, %s)",
                (name, mobile, email, hashed_password)
            )
            conn.commit()
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('user_login'))
        except pymysql.IntegrityError:
            flash('Email already exists!', 'error')
        finally:
            cursor.close()
            conn.close()
    
    return render_template('user/signup.html')

# User Login
@app.route('/user/login', methods=['GET', 'POST'])
def user_login():
    """User login page"""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Check user credentials
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        if user and verify_password(password, user['password']):
            # Set session
            session['user_id'] = user['id']
            session['user_name'] = user['name']
            session['user_type'] = 'user'
            flash('Login successful!', 'success')
            return redirect(url_for('user_dashboard'))
        else:
            flash('Invalid email or password!', 'error')
    
    return render_template('user/login.html')

# User Dashboard
@app.route('/user/dashboard')
def user_dashboard():
    """User dashboard with rates and jewellery"""
    if 'user_id' not in session or session.get('user_type') != 'user':
        flash('Please login first!', 'error')
        return redirect(url_for('user_login'))
    
    # Get today's rates
    gold_rate, silver_rate = get_todays_rates()
    
    # Get all products
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE stock > 0")
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template('user/dashboard.html', 
                         gold_rate=gold_rate, 
                         silver_rate=silver_rate, 
                         products=products)

# Place Order
@app.route('/user/order', methods=['GET', 'POST'])
def place_order():
    """Place order page"""
    if 'user_id' not in session or session.get('user_type') != 'user':
        flash('Please login first!', 'error')
        return redirect(url_for('user_login'))
    
    if request.method == 'POST':
        product_id = request.form['product_id']
        weight = float(request.form['weight'])
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Get product details
        cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
        product = cursor.fetchone()
        
        # Get today's rate
        gold_rate, silver_rate = get_todays_rates()
        
        # Calculate total
        rate = gold_rate if product['type'] == 'Gold' else silver_rate
        total_amount = weight * rate
        
        # Insert order
        cursor.execute(
            "INSERT INTO orders (user_id, product_id, weight, rate, total_amount) VALUES (%s, %s, %s, %s, %s)",
            (session['user_id'], product_id, weight, rate, total_amount)
        )
        conn.commit()
        
        cursor.close()
        conn.close()
        
        flash(f'Order placed successfully! Total: ₹{total_amount:.2f}', 'success')
        return redirect(url_for('user_orders'))
    
    # Get products for order form
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE stock > 0")
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    
    gold_rate, silver_rate = get_todays_rates()
    
    return render_template('user/order.html', products=products, gold_rate=gold_rate, silver_rate=silver_rate)

# User Orders
@app.route('/user/orders')
def user_orders():
    """View user's orders"""
    if 'user_id' not in session or session.get('user_type') != 'user':
        flash('Please login first!', 'error')
        return redirect(url_for('user_login'))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Get user's orders with product details
    cursor.execute("""
        SELECT o.*, p.name as product_name, p.type as product_type 
        FROM orders o 
        JOIN products p ON o.product_id = p.id 
        WHERE o.user_id = %s 
        ORDER BY o.order_date DESC
    """, (session['user_id'],))
    orders = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return render_template('user/orders.html', orders=orders)

# User Logout
@app.route('/user/logout')
def user_logout():
    """User logout"""
    session.clear()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('index'))

# Admin Login
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    """Admin login page"""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Simple admin check (you can enhance this)
        if email == 'admin@mahajanjewellers.com' and password == 'mahajanchile':
            session['admin_id'] = 1
            session['admin_email'] = email
            session['user_type'] = 'admin'
            flash('Admin login successful!', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid admin credentials!', 'error')
    
    return render_template('admin/login.html')

# Admin Dashboard
@app.route('/admin/dashboard')
def admin_dashboard():
    """Admin dashboard with statistics"""
    if 'admin_id' not in session or session.get('user_type') != 'admin':
        flash('Please login as admin!', 'error')
        return redirect(url_for('admin_login'))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Get statistics
    cursor.execute("SELECT COUNT(*) as total_users FROM users")
    total_users = cursor.fetchone()['total_users']
    
    cursor.execute("SELECT COUNT(*) as total_orders FROM orders")
    total_orders = cursor.fetchone()['total_orders']
    
    cursor.execute("SELECT COUNT(*) as total_products FROM products")
    total_products = cursor.fetchone()['total_products']
    
    gold_rate, silver_rate = get_todays_rates()
    
    cursor.close()
    conn.close()
    
    return render_template('admin/dashboard.html', 
                         total_users=total_users,
                         total_orders=total_orders,
                         total_products=total_products,
                         gold_rate=gold_rate,
                         silver_rate=silver_rate)

# Admin - Manage Products
@app.route('/admin/products')
def admin_products():
    """Admin products management"""
    if 'admin_id' not in session or session.get('user_type') != 'admin':
        flash('Please login as admin!', 'error')
        return redirect(url_for('admin_login'))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template('admin/products.html', products=products)

# Admin - Add Product
@app.route('/admin/products/add', methods=['GET', 'POST'])
def admin_add_product():
    """Add new product"""
    if 'admin_id' not in session or session.get('user_type') != 'admin':
        flash('Please login as admin!', 'error')
        return redirect(url_for('admin_login'))
    
    if request.method == 'POST':
        name = request.form['name']
        type_ = request.form['type']
        base_weight = request.form['base_weight']
        stock = request.form['stock']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO products (name, type, base_weight, stock) VALUES (%s, %s, %s, %s)",
            (name, type_, base_weight, stock)
        )
        conn.commit()
        cursor.close()
        conn.close()
        
        flash('Product added successfully!', 'success')
        return redirect(url_for('admin_products'))
    
    return render_template('admin/add_product.html')

# Admin - Edit Product
@app.route('/admin/products/edit/<int:product_id>', methods=['GET', 'POST'])
def admin_edit_product(product_id):
    """Edit existing product"""
    if 'admin_id' not in session or session.get('user_type') != 'admin':
        flash('Please login as admin!', 'error')
        return redirect(url_for('admin_login'))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if request.method == 'POST':
        name = request.form['name']
        type_ = request.form['type']
        base_weight = request.form['base_weight']
        stock = request.form['stock']
        
        cursor.execute(
            "UPDATE products SET name=%s, type=%s, base_weight=%s, stock=%s WHERE id=%s",
            (name, type_, base_weight, stock, product_id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        
        flash('Product updated successfully!', 'success')
        return redirect(url_for('admin_products'))
    
    cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
    product = cursor.fetchone()
    cursor.close()
    conn.close()
    
    return render_template('admin/edit_product.html', product=product)

# Admin - Delete Product
@app.route('/admin/products/delete/<int:product_id>')
def admin_delete_product(product_id):
    """Delete product"""
    if 'admin_id' not in session or session.get('user_type') != 'admin':
        flash('Please login as admin!', 'error')
        return redirect(url_for('admin_login'))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
    conn.commit()
    cursor.close()
    conn.close()
    
    flash('Product deleted successfully!', 'success')
    return redirect(url_for('admin_products'))

# Admin - Manage Orders
@app.route('/admin/orders')
def admin_orders():
    """Admin orders management"""
    if 'admin_id' not in session or session.get('user_type') != 'admin':
        flash('Please login as admin!', 'error')
        return redirect(url_for('admin_login'))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Get all orders with user and product details
    cursor.execute("""
        SELECT o.*, u.name as user_name, u.email as user_email, 
               p.name as product_name, p.type as product_type 
        FROM orders o 
        JOIN users u ON o.user_id = u.id 
        JOIN products p ON o.product_id = p.id 
        ORDER BY o.order_date DESC
    """)
    orders = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return render_template('admin/orders.html', orders=orders)

# Admin - Update Order Status
@app.route('/admin/orders/update/<int:order_id>/<status>')
def admin_update_order(order_id, status):
    """Update order status"""
    if 'admin_id' not in session or session.get('user_type') != 'admin':
        flash('Please login as admin!', 'error')
        return redirect(url_for('admin_login'))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE orders SET status = %s WHERE id = %s", (status, order_id))
    conn.commit()
    cursor.close()
    conn.close()
    
    flash(f'Order status updated to {status}!', 'success')
    return redirect(url_for('admin_orders'))

# Admin Logout
@app.route('/admin/logout')
def admin_logout():
    """Admin logout"""
    session.clear()
    flash('Admin logged out successfully!', 'success')
    return redirect(url_for('index'))

# API endpoint to get current rates (for AJAX)
@app.route('/api/rates')
def api_rates():
    """API to get current gold and silver rates"""
    gold_rate, silver_rate = get_todays_rates()
    return jsonify({
        'gold_rate': gold_rate,
        'silver_rate': silver_rate
    })

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
