class BMW:
    def fuel_type(self):
        print("BMW runs on Petrol.")

    def max_speed(self):
        print("BMW max speed is 250 km/h.")


class Ferrari:
    def fuel_type(self):
        print("Ferrari runs on Petrol.")

    def max_speed(self):
        print("Ferrari max speed is 340 km/h.")


# Create objects
bmw = BMW()
ferrari = Ferrari()

# Implement polymorphism
for car in (bmw, ferrari):
    car.fuel_type()
    car.max_speed()