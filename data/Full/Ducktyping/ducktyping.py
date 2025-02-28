# Duck typing in Python is another way to achieve polymorphism besides inheritance.
# It allows objects to be used interchangeably if they have the required attributes/methods.

# Base class
class Animal:
    alive = True  # Class attribute indicating if the object is alive

# Dog class inherits from Animal
class Dog(Animal):
    def speak(self):  # Method to make a sound
        print("Woof woof")

# Cat class inherits from Animal
class Cat(Animal):
    def speak(self):  # Method to make a sound
        print("Meow")

# Car class does NOT inherit from Animal but has the same method and attribute
class Car:
    alive = False  # Class attribute indicating it's not alive
    
    def speak(self):  # Method to make a sound
        print("Honk honk")

# Creating a list of different objects that have a 'speak' method
animals = [Dog(), Cat(), Car()]  # Removed colon (syntax error)

# Iterating through the list and calling the 'speak' method on each object
for animal in animals:
    animal.speak()  # Calls the respective 'speak' method
    print(animal.alive)  # Prints whether the object is alive or not


# #Duck typing in pyhton = another way to achieve polymorphism besides inheritance
# # object must have the minimun neccesary attriubtues /methods

# class Animal:
#     alive = True

# class Dog(Animal):
#     def speak(self):
#         print("Woof woof")

# class Cat(Animal):
#     def speak(self):
#         print("Meow")


# class Car:

#     alive = False

#     def speak(self):
#         print("Honk honk")


# animals = [Dog(), Cat(), Car()]:

# for animal in animals:
#     animal.speak()
#     print(animal.alive)

