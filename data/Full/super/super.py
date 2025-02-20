# super() = Funtion that allows you to call a method from the parent class.
# allows you to extend the functionality of the inherited method.


# super class
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"Shape: {self.color}, {self.is_filled}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"if its is a circle with an area of {3.14 * self.radius * self.radius}cm^2")

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        super().describe()
        print(f"if its is a square with an area of {self.width * self.width}cm^2")
        

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height


Circle = Circle("red", True, 5)
Square = Square("blue", False, 10)
Triangle = Triangle("green", True, 15, 20)

print(f"Circle: {Circle.color}, {Circle.is_filled}, {Circle.radius}")
print(f"Square: {Square.color}, {Square.is_filled}, {Square.width}")
print(f"Triangle: {Triangle.color}, {Triangle.is_filled}, {Triangle.width}, {Triangle.height}")

Circle.describe()
Square.describe()
Triangle.describe()





 
