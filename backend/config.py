# Configuration file for Mahajan Jewellers
# BCA Final Year Project

import os

class Config:
    """Application configuration class"""
    
    # Flask Settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'mahajan_jewellers_secret_key_2024'
    DEBUG = True
    
    # Database Settings
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = ''
    DB_NAME = 'mahajan_jewellers'
    
    # Session Settings
    SESSION_PERMANENT = False
    SESSION_TYPE = 'filesystem'
    
    # API Settings
    METALS_API_KEY = 'demo'  # Replace with actual API key if needed
