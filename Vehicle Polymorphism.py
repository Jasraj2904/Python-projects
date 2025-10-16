class BMW:
    def fuel_type(self):
        return "Petrol"
    def max_speed(self):
        return "The maximum speed of BMW is 250 km/h"
    
class Ferrari:
    def fuel_type(self):
        return "Petrol and Hybrid options"
    def max_speed(self):
        return "The maximum speed of Ferrari is 340 km/h"
    
def car_details(car):
    print(f"Fuel Type : {car.fuel_type()}")
    print(f"Max Speed : {car.max_speed()}")

BMW_car = BMW()
Ferrari_car = Ferrari()

car_details(BMW_car)
car_details(Ferrari_car)