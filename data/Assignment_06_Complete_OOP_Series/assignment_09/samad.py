#Abstract Classes and Methods
#Use the abc module to create an abstract class Shape with an abstract method area(). 
# Inherit a class Rectangle that implements area().



# 💡 What is an Abstract Class?
# An abstract class is like a blueprint for other classes. It:

# Cannot be used directly to create objects

# Can have abstract methods, which are methods without implementation

# Forces any class that inherits it to implement those methods

# Think of it like a contract — if you're building something from the blueprint, you must finish the parts it says.




# abc module se abstract base class ka support liya
from abc import ABC, abstractmethod


# Shape aik abstract class hai
class Shape(ABC):
    @abstractmethod

    def area(self): 
        pass  # Ye method sirf declare kiya, implement nahi kiya


# Rectangle class, Shape class se inherit karti hai
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
       return self.width * self.height # Area calculate kar ke return kar rahe hain
    

 # Rectangle ka object banaya jismein width 5 aur height 9 hai
rect = Rectangle(5,9)
print("Area of Rectangle",rect.area())