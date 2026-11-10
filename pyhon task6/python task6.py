# Tuple-Based Transaction Audit

transactions = [
    (101, 500, "DEPOSIT"),
    (102, 1000, "WITHDRAWAL"),
    (101, 700, "DEPOSIT"),
    (103, -200, "WITHDRAWAL"),
    (104, 5000, "DEPOSIT"),
    (105, 200, "UNKNOWN")
]

seen_ids = set()
previous_amount = None

print("Transaction Audit Report")
print("-" * 30)

for transaction in transactions:
    tid, amount, ttype = transaction
    issues = []

    # Check duplicate transaction ID
    if tid in seen_ids:
        issues.append("Duplicate ID")
    else:
        seen_ids.add(tid)

    # Check invalid amount
    if amount <= 0:
        issues.append("Invalid amount")

    # Check transaction type
    if ttype not in ("DEPOSIT", "WITHDRAWAL"):
        issues.append("Invalid transaction type")

    # Check suspicious sequence
    if previous_amount is not None and amount > 3 * previous_amount:
        issues.append("Suspicious amount increase")

    previous_amount = amount

    if issues:
        print(f"Transaction {tid}: {', '.join(issues)}")
    else:
        print(f"Transaction {tid}: Valid")

print("-" * 30)
print("Audit completed.")
