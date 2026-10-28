# Repeated Transaction Detection

n = int(input("Enter number of transactions: "))
threshold = float(input("Enter suspicious amount threshold: "))

transaction_ids = set()
suspicious = []

for i in range(n):
    print(f"\nTransaction {i + 1}")

    tx_id = input("Enter Transaction ID: ")
    amount = float(input("Enter Amount: "))

    duplicate = False
    threshold_violation = False

    # Check duplicate transaction
    if tx_id in transaction_ids:
        duplicate = True
    else:
        transaction_ids.add(tx_id)

    # Check threshold violation
    if amount > threshold:
        threshold_violation = True

    # Add suspicious transactions
    if duplicate or threshold_violation:
        suspicious.append((tx_id, amount, duplicate, threshold_violation))

print("\nSuspicious Transactions")

if len(suspicious) == 0:
    print("No suspicious transactions found.")
else:
    for tx_id, amount, duplicate, threshold_violation in suspicious:
        print(f"\nTransaction ID: {tx_id}")
        print(f"Amount: ₹{amount:.2f}")

        if duplicate:
            print("Reason: Duplicate Transaction")

        if threshold_violation:
            print("Reason: Amount Exceeds Threshold")