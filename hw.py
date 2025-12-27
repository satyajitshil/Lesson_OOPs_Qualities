class Vehicle:
    def __init__(self,fare,seat):
        self.fare = fare

class Bus(Vehicle):
    def __init__(self, seat):
        self.fare = (50 * 100) * (1/10)

obj = Bus()
print(obj)



        