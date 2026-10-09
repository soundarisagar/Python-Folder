class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

model_1 = Vehicle(240, 18)

print("Max speed of model_1:", model_1.max_speed)
print("Mileage of model_1:", model_1.mileage)