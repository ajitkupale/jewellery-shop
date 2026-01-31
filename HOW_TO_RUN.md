# How to Run Mahajan Jewellers Project on Localhost

## Step-by-Step Instructions for BCA Students

### Prerequisites
- Python 3.x installed
- MySQL/MariaDB installed
- Basic knowledge of terminal/command prompt

---

## Step 1: Start MySQL Database

Open terminal and run:
```bash
service mariadb start
```

Or for MySQL:
```bash
service mysql start
```

---

## Step 2: Create Database

Navigate to backend folder and create database:
```bash
cd /app/backend
mysql -u root < database.sql
```

This will:
- Create `mahajan_jewellers` database
- Create all necessary tables (users, admin, products, orders, daily_rates)
- Insert sample products
- Create default admin account

---

## Step 3: Install Python Dependencies

Install all required packages:
```bash
cd /app/backend
pip install -r requirements.txt
```

Required packages:
- Flask (Web framework)
- PyMySQL (Database connector)
- bcrypt (Password hashing)
- requests (API calls)

---

## Step 4: Run the Flask Application

Start the Flask server:
```bash
cd /app/backend
python flask_app.py
```

You should see:
```
 * Running on http://0.0.0.0:5000
```

---

## Step 5: Access the Application

Open your web browser and visit:
```
http://localhost:5000
```

---

## Default Login Credentials

### Admin Access:
- **URL:** http://localhost:5000/admin/login
- **Email:** admin@mahajanjewellers.com
- **Password:** mahajanchile

### User Access:
- **URL:** http://localhost:5000/user/login
- First, create an account via "Sign Up" link
- Then login with your credentials

---

## Project Structure

```
/app/
│
├── backend/
│   ├── flask_app.py          # Main application file
│   ├── config.py              # Configuration settings
│   ├── database.sql           # Database schema
│   └── requirements.txt       # Python dependencies
│
├── templates/
│   ├── index.html             # Home page
│   │
│   ├── user/
│   │   ├── signup.html        # User registration
│   │   ├── login.html         # User login
│   │   ├── dashboard.html     # User dashboard
│   │   ├── order.html         # Place order
│   │   └── orders.html        # Order history
│   │
│   └── admin/
│       ├── login.html         # Admin login
│       ├── dashboard.html     # Admin dashboard
│       ├── products.html      # Product management
│       ├── add_product.html   # Add product
│       ├── edit_product.html  # Edit product
│       └── orders.html        # Order management
│
└── static/
    └── css/
        └── style.css          # Custom styling
```

---

## Features to Demonstrate in Viva

### 1. User Module
- **Signup/Login:** Secure authentication with password hashing
- **View Rates:** Live gold & silver rates (₹ per gram)
- **Browse Products:** See available jewellery with stock info
- **Place Order:** Select product, enter weight, auto-calculate total
- **Order History:** View all orders with status

### 2. Admin Module
- **Dashboard:** Statistics (total users, orders, products)
- **Manage Products:** Add, edit, delete jewellery items
- **Manage Orders:** View all orders, update status (Pending/Confirmed/Cancelled)
- **View Rates:** Current gold & silver rates

### 3. Technical Features
- **Password Security:** Bcrypt hashing
- **Session Management:** Secure user sessions
- **API Integration:** Gold/Silver rate API with fallback
- **Real-time Calculation:** Order total = Weight × Rate
- **Responsive Design:** Bootstrap-based UI

---

## Database Tables Explained

### 1. users
- Stores customer information
- Fields: id, name, mobile, email, password (hashed)

### 2. admin
- Stores admin credentials
- Fields: id, email, password (hashed)

### 3. products
- Stores jewellery items
- Fields: id, name, type (Gold/Silver), base_weight, stock

### 4. orders
- Stores customer orders
- Fields: id, user_id, product_id, weight, rate, total_amount, status, order_date

### 5. daily_rates
- Stores daily gold & silver rates
- Fields: id, gold_rate, silver_rate, date

---

## Key Concepts for Viva

### 1. Why Flask?
- Lightweight Python web framework
- Easy to learn and implement
- Perfect for BCA-level projects
- Follows MVC pattern (Model-View-Controller)

### 2. Why MySQL?
- Relational database suitable for structured data
- ACID compliant (ensures data integrity)
- Easy to understand table relationships
- Supports foreign keys for data consistency

### 3. Security Features
- **Password Hashing:** Passwords stored as bcrypt hashes, not plain text
- **Session Management:** Server-side sessions for authentication
- **SQL Injection Prevention:** Parameterized queries
- **Separate User Types:** Different access levels (User vs Admin)

### 4. Business Logic
- **Order Calculation:** Total = Weight × Current Rate
- **Rate Management:** Daily rates fetched from API, stored in database
- **Stock Management:** Track available inventory
- **Order Status:** Track order lifecycle (Pending → Confirmed)

---

## Troubleshooting

### Issue: MySQL Connection Error
**Solution:**
```bash
# Start MySQL
service mariadb start

# Grant permissions
mysql -u root -e "GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost';"
```

### Issue: Flask App Not Starting
**Solution:**
```bash
# Check if dependencies are installed
pip install -r requirements.txt

# Check if port 5000 is free
lsof -i :5000

# Kill existing process if needed
pkill -f flask_app.py
```

### Issue: Database Not Created
**Solution:**
```bash
# Recreate database
mysql -u root < /app/backend/database.sql
```

---

## Testing Checklist

### User Flow:
1. ✅ Open homepage
2. ✅ Click "User Login" → "Sign Up"
3. ✅ Register new account
4. ✅ Login with credentials
5. ✅ View dashboard with rates
6. ✅ Browse jewellery collection
7. ✅ Place an order
8. ✅ View order history
9. ✅ Logout

### Admin Flow:
1. ✅ Open homepage
2. ✅ Click "Admin Login"
3. ✅ Login with admin credentials
4. ✅ View dashboard statistics
5. ✅ Add new product
6. ✅ Edit existing product
7. ✅ View all orders
8. ✅ Update order status
9. ✅ Logout

---

## Sample Test Data

### Test User:
- Name: Raj Kumar
- Mobile: 9876543210
- Email: raj@example.com
- Password: raj123

### Sample Order:
- Product: Gold Necklace
- Weight: 10 grams
- Rate: ₹6500/gram
- Total: ₹65,000

---

## Important Points for Project Presentation

1. **Project Title:** Mahajan Jewellers - Jewellery Shop Management System

2. **Technology Stack:**
   - Frontend: HTML5, CSS3, Bootstrap 5, JavaScript
   - Backend: Python Flask
   - Database: MySQL (MariaDB)

3. **Main Objectives:**
   - Manage jewellery inventory
   - Track customer orders
   - Display live gold/silver rates
   - Secure authentication system
   - Generate order summaries

4. **Key Features:**
   - Dual login (User & Admin)
   - Real-time order calculation
   - API integration for live rates
   - Responsive web design
   - Session-based authentication

5. **Future Enhancements:**
   - Payment gateway integration
   - Invoice generation (PDF)
   - Email/SMS notifications
   - Customer reviews & ratings
   - Advanced reporting & analytics

---

## Code Explanation Tips

### How Authentication Works:
```python
# Password hashing during signup
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Password verification during login
bcrypt.checkpw(password.encode('utf-8'), stored_password)

# Session management
session['user_id'] = user['id']
session['user_type'] = 'user'
```

### How Order Calculation Works:
```python
# Get today's rate
rate = gold_rate if product_type == 'Gold' else silver_rate

# Calculate total
total_amount = weight × rate

# Store order
INSERT INTO orders (user_id, product_id, weight, rate, total_amount)
```

### How Rate API Works:
```python
# Fetch from API
response = requests.get(api_url)

# If API fails, use fallback
if response.status_code != 200:
    gold_rate = 6500.00
    silver_rate = 75.00
```

---

## Contact for Help

If you face any issues:
1. Check the error message in terminal
2. Verify MySQL is running
3. Ensure all dependencies are installed
4. Check if port 5000 is available

---

## Conclusion

This project demonstrates:
- Full-stack web development skills
- Database design and management
- API integration
- Security best practices
- Clean and maintainable code

**Good luck with your BCA presentation!** 🎓✨
