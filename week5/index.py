# question 1

# Base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def info(self):
        print(f"Smartphone: {self.brand} {self.model}, Storage: {self.storage}GB")

# Child class
class AndroidPhone(Smartphone):
    def __init__(self, brand, model, storage, version):
        super().__init__(brand, model, storage)
        self.version = version

    def update_os(self):
        print(f"{self.model} is updating to Android version {self.version}")

# Creating objects
phone1 = Smartphone("Apple", "iPhone 13", 128)
phone2 = AndroidPhone("Samsung", "Galaxy S21", 256, "13.0")

phone1.info()
phone1.call("0700000000")

phone2.info()
phone2.call("0711111111")
phone2.update_os()
#question 2----------------------------------------------
class Vehicle:
    def move(self):
        print("The vehicle moves.")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚢")

# Using polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
