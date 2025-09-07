def trip_expennditure():
    hotel_per_day = float(input("Enter hotel cost per day : "))
    days = int(input("Enter number of days stayed : "))
    total_hotel_cost = hotel_per_day * days

    plane_cost = float(input("Enter price of Plane's ticket : "))

    vehicle_cost = float(input("Enter the vehicle rental cost  :"))

    total = total_hotel_cost + plane_cost + vehicle_cost

    print("\n === Trip Expense Breakdown ===")
    print(f"Hotel Cost({days} days)  : ₹{total_hotel_cost}")
    print(f"Plane Cost : ₹{plane_cost}")
    print(f"Vehicle Rental Cost : ₹{vehicle_cost}")
    print("---------------------------------")
    print(f"Total Trip Expenditure : ₹{total}")

trip_expennditure()