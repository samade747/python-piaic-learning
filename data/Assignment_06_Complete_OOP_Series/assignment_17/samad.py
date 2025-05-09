# Class Decorators
# Create a class decorator add_greeting that modifies a class to add a greet()
# method returning "Hello from Decorator!". Apply it to a class Person.


# class devorator define kiya
def add_greeting(cls):
    #greet method define kar rahe hain jo object ka naam use hoga
    def greet(self):
        return f"Hello from {self.name} Greeting from Decorator!"

    cls.greet = greet  # class ko greet method add kar rahe hain
    return cls  # modified class return kar rahe hai    
