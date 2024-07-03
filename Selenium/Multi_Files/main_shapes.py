from Selenium.Multi_Files.Util.math_util import add, product
from Selenium.Multi_Files.shapes.circle import Circle
from Selenium.Multi_Files.shapes.rectangle import Rectangle


def test():
    c1 = Circle(7)
    print(f"radius of Circle, {c1.radius}")
    print(f"Area of Circle, {c1.area()}")
    print(f"Circumference of Circle, {c1.circumference()}")

    r1 = Rectangle(5, 10)
    print(f"Length of rectangle {r1.length},Breadth of rectangle {r1.breadth}")
    print(f"Area of Rectangle, {r1.area()}")
    print(f"Perimeter of Rectangle, {r1.perimeter()}")

    print(f"print sum of 2 numbers, {add(2, 5)}")
    print(f"print product of 2 numbers, {product(2, 5)}")


test()
