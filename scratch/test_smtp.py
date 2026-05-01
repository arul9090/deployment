import os
import sys
from pathlib import Path

# Add backend to path so we can import config
backend_path = Path(r"c:\Users\UWAIS\Desktop\Task\API-Task\backend")
sys.path.append(str(backend_path))

from config import Config

def mask(s):
    if not s: return "NOT SET"
    if len(s) <= 4: return "****"
    return s[:2] + "*" * (len(s)-4) + s[-2:]

print(f"SMTP_HOST: {Config.SMTP_HOST}")
print(f"SMTP_PORT: {Config.SMTP_PORT}")
print(f"SMTP_USERNAME: {mask(Config.SMTP_USERNAME)}")
print(f"SMTP_PASSWORD: {mask(Config.SMTP_PASSWORD)}")
print(f"SMTP_FROM_EMAIL: {Config.SMTP_FROM_EMAIL}")
print(f"SMTP_USE_TLS: {Config.SMTP_USE_TLS}")

import smtplib
try:
    print("\nAttempting connection to SMTP host...")
    with smtplib.SMTP(Config.SMTP_HOST, Config.SMTP_PORT, timeout=10) as smtp:
        print("Connected successfully!")
        if Config.SMTP_USE_TLS:
            print("Starting TLS...")
            smtp.starttls()
            print("TLS started.")
        
        if Config.SMTP_USERNAME and Config.SMTP_PASSWORD:
            print(f"Attempting login for {Config.SMTP_USERNAME}...")
            smtp.login(Config.SMTP_USERNAME, Config.SMTP_PASSWORD)
            print("Login successful!")
        else:
            print("No credentials provided, skipping login.")
            
except Exception as e:
    print(f"\nError: {e}")
