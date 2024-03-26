class Vehicle:
    def __init__(self, make, model, color, year):
        self.make = make
        self.model = model
        self.color = color
        self.year = year

    def __str__(self):
        return f"{self.make} {self.model} {self.color} {self.year}"


class Car(Vehicle):
    def __init__(self, make, model, color, year, num_doors):
        super().__init__(make, model, color, year)
        self.num_doors = num_doors

    def hock(self):
        return "Car Hocks"


class Truck(Vehicle):
    def __init__(self, make, model, color, year, pay_load):
        super().__init__(make, model, color, year)
        self.payload = pay_load

    def large_cargo(self):
        return "carries cargo"


class Motorcycle(Vehicle):
    def __init__(self, make, model, color, year, num_wheels):
        super().__init__(make, model, color, year)
        self.num_wheels = num_wheels

    def wheeling(self):
        return "Wheeling on roads"


car1 = Car('TATA', 'altroz', 'white', 2021, 4)
print(car1.hock())
print(car1.year)

t1 = Truck("ASHOK", 'Layland', 'gray', 2000, 20)
print(t1.large_cargo())
print(t1.payload)

m1 = Motorcycle('HOnda', '110cc', 'red', 2013, 2)
print(m1.wheeling())
print(m1.num_wheels)
