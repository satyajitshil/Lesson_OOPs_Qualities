
class Vehicle:
    def __init__(self, name, max_speed, mileage ):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass

bus = Bus("School Volvo", 110, 12)
print("Vehicle Name:",bus.name,"Speed:",bus.max_speed,"Mileage:",bus.mileage)
    