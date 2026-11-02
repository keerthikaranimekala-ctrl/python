
from datetime import datetime
import math

# Parking rates per hour
rates = {
    "bike": 20,
    "car": 50,
    "truck": 80
}

# Maximum charge per day
daily_limit = {
    "bike": 150,
    "car": 400,
    "truck": 600
}

# Penalty for invalid or lost parking ticket
penalty = 200

print("===== SMART PARKING FEE MANAGEMENT =====")

vehicle = input("Enter vehicle type (bike/car/truck): ").lower()

if vehicle not in rates:
    print("Invalid vehicle type!")
else:
    entry = input("Enter entry time (YYYY-MM-DD HH:MM): ")
    exit_time = input("Enter exit time (YYYY-MM-DD HH:MM): ")

    try:
        entry_time = datetime.strptime(entry, "%Y-%m-%d %H:%M")
        leaving_time = datetime.strptime(
            exit_time, "%Y-%m-%d %H:%M"
        )

        if leaving_time <= entry_time:
            print("Error: Exit time must be after entry time.")

        else:
            # Calculate parking duration
            duration = leaving_time - entry_time
            total_hours = duration.total_seconds() / 3600
            hours = math.ceil(total_hours)

            # Calculate number of calendar days
            days = (leaving_time.date() - entry_time.date()).days + 1

            # Calculate basic parking fee
            hourly_fee = hours * rates[vehicle]

            # Apply daily parking limit
            maximum_fee = days * daily_limit[vehicle]
            parking_fee = min(hourly_fee, maximum_fee)

            # Overnight charge
            overnight_fee = 0
            if leaving_time.date() > entry_time.date():
                overnight_fee = 100

            # Penalty for parking over 24 hours
            extra_penalty = 0
            if total_hours > 24:
                extra_penalty = penalty

            total_fee = (
                parking_fee + overnight_fee + extra_penalty
            )

            print("\n===== PARKING BILL =====")
            print("Vehicle Type:", vehicle.title())
            print("Entry Time:", entry_time)
            print("Exit Time:", leaving_time)
            print("Parking Duration:", round(total_hours, 2), "hours")
            print("Charged Hours:", hours)
            print("Parking Fee: Rs.", parking_fee)
            print("Overnight Fee: Rs.", overnight_fee)
            print("Penalty: Rs.", extra_penalty)
            print("Total Amount: Rs.", total_fee)

    except ValueError:
        print("Invalid date or time format!")
        print("Use YYYY-MM-DD HH:MM")
