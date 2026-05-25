student_name = "John"
topic = "Loops"
date = "27 May 2026"
time = "08:00 AM"
mode = "Online"
sender_name = "Veerendra"

email = f"""
Dear {student_name},

This is to inform you that the Python class is scheduled as per the details below:

Subject: Python Programming
Topic: {topic}
Date: {date}
Time: {time}
Mode: {mode}

Please join the session on time.

Best Regards,
{sender_name}
"""

print(email)