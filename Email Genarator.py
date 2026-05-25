print("\n==============================")
print("      EMAIL GENERATOR")
print("==============================")

student_name = input("\nEnter student name: ")
course_name = input("Enter course name: ")
topic = input("Enter topic: ")
date = input("Enter class date: ")
time = input("Enter class time: ")
mode = input("Enter class mode: ")

email = f"""
----------------------------------------

Dear {student_name},

This is to inform you that your class
has been scheduled successfully.

Class Details:
----------------------------------------
Course : {course_name}
Topic  : {topic}
Date   : {date}
Time   : {time}
Mode   : {mode}
----------------------------------------

Please attend the session on time.

Best Regards,
Veerendra Kalyan Babu 🚀

----------------------------------------
"""

print(email)