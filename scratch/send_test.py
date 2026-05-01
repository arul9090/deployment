import sys, os
from pathlib import Path

sys.path.append(str(Path(r"c:\Users\UWAIS\Desktop\Task\API-Task\backend")))
from config import Config

import smtplib
from email.message import EmailMessage

print("=== SMTP Send Test ===")
print(f"Host     : {Config.SMTP_HOST}")
print(f"Port     : {Config.SMTP_PORT}")
print(f"Username : {Config.SMTP_USERNAME}")
print(f"From     : {Config.SMTP_FROM_EMAIL}")
print(f"TLS      : {Config.SMTP_USE_TLS}")
print()

# Send a real test email
TO_EMAIL = "rahmanabdur8009@gmail.com"  # change if needed

msg = EmailMessage()
msg["Subject"] = "SkillRank — SMTP Test Email"
msg["From"]    = Config.SMTP_FROM_EMAIL
msg["To"]      = TO_EMAIL
msg.set_content("This is a test email from your SkillRank SMTP setup using SendGrid.")

msg.add_alternative("""
<!DOCTYPE html>
<html>
<body style="background:#0b1120; color:#f1f5f9; font-family:Inter,sans-serif; padding:40px;">
  <div style="max-width:500px; margin:auto; background:#1e293b; border-radius:16px; padding:32px; border:1px solid rgba(148,163,184,.12);">
    <h2 style="color:#6366f1;">✅ SkillRank SMTP is Working!</h2>
    <p>This test email confirms your SendGrid SMTP integration is configured correctly.</p>
    <p style="color:#94a3b8; font-size:13px;">Sent from: """ + Config.SMTP_FROM_EMAIL + """</p>
  </div>
</body>
</html>
""", subtype="html")

try:
    print(f"Connecting to {Config.SMTP_HOST}:{Config.SMTP_PORT}...")
    with smtplib.SMTP(Config.SMTP_HOST, Config.SMTP_PORT, timeout=15) as smtp:
        print("Connected!")
        if Config.SMTP_USE_TLS:
            smtp.starttls()
            print("TLS started.")
        smtp.login(Config.SMTP_USERNAME, Config.SMTP_PASSWORD)
        print("Logged in!")
        smtp.send_message(msg)
        print(f"\n✅ SUCCESS! Email sent to {TO_EMAIL}")
        print("   Check your inbox (and spam folder).")
except Exception as e:
    print(f"\n❌ FAILED: {e}")
    print()
    print("Common causes:")
    print("  - SendGrid: Sender email not verified as a Single Sender")
    print("  - SendGrid: API key doesn't have 'Mail Send' permission")
    print("  - SendGrid: Free account blocked outbound to certain domains")
