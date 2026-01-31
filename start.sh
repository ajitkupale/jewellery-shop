#!/bin/bash

# Mahajan Jewellers - Startup Script
# BCA Final Year Project

echo "=========================================="
echo "  Mahajan Jewellers Management System"
echo "  Starting Application..."
echo "=========================================="
echo ""

# Start MySQL
echo "1. Starting MySQL Database..."
service mariadb start
sleep 2
echo "   ✓ MySQL Started"
echo ""

# Check if database exists, if not create it
echo "2. Checking Database..."
mysql -u root -e "USE mahajan_jewellers;" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "   Creating database..."
    mysql -u root < /app/backend/database.sql
    echo "   ✓ Database Created"
else
    echo "   ✓ Database Already Exists"
fi
echo ""

# Start Flask Application
echo "3. Starting Flask Application..."
cd /app/backend
python flask_app.py &
FLASK_PID=$!
sleep 3
echo "   ✓ Flask Started (PID: $FLASK_PID)"
echo ""

echo "=========================================="
echo "  APPLICATION IS NOW RUNNING!"
echo "=========================================="
echo ""
echo "  Open your browser and visit:"
echo "  http://localhost:5000"
echo ""
echo "  Admin Login:"
echo "  Email: admin@mahajanjewellers.com"
echo "  Password: mahajanchile"
echo ""
echo "  Press Ctrl+C to stop the application"
echo "=========================================="

# Keep script running
wait $FLASK_PID
