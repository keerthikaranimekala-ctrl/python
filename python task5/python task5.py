
# Weekly Electricity Consumption Matrix

days = ["Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"]

appliances = ["Fan", "Light", "TV"]

readings = {}

# Input electricity consumption for each appliance
for appliance in appliances:
    print("\nEnter daily consumption for", appliance, "(in kWh):")
    readings[appliance] = []

    for day in days:
        while True:
            try:
                units = float(input(day + ": "))
                if units < 0:
                    print("Consumption cannot be negative.")
                    continue
                readings[appliance].append(units)
                break
            except ValueError:
                print("Please enter a valid number.")

# Calculate appliance-wise totals
print("\n--- Appliance-wise Weekly Totals ---")

for appliance in appliances:
    total = sum(readings[appliance])
    print(appliance, ":", total, "kWh")

# Calculate daily totals
print("\n--- Daily Electricity Consumption ---")

daily_totals = []

for i in range(7):
    total = sum(readings[a][i] for a in appliances)
    daily_totals.append(total)
    print(days[i], ":", total, "kWh")

# Check consumption limits
daily_limit = float(input("\nEnter daily consumption limit (kWh): "))
appliance_limit = float(input("Enter weekly appliance limit (kWh): "))

print("\n--- Daily Limit Check ---")

for i in range(7):
    if daily_totals[i] > daily_limit:
        print(days[i], "exceeds the daily limit!")

print("\n--- Appliance Limit Check ---")

for appliance in appliances:
    total = sum(readings[appliance])

    if total > appliance_limit:
        print(appliance, "exceeds the weekly limit!")
    else:
        print(appliance, "is within the weekly limit.")

print("\nTotal weekly consumption:",
      sum(daily_totals), "kWh")
