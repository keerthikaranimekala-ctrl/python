
# Multi-Plan Telecommunications Cost Optimization

# User requirements
data_needed = 2.5       # GB per day
calls_needed = 100      # Minutes per day
sms_needed = 20         # SMS per day
required_validity = 28  # Days
budget = 500            # Maximum budget in rupees

# Mobile plans
plans = [
    {
        "name": "Plan A",
        "price": 199,
        "data": 2,
        "calls": 100,
        "sms": 100,
        "validity": 28,
        "extra_data_charge": 20
    },
    {
        "name": "Plan B",
        "price": 299,
        "data": 3,
        "calls": 150,
        "sms": 100,
        "validity": 28,
        "extra_data_charge": 15
    },
    {
        "name": "Plan C",
        "price": 399,
        "data": 4,
        "calls": 200,
        "sms": 100,
        "validity": 56,
        "extra_data_charge": 10
    }
]

eligible_plans = []

print("MOBILE PLAN COST COMPARISON")
print("-" * 55)

for plan in plans:
    # Calculate total usage for the validity period
    total_data_needed = data_needed * plan["validity"]
    total_calls_needed = calls_needed * plan["validity"]
    total_sms_needed = sms_needed * plan["validity"]

    # Calculate excess usage charges
    excess_data = max(
        0, total_data_needed - plan["data"] * plan["validity"]
    )
    excess_calls = max(
        0, total_calls_needed - plan["calls"] * plan["validity"]
    )
    excess_sms = max(
        0, total_sms_needed - plan["sms"] * plan["validity"]
    )

    # Example excess charges
    data_charge = (
        excess_data / 1.0
    ) * plan["extra_data_charge"]

    call_charge = excess_calls * 0.50
    sms_charge = excess_sms * 0.25

    total_cost = (
        plan["price"] + data_charge
        + call_charge + sms_charge
    )

    # Check requirements and budget
    meets_usage = (
        plan["data"] >= data_needed
        and plan["calls"] >= calls_needed
        and plan["sms"] >= sms_needed
    )

    meets_validity = plan["validity"] >= required_validity
    meets_budget = total_cost <= budget

    print(f"\n{plan['name']}: Rs.{plan['price']}")
    print(f"Excess charges: Rs.{data_charge + call_charge + sms_charge:.2f}")
    print(f"Total estimated cost: Rs.{total_cost:.2f}")

    if meets_usage and meets_validity and meets_budget:
        eligible_plans.append((plan["name"], total_cost))

# Find the cheapest eligible plan
print("\n" + "-" * 55)

if eligible_plans:
    best_plan = min(eligible_plans, key=lambda x: x[1])
    print("Most economical eligible plan:")
    print("Plan:", best_plan[0])
    print(f"Total Cost: Rs.{best_plan[1]:.2f}")
else:
    print("No plan satisfies all the requirements and budget.")
