#inhteritance = allows a class to interhit attributes and methods from another class
#parent class = the class being inherited from
# helps with code reusability and readability
# class child_class(parent_class):



class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")



class Dog(Animal):
    def speak(self):
        print(f"{self.name} is barking")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} is meowing")

class Mouse(Animal):
    def speak(self):
        print(f"{self.name} is squeaking")


dog = Dog("scooby")
cat = Cat("tom")
mouse = Mouse("jerry")

mouse.speak()