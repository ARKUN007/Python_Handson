class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def __int__(self,brand, model):
        self.brand = brand
        self.model = model
class Plane(Vehicle):
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ferry", "Victoria")
plane1 = Plane("AirIndia", "908")

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()