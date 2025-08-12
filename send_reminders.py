import smtplib
from datetime import datetime, timedelta
import sqlite3

conn = sqlite3.connect('../job_tracker.db')
cursor = conn.cursor()

today = datetime.today().date()
two_days_from_now = today + timedelta(days=2)

cursor.execute("SELECT company, position, deadline FROM jobs")
rows = cursor.fetchall()

for row in rows:
    company, position, deadline_str = row
    deadline = datetime.strptime(deadline_str, "%Y-%m-%d").date()
    if deadline == two_days_from_now:
        print(f"Reminder: Follow up for {position} at {company}")
