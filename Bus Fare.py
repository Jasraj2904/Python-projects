class Vehicle:
    def __init__(self, name, max_speed, mileage , capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def display_details(self):
        print(f"Vehicle Name: {self.name}")
        print(f"Maximum Speed: {self.max_speed} km/h")
        print(f"Mileage: {self.mileage} km/l")
        print(f"Capacity: {self.capacity}")

    def fare(self):
        return self.capacity * 100
class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare()
        total_fare = base_fare + (0.1 * base_fare)
        return total_fare
    
school_bus = Bus("School Volvo" , 180 , 12 , 50)

print("Deatils of the School Bus : ")

school_bus.display_details()

print(f"Total Bus Fare: ₹{school_bus.fare()}")