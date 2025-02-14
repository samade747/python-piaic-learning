# multiple interitance = inherit from more than on parent class
                         # C(A, B)

# mutlilevel inheritance = inherit from a class that inherits from another class
                            # C(B) <- B(A) <- A
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('{self.name} is eating')

    def sleep(self):
        print('{self.name} is sleeping')




class Prey(Animal):
    def flee(self):
        print('The animal is fleeing')


class Predator(Animal):
    def hunt(self):
        print('The animal is hunting')


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bunny")
hawk = Hawk("Hawky")
fish = Fish("Fishy")

fish.eat()