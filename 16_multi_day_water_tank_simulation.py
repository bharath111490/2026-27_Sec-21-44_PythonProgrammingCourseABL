# Multi-Day Water Tank Simulation

capacity = float(input("Enter tank capacity (liters): "))
current_level = float(input("Enter initial water level (liters): "))
threshold = float(input("Enter threshold level (liters): "))
days = int(input("Enter number of days: "))

first_threshold_day = -1

for day in range(1, days + 1):
    print(f"\nDay {day}")

    inflow = float(input("Enter inflow amount: "))
    outflow = float(input("Enter outflow amount: "))

    current_level = current_level + inflow - outflow

    if current_level > capacity:
        overflow = current_level - capacity
        current_level = capacity
        print(f"Overflow detected: {overflow:.2f} liters lost")

    elif current_level < 0:
        shortage = abs(current_level)
        current_level = 0
        print(f"Water shortage: {shortage:.2f} liters")

    print(f"Current Water Level: {current_level:.2f} liters")

    if first_threshold_day == -1 and current_level >= threshold:
        first_threshold_day = day

print()

print(f"Final Water Level: {current_level:.2f} liters")

if first_threshold_day != -1:
    print(f"Threshold first reached on Day {first_threshold_day}")
else:
    print("Threshold was never reached")