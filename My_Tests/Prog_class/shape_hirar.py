class Shape:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"


class Rectangle(Shape):
    def __init__(self, name, length, breath):
        super().__init__(name)
        self.length = length
        self.breath = breath

    def area(self):
        return self.length * self.breath


class Triangle(Shape):
    def __init__(self, name, r1, r2, r3):
        super().__init__(name)
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3

    def peri(self):
        return self.r1 + self.r2 + self.r3


rect1 = Rectangle('Rect',5,5)
print(rect1.area())
print(str(rect1))

tri1 = Triangle("Tri",2,3,4)
print(tri1.peri())
print(str(tri1))