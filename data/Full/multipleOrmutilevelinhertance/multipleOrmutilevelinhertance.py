# multiple interitance = inherit from more than on parent class
                         # C(A, B)

# mutlilevel inheritance = inherit from a class that inherits from another class
                            # C(B) <- B(A) <- A
class Animal:
    def eat(self):
        print('The animal is eating')

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

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

hawk.flee()