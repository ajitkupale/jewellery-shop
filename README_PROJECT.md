# Mahajan Jewellers - Jewellery Shop Management System

## BCA Final Year Project

A complete Jewellery Shop Management System built with Flask, HTML, CSS, Bootstrap, and MySQL.

---

## Features

### User Module
- User Registration and Login
- View Today's Gold & Silver Rates
- Browse Available Jewellery
- Place Orders with Auto-calculation
- View Order History

### Admin Module
- Admin Login
- Dashboard with Statistics
- Manage Products (Add, Edit, Delete)
- View and Manage Orders
- Update Order Status

---

## Technology Stack

**Frontend:**
- HTML5
- CSS3
- Bootstrap 5
- JavaScript (Vanilla)

**Backend:**
- Python Flask
- PyMySQL

**Database:**
- MySQL (MariaDB)

**API:**
- Free Metal Price API (with fallback rates)

---

## Project Structure

```
/app/
├── backend/
│   ├── flask_app.py          # Main Flask application
│   ├── config.py              # Configuration file
│   ├── database.sql           # Database schema
│   └── requirements.txt       # Python dependencies
├── templates/
│   ├── index.html             # Home page
│   ├── user/
│   │   ├── signup.html        # User registration
│   │   ├── login.html         # User login
│   │   ├── dashboard.html     # User dashboard
│   │   ├── order.html         # Place order
│   │   └── orders.html        # Order history
│   └── admin/
│       ├── login.html         # Admin login
│       ├── dashboard.html     # Admin dashboard
│       ├── products.html      # Manage products
│       ├── add_product.html   # Add product
│       ├── edit_product.html  # Edit product
│       └── orders.html        # Manage orders
└── static/
    ├── css/
    │   └── style.css          # Custom CSS styles
    └── js/
```

---

## Database Schema

### Tables:
1. **users** - Store user information
2. **admin** - Store admin credentials
3. **products** - Store jewellery products
4. **orders** - Store customer orders
5. **daily_rates** - Store gold & silver rates

---

## Installation & Setup

### Step 1: Install MySQL
```bash
# Already installed in this environment
service mariadb start
```

### Step 2: Create Database
```bash
mysql -u root < /app/backend/database.sql
```

### Step 3: Install Python Dependencies
```bash
cd /app/backend
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
cd /app/backend
python flask_app.py
```

The application will start on: **http://localhost:5000**

---

## Default Credentials

### Admin Login
- **Email:** admin@mahajanjewellers.com
- **Password:** mahajanchile

### Test User (Create via signup)
- Register as a new user through the signup page

---

## How to Use

### For Users:
1. Open http://localhost:5000
2. Click "User Login" → "Sign Up"
3. Register with your details
4. Login with your credentials
5. View today's gold & silver rates
6. Browse jewellery collection
7. Place orders by selecting product and weight
8. View your order history

### For Admin:
1. Open http://localhost:5000
2. Click "Admin Login"
3. Login with admin credentials
4. View dashboard statistics
5. Manage products (Add/Edit/Delete)
6. View all orders
7. Update order status (Pending/Confirmed/Cancelled)

---

## Key Features Explained

### 1. Gold & Silver Rate API
- Fetches live rates from free API
- Updates once per day
- Has fallback rates if API fails
- Stored in database for consistency

### 2. Order Calculation
- Automatic calculation: Total = Weight × Rate
- Real-time calculation on order page
- Uses today's rate from database

### 3. Session Management
- Secure session-based authentication
- Separate sessions for users and admin
- Password hashing with bcrypt

### 4. Responsive Design
- Mobile-friendly Bootstrap layout
- Clean and attractive UI
- Golden theme for jewellery shop

---

## Code Features for Viva

### Well-Commented Code
- Every function has clear comments
- Explains logic for easy understanding
- Beginner-friendly structure

### Simple Architecture
- Basic Flask routing
- Clear separation of concerns
- Easy to explain in viva

### Database Operations
- Simple CRUD operations
- Clear SQL queries
- Proper error handling

### Security Features
- Password hashing (bcrypt)
- Session management
- SQL injection prevention (parameterized queries)

---

## API Used

**Metal Price API:**
- Provides gold and silver rates
- Free tier available
- Fallback mechanism if API fails
- Default rates: Gold ₹6500/g, Silver ₹75/g

---

## Screenshots & Demo

### Home Page
- Two clear buttons: User Login and Admin Login
- Beautiful golden theme
- Feature highlights

### User Dashboard
- Today's rates display
- Jewellery collection
- Easy navigation

### Admin Dashboard
- Statistics cards
- Quick action buttons
- Order management

---

## Future Enhancements (For Discussion)

1. Payment Gateway Integration
2. SMS/Email Notifications
3. Invoice Generation
4. Advanced Reporting
5. Multiple Admin Roles
6. Product Images Upload
7. Discount Management
8. Customer Reviews

---

## Troubleshooting

### MySQL Not Starting
```bash
service mariadb start
```

### Flask App Not Running
```bash
# Check if all dependencies are installed
pip install -r requirements.txt

# Run the app
python flask_app.py
```

### Database Connection Error
```bash
# Recreate database
mysql -u root < /app/backend/database.sql
```

---

## Developer Information

**Project Name:** Mahajan Jewellers - Jewellery Shop Management System  
**Course:** BCA Final Year Project  
**Technology:** Flask + HTML + Bootstrap + MySQL  
**Shop Name:** Mahajan Jewellers  
**Tagline:** Pure Gold & Silver Excellence Since 1990

---

## Notes for Viva

1. **Why Flask?** - Lightweight, easy to learn, perfect for BCA project
2. **Why MySQL?** - Relational data (users, orders, products)
3. **Why Bootstrap?** - Quick responsive design, professional look
4. **Security:** Bcrypt password hashing, session management
5. **API Integration:** Live gold/silver rates with fallback
6. **Calculation Logic:** Weight × Rate = Total Amount
7. **User Experience:** Simple, clean, easy to navigate

---

## License

This project is created for educational purposes as part of BCA final year project.

---

## Contact & Support

For any queries or issues, please refer to the code comments or contact your project guide.

---

**Thank you for reviewing Mahajan Jewellers Management System!**
