# Polymorphism = greek word that means to "have many forms or faces"
  # poly = Many
  # Morphe = Form

# two ways to achieve polymorphism
# 1. inheritance = an object could be treated of the same type as a parent class
# 2. Duck typing = object must have neccsary attributes / methods

from abc import ABC, abstractmethod

class Shape:
   
   @abstractmethod
   def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

shapes = [Circle(7), Square(5), Triangle(3, 6)]