#Duck typing in pyhton = another way to achieve polymorphism besides inheritance
# object must have the minimun neccesary attriubtues /methods

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Woof woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

animals = [Dog(), Cat()]:

for animal in animals:
    animal.speak()
    print(animal.alive)

