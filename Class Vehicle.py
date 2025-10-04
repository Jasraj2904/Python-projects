class vehicle:
    def __init__(self , max_speed , mileage):
        self.max_speed = max_speed
        self.mileage = mileage
modelX = vehicle(240 , 20)
print(modelX.max_speed)
print(modelX.mileage)