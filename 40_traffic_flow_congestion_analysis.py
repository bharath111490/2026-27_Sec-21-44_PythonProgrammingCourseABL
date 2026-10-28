# Traffic Flow and Congestion Analysis

roads = int(input("Enter number of roads: "))
intervals = int(input("Enter number of time intervals: "))
capacity = int(input("Enter road capacity threshold: "))

peak_traffic = 0
peak_road = ""
peak_interval = 0

for i in range(roads):
    road_name = input(f"\nEnter name of Road {i+1}: ")

    total_vehicles = 0
    exceeded = False

    for j in range(intervals):
        count = int(input(f"Vehicles during Interval {j+1}: "))

        total_vehicles += count

        # Find peak traffic
        if count > peak_traffic:
            peak_traffic = count
            peak_road = road_name
            peak_interval = j + 1

        # Check capacity threshold
        if count > capacity:
            exceeded = True

    average = total_vehicles / intervals

    # Congestion Classification
    if average < 0.5 * capacity:
        congestion = "Low"
    elif average <= capacity:
        congestion = "Moderate"
    else:
        congestion = "High"

    print(f"\nRoad: {road_name}")
    print(f"Average Traffic: {average:.2f}")
    print(f"Congestion Level: {congestion}")

    if exceeded:
        print("Status: Capacity Threshold Exceeded")
    else:
        print("Status: Within Capacity")

print("\nPeak Traffic Analysis")
print(f"Road: {peak_road}")
print(f"Interval: {peak_interval}")
print(f"Vehicle Count: {peak_traffic}")
