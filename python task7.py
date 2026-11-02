# Campus Resource Allocation Under Constraints

# Available equipment in the campus
available = {
    "Projector": 5,
    "Laptop": 10,
    "Microphone": 4
}

# Equipment required for each activity
activities = {
    "Hackathon": {"Projector": 2, "Laptop": 6, "Microphone": 2},
    "Seminar": {"Projector": 3, "Laptop": 4, "Microphone": 3},
    "Workshop": {"Projector": 2, "Laptop": 5, "Microphone": 1}
}

# Priority order (highest priority first)
priority = ["Hackathon", "Seminar", "Workshop"]

print("Available Resources:", available)
print("\nResource Allocation Report")

for activity in priority:
    print("\nActivity:", activity)

    for equipment, required in activities[activity].items():
        allocated = min(required, available[equipment])
        shortage = required - allocated

        available[equipment] -= allocated

        print(equipment,
              "| Required:", required,
              "| Allocated:", allocated,
              "| Shortage:", shortage)

print("\nRemaining Resources:", available)