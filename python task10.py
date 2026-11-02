
# Integrated Manufacturing Production Planner

# Raw materials available
raw_materials = {
    "Steel": 100,
    "Plastic": 80,
    "Rubber": 50
}

# Raw materials required for one product
material_required = {
    "Steel": 2,
    "Plastic": 1,
    "Rubber": 1
}

# Production and order details
production_quantity = 40
order_demand = 45
defect_count = 3
max_defect_limit = 5

print("MANUFACTURING PRODUCTION PLANNER")
print("-" * 35)

# Check raw material availability
max_possible = production_quantity

for material in material_required:
    possible = raw_materials[material] // material_required[material]
    if possible < max_possible:
        max_possible = possible

print("Planned Production:", production_quantity)
print("Order Demand:", order_demand)
print("Maximum Possible Production:", max_possible)

# Check production feasibility
if max_possible >= production_quantity:
    print("Material Status: Sufficient")
else:
    print("Material Status: Insufficient")
    print("Material Shortages:")

    for material in material_required:
        required = production_quantity * material_required[material]
        available = raw_materials[material]

        if required > available:
            print(material, "shortage:", required - available)

# Calculate good products after defects
good_products = production_quantity - defect_count

print("Defective Products:", defect_count)
print("Good Products:", good_products)

# Check order demand
if good_products >= order_demand:
    print("Order Status: Demand can be fulfilled")
else:
    print("Order Status: Demand cannot be fulfilled")
    print("Product Shortage:", order_demand - good_products)

# Check quality violations
if defect_count > max_defect_limit:
    print("Quality Status: Violation detected")
else:
    print("Quality Status: Within defect limit")

# Final production report
print("-" * 35)
if (max_possible >= production_quantity
        and good_products >= order_demand
        and defect_count <= max_defect_limit):
    print("FINAL STATUS: Production is feasible")
else:
    print("FINAL STATUS: Production needs attention")