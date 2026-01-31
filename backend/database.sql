-- Mahajan Jewellers Database Schema
-- BCA Final Year Project

-- Create Database
CREATE DATABASE IF NOT EXISTS mahajan_jewellers;
USE mahajan_jewellers;

-- Users Table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    mobile VARCHAR(15) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Admin Table
CREATE TABLE IF NOT EXISTS admin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Products Table (Jewellery Items)
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    type ENUM('Gold', 'Silver') NOT NULL,
    base_weight DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL DEFAULT 0,
    image VARCHAR(255) DEFAULT 'default.jpg',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Daily Rates Table (Gold & Silver Rates)
CREATE TABLE IF NOT EXISTS daily_rates (
    id INT AUTO_INCREMENT PRIMARY KEY,
    gold_rate DECIMAL(10, 2) NOT NULL,
    silver_rate DECIMAL(10, 2) NOT NULL,
    date DATE UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Orders Table
CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    product_id INT NOT NULL,
    weight DECIMAL(10, 2) NOT NULL,
    rate DECIMAL(10, 2) NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    status ENUM('Pending', 'Confirmed', 'Cancelled') DEFAULT 'Pending',
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- Insert Default Admin
-- Password: mahajanchile (hashed with bcrypt)
INSERT INTO admin (email, password) VALUES 
('admin@mahajanjewellers.com', '$2b$12$LKJ8h5K7Z9mXqZ5F5K7Z9eN8mXqZ5F5K7Z9eN8mXqZ5F5K7Z9eN8m');

-- Insert Sample Products
INSERT INTO products (name, type, base_weight, stock) VALUES
('Gold Necklace', 'Gold', 25.50, 10),
('Gold Ring', 'Gold', 5.00, 20),
('Gold Bracelet', 'Gold', 15.00, 15),
('Silver Anklet', 'Silver', 30.00, 25),
('Silver Chain', 'Silver', 10.00, 30),
('Silver Bangle', 'Silver', 20.00, 20);

-- Insert Default Today's Rate (Fallback)
INSERT INTO daily_rates (gold_rate, silver_rate, date) VALUES
(6500.00, 75.00, CURDATE())
ON DUPLICATE KEY UPDATE gold_rate=6500.00, silver_rate=75.00;
