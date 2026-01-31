# Mahajan Jewellers - Project Summary

## BCA Final Year Project

---

## Project Overview

**Project Name:** Mahajan Jewellers - Jewellery Shop Management System

**Objective:** Create a web-based management system for a jewellery shop that handles customer orders, inventory management, and provides live gold/silver rates.

**Technology Stack:**
- **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript
- **Backend:** Python Flask
- **Database:** MySQL (MariaDB)
- **API:** Free Metal Price API (with fallback rates)

---

## Key Features Implemented

### 1. Home Page ✅
- Clean and attractive golden theme
- Two clear login buttons (User & Admin)
- "Sign Up" option visible below User Login
- Feature highlights section
- Professional and beginner-friendly design

### 2. User Module ✅

#### User Registration
- Full Name
- Mobile Number (10 digits)
- Email Address
- Password (hashed with bcrypt)

#### User Login
- Secure authentication
- Session-based login
- Error handling for invalid credentials

#### User Dashboard
- Welcome message with user name
- Today's gold & silver rates (per gram)
- Browse available jewellery with:
  - Product name
  - Type (Gold/Silver)
  - Base weight
  - Stock availability
- Navigation menu (Dashboard, Place Order, My Orders, Logout)

#### Place Order
- Select jewellery from dropdown
- Enter weight in grams
- **Real-time calculation:** Total = Weight × Current Rate
- Order summary display before confirmation
- Success message with total amount
- Order stored in database

#### My Orders
- View all orders in table format
- Order details: ID, Product, Type, Weight, Rate, Total Amount, Status, Date
- Status tracking (Pending/Confirmed/Cancelled)

### 3. Admin Module ✅

#### Admin Login
- Secure admin authentication
- Default credentials:
  - Email: admin@mahajanjewellers.com
  - Password: mahajanchile

#### Admin Dashboard
- Statistics cards:
  - Total Users
  - Total Orders
  - Total Products
  - Active Business indicator
- Today's metal rates display
- Quick action buttons
- Professional admin navigation

#### Products Management
- **View All Products:** Table with ID, Name, Type, Weight, Stock, Actions
- **Add Product:** 
  - Product name
  - Type (Gold/Silver dropdown)
  - Base weight in grams
  - Stock quantity
- **Edit Product:** Update existing product details
- **Delete Product:** Remove product with confirmation
- Color-coded badges (Gold: Yellow, Silver: Gray)

#### Orders Management
- View all customer orders
- Complete order information:
  - Order ID, User Name, Email
  - Product details, Type, Weight
  - Amount, Status, Date
- **Update Status:**
  - Confirm pending orders
  - Cancel orders
  - Confirmation dialog before action

### 4. Gold & Silver Rates ✅
- Fetches from free Metal Price API
- Updates once per day
- Stored in database
- **Fallback mechanism:** If API fails, uses default rates
  - Gold: ₹6500 per gram
  - Silver: ₹75 per gram
- Displayed on both user and admin dashboards

---

## Database Schema

### 1. users
```sql
- id (Primary Key)
- name
- mobile
- email (Unique)
- password (Hashed)
- created_at
```

### 2. admin
```sql
- id (Primary Key)
- email (Unique)
- password (Hashed)
- created_at
```

### 3. products
```sql
- id (Primary Key)
- name
- type (ENUM: Gold, Silver)
- base_weight
- stock
- image
- created_at
```

### 4. orders
```sql
- id (Primary Key)
- user_id (Foreign Key → users)
- product_id (Foreign Key → products)
- weight
- rate
- total_amount
- status (ENUM: Pending, Confirmed, Cancelled)
- order_date
```

### 5. daily_rates
```sql
- id (Primary Key)
- gold_rate
- silver_rate
- date (Unique)
- created_at
```

---

## Security Features

1. **Password Hashing:** All passwords stored as bcrypt hashes
2. **Session Management:** Flask session-based authentication
3. **SQL Injection Prevention:** Parameterized queries using PyMySQL
4. **Access Control:** Separate sessions for users and admin
5. **Form Validation:** Required fields and input validation

---

## Design Highlights

### Color Scheme
- **Primary:** Golden (#d4af37) - Traditional jewellery theme
- **Secondary:** Blue (#0d6efd) - User actions
- **Warning:** Yellow (#ffc107) - Admin actions
- **Background:** Cream gradient (#f5f5dc to #fff8dc)

### Typography
- **Headings:** Playfair Display (Serif - elegant)
- **Body:** Poppins (Sans-serif - clean and readable)

### UI/UX Elements
- Card-based layout
- Hover effects on buttons and cards
- Smooth transitions
- Font Awesome icons
- Responsive Bootstrap grid
- Color-coded badges for product types
- Status indicators for orders

---

## Sample Data Included

### Products (6 items)
1. Gold Necklace - 25.50g - Stock: 10
2. Gold Ring - 5.00g - Stock: 20
3. Gold Bracelet - 15.00g - Stock: 15
4. Silver Anklet - 30.00g - Stock: 25
5. Silver Chain - 10.00g - Stock: 30
6. Silver Bangle - 20.00g - Stock: 20

### Default Admin
- Email: admin@mahajanjewellers.com
- Password: mahajanchile

---

## Code Structure

### Backend (Flask)
```
flask_app.py (650+ lines)
├── Database Functions
│   ├── get_db_connection()
│   ├── hash_password()
│   ├── verify_password()
│   └── fetch_rates_from_api()
│
├── User Routes
│   ├── / (Home)
│   ├── /user/signup
│   ├── /user/login
│   ├── /user/dashboard
│   ├── /user/order
│   ├── /user/orders
│   └── /user/logout
│
├── Admin Routes
│   ├── /admin/login
│   ├── /admin/dashboard
│   ├── /admin/products
│   ├── /admin/products/add
│   ├── /admin/products/edit/<id>
│   ├── /admin/products/delete/<id>
│   ├── /admin/orders
│   ├── /admin/orders/update/<id>/<status>
│   └── /admin/logout
│
└── API Route
    └── /api/rates
```

### Frontend (Templates)
```
templates/
├── index.html (Home page)
├── user/
│   ├── signup.html
│   ├── login.html
│   ├── dashboard.html
│   ├── order.html
│   └── orders.html
└── admin/
    ├── login.html
    ├── dashboard.html
    ├── products.html
    ├── add_product.html
    ├── edit_product.html
    └── orders.html
```

---

## How to Run

### Quick Start
```bash
# Start MySQL
service mariadb start

# Create Database
mysql -u root < /app/backend/database.sql

# Install Dependencies
cd /app/backend
pip install -r requirements.txt

# Run Application
python flask_app.py
```

### Or Use Startup Script
```bash
bash /app/start.sh
```

### Access Application
```
http://localhost:5000
```

---

## Testing Results

### ✅ All Features Tested and Working

1. **User Registration:** Successfully creates account with hashed password
2. **User Login:** Authenticates and creates session
3. **User Dashboard:** Displays rates and products correctly
4. **Place Order:** Calculates total accurately (Weight × Rate)
5. **Order History:** Shows all orders with proper formatting
6. **Admin Login:** Secure admin access
7. **Admin Dashboard:** Statistics display correctly
8. **Product Management:** Add, Edit, Delete working perfectly
9. **Order Management:** View and update status functioning
10. **Logout:** Clears session properly

---

## Screenshots Available

1. Homepage with dual login buttons ✅
2. User signup form ✅
3. User login with success message ✅
4. User dashboard with rates and products ✅
5. Place order with real-time calculation ✅
6. Order success and history ✅
7. Admin login page ✅
8. Admin dashboard with statistics ✅
9. Products management table ✅
10. Orders management with actions ✅

---

## Documentation Provided

1. **README_PROJECT.md** - Complete project documentation
2. **HOW_TO_RUN.md** - Step-by-step running instructions
3. **database.sql** - Database schema with comments
4. **start.sh** - Easy startup script
5. **Code Comments** - Well-commented code throughout

---

## Viva Preparation Points

### Technical Questions

**Q: Why Flask instead of Django?**
A: Flask is lightweight, easy to learn, and perfect for small to medium projects. It gives more control and is ideal for BCA-level understanding.

**Q: How does password security work?**
A: We use bcrypt hashing. Passwords are never stored in plain text. During login, we hash the input and compare with stored hash.

**Q: How is the order total calculated?**
A: Total Amount = Weight (in grams) × Current Rate (per gram)
For example: 10g × ₹6500/g = ₹65,000

**Q: What if the API fails?**
A: We have fallback rates (Gold: ₹6500, Silver: ₹75). The application never crashes.

**Q: How do you prevent SQL injection?**
A: We use parameterized queries with PyMySQL. User inputs are never directly inserted into SQL.

### Business Logic Questions

**Q: Why only Gold and Silver?**
A: Requirement specified to keep it simple, avoiding diamond complexity for BCA project.

**Q: Can admin delete users?**
A: No, to maintain data integrity and order history. Only products can be deleted.

**Q: What happens to orders when product is deleted?**
A: CASCADE delete - orders are maintained but product reference is handled properly.

---

## Future Enhancements (For Discussion)

1. **Payment Gateway Integration** (Razorpay/Stripe)
2. **Invoice Generation** (PDF export)
3. **Email/SMS Notifications** (Order confirmation)
4. **Advanced Reporting** (Sales charts, graphs)
5. **Customer Reviews** (Product ratings)
6. **Multiple Admin Roles** (Super admin, Manager, Staff)
7. **Product Images Upload** (File handling)
8. **Discount Management** (Coupon codes)

---

## Project Highlights

✅ **Simple & Clean Design** - No over-complexity
✅ **Beginner-Friendly Code** - Well-commented for understanding
✅ **Complete CRUD Operations** - Create, Read, Update, Delete
✅ **Secure Authentication** - Password hashing, sessions
✅ **Real-time Calculations** - JavaScript for instant feedback
✅ **API Integration** - Live data with fallback
✅ **Responsive Design** - Works on all screen sizes
✅ **Professional UI** - Bootstrap + Custom CSS
✅ **Database Relations** - Foreign keys, proper schema
✅ **Error Handling** - Try-catch blocks, flash messages

---

## Conclusion

This project successfully demonstrates:
- Full-stack web development skills
- Database design and management
- Secure authentication implementation
- API integration
- Clean code practices
- User interface design
- Business logic implementation

**Perfect for BCA Final Year Project! Ready for Viva! 🎓✨**

---

## Contact & Support

For any queries:
- Check code comments
- Refer to documentation files
- Review screenshots
- Test all features locally

**All the Best for Your Presentation!**
