# Food Waste Monitoring System

days = int(input("Enter number of days: "))
acceptable_limit = float(input("Enter acceptable wastage percentage: "))

high_waste_days = []

for day in range(1, days + 1):
    print(f"\nDay {day}")

    prepared = int(input("Meals prepared: "))
    served = int(input("Meals served: "))
    leftovers = int(input("Leftover meals: "))

    wastage = leftovers
    wastage_percent = (wastage / prepared) * 100

    print(f"Wastage Percentage: {wastage_percent:.2f}%")

    if wastage_percent > acceptable_limit:
        high_waste_days.append(day)

print("\nFood Waste Report")

if len(high_waste_days) == 0:
    print("No days exceeded the acceptable wastage limit.")
else:
    print("Days exceeding acceptable wastage limit:")
    for day in high_waste_days:
        print(f"Day {day}")