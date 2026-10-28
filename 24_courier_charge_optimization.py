# Courier Charge Optimization

weight = float(input("Enter parcel weight (kg): "))
length = float(input("Enter parcel length (cm): "))
width = float(input("Enter parcel width (cm): "))
height = float(input("Enter parcel height (cm): "))
zone = int(input("Enter distance zone (1-Local, 2-State, 3-National): "))
urgent = input("Urgent delivery? (Y/N): ").upper()
restricted = input("Restricted item? (Y/N): ").upper()

# Check restrictions
if restricted == "Y":
    print("Parcel rejected due to declared restrictions.")
else:
    volume = length * width * height

    # Size charge
    if volume <= 5000:
        size_charge = 20
    elif volume <= 15000:
        size_charge = 50
    else:
        size_charge = 100

    # Distance charge
    if zone == 1:
        distance_charge = 50
    elif zone == 2:
        distance_charge = 100
    else:
        distance_charge = 200

    # Service options
    standard = (weight * 20) + size_charge + distance_charge
    express = (weight * 35) + size_charge + distance_charge

    if urgent == "Y":
        selected_service = "Express"
        final_charge = express
    else:
        selected_service = "Standard"
        final_charge = standard

    print("\nCourier Service Comparison")
    print(f"Standard Charge: ₹{standard:.2f}")
    print(f"Express Charge : ₹{express:.2f}")

    print(f"\nSelected Service: {selected_service}")
    print(f"Final Delivery Charge: ₹{final_charge:.2f}")