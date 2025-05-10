# Instance Methods
# Create a class Dog with instance variables name and breed. Add an instance method bark()
# that prints a message including the dog's name.

# Dog class define kiya
class Dog():
    def __init__(self,name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
         # Ye method dog ka naam use karke ek message print kiya
        print(f"{self.name} Is Breeking! woof woof")

dog1 = Dog("Buddy", "Golden Retriever")  # Dog object create kiya
dog1.bark()  # bark() method call kiya