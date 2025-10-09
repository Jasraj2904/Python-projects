class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def display_details(self):
        print(f"Vehicle Name: {self.name}")
        print(f"Maximum Speed: {self.max_speed} km/h")
        print(f"Mileage: {self.mileage} km/l")
class Bus(Vehicle):
    pass  

school_bus = Bus("School Volvo", 180, 12)

print("Details of the Vehicle Bus:")
school_bus.display_details()