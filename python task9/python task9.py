
# Smart Classroom Timetable Allocation

# Courses: (Course Name, Number of Students)
courses = [
    ("Python", 40),
    ("Java", 30),
    ("AI", 50),
    ("DBMS", 35)
]

# Classrooms: (Room Name, Capacity)
rooms = [
    ("Room A", 45),
    ("Room B", 35),
    ("Room C", 60)
]

# Available periods
periods = ["9-10 AM", "10-11 AM", "11-12 PM"]

# Store timetable allocations
timetable = []

# Track occupied rooms and periods
occupied = set()

# Allocate classrooms
for course, students in courses:
    allocated = False

    for room, capacity in rooms:
        if capacity < students:
            continue

        for period in periods:
            if (room, period) not in occupied:
                timetable.append((course, room, period, students))
                occupied.add((room, period))
                allocated = True
                break

        if allocated:
            break

    if not allocated:
        print("Cannot schedule:", course,
              "- No suitable room or period available.")

# Display timetable
print("\nSMART CLASSROOM TIMETABLE")
print("-" * 60)

for course, room, period, students in timetable:
    print("Course:", course)
    print("Room:", room)
    print("Period:", period)
    print("Students:", students)
    print("-" * 60)

# Check for clashes
print("\nCLASH CHECK")

clashes = False

for i in range(len(timetable)):
    for j in range(i + 1, len(timetable)):
        if timetable[i][1] == timetable[j][1] and \
           timetable[i][2] == timetable[j][2]:
            print("Clash:", timetable[i][0],
                  "and", timetable[j][0])
            clashes = True

if not clashes:
    print("No classroom clashes found.")

# Check whether all courses are scheduled
if len(timetable) == len(courses):
    print("Result: All courses scheduled successfully.")
else:
    print("Result: Some courses could not be scheduled.")
