
# Integrated Student Record Consistency Checker

students = [
    (101, "Ravi", [85, 90, 78], 92, "Python"),
    (102, "Sita", [88, 76, 95], 85, "Java"),
    (101, "Kiran", [70, 80, 75], 90, "Python"),
    (103, "", [65, 110, 70], 105, "C"),
    (104, "Anu", [80, None, 85], 75, ""),
    (105, "Rahul", [90, 85, 88], 95, "Python")
]

seen_ids = set()

print("STUDENT RECORD CONSISTENCY CHECKER")
print("-" * 40)

for student in students:
    sid, name, marks, attendance, course = student
    errors = []

    # Check student ID
    if sid is None or sid == "":
        errors.append("Missing student ID")
    elif sid in seen_ids:
        errors.append("Duplicate student ID")
    else:
        seen_ids.add(sid)

    # Check student name
    if not isinstance(name, str) or not name.strip():
        errors.append("Missing student name")

    # Check marks
    if not isinstance(marks, (list, tuple)) or len(marks) == 0:
        errors.append("Missing marks")
    else:
        for mark in marks:
            if mark is None or mark == "":
                errors.append("Missing marks")
                break
            if (not isinstance(mark, (int, float))
                    or isinstance(mark, bool)
                    or not 0 <= mark <= 100):
                errors.append("Invalid marks")
                break

    # Check attendance
    if attendance is None or attendance == "":
        errors.append("Missing attendance")
    elif (not isinstance(attendance, (int, float))
          or isinstance(attendance, bool)
          or not 0 <= attendance <= 100):
        errors.append("Invalid attendance")

    # Check course
    if not isinstance(course, str) or not course.strip():
        errors.append("Missing course")

    # Display results
    print(f"\nStudent ID: {sid}")
    print(f"Name: {name}")
    print(f"Marks: {marks}")
    print(f"Attendance: {attendance}%")
    print(f"Course: {course}")

    if errors:
        print("Status: ERROR")
        for error in errors:
            print("-", error)
    else:
        print("Status: VALID")

print("\nRecord checking completed.")
