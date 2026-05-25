students = []

print("\n==============================")
print("      STUDENT MANAGER")
print("==============================")

number_of_students = int(input("\nHow many students to add? "))

for i in range(number_of_students):

    print(f"\nEnter Details for Student {i + 1}")

    name = input("Name: ")
    city = input("City: ")
    marks = int(input("Marks: "))

    if marks >= 90:
        grade = "A"

    elif marks >= 75:
        grade = "B"

    elif marks >= 50:
        grade = "C"

    else:
        grade = "Fail"

    student = {
        "name": name,
        "city": city,
        "marks": marks,
        "grade": grade
    }

    students.append(student)

print("\n==============================")
print("      STUDENT RECORDS")
print("==============================")

for student in students:

    print(f"""
Name   : {student['name']}
City   : {student['city']}
Marks  : {student['marks']}
Grade  : {student['grade']}
------------------------------
""")