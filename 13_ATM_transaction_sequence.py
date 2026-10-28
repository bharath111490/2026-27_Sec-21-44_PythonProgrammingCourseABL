# ATM Transaction Sequence Simulation

balance = float(input("Enter initial balance: "))
num_transactions = int(input("Enter number of transactions: "))

WITHDRAWAL_LIMIT = 20000

deposit_count = 0
withdraw_count = 0
deposit_total = 0
withdraw_total = 0

for i in range(num_transactions):
    print(f"\nTransaction {i + 1}")

    transaction_type = input("Enter transaction type (D/W): ").upper()
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount! Transaction rejected.")
        continue

    if transaction_type == "D":
        balance += amount
        deposit_count += 1
        deposit_total += amount
        print("Deposit successful.")

    elif transaction_type == "W":

        if amount > WITHDRAWAL_LIMIT:
            print("Withdrawal exceeds limit! Transaction rejected.")

        elif amount > balance:
            print("Insufficient balance! Transaction rejected.")

        else:
            balance -= amount
            withdraw_count += 1
            withdraw_total += amount
            print("Withdrawal successful.")

    else:
        print("Invalid transaction type! Transaction rejected.")

# Transaction Summary
print("\n" + "=" * 40)
print("ATM TRANSACTION SUMMARY")
print("=" * 40)

print(f"Total Deposits      : {deposit_count}")
print(f"Deposit Amount      : ₹{deposit_total:.2f}")

print(f"Total Withdrawals   : {withdraw_count}")
print(f"Withdrawal Amount   : ₹{withdraw_total:.2f}")

print(f"Final Balance       : ₹{balance:.2f}")

print("=" * 40)