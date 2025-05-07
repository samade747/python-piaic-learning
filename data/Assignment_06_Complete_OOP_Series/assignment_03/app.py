# 3. Public Variables and Methods
# Create a class Car with a public variable brand and a public method start(). 
# Instantiate the class and access both from outside the class.


class Car:
    # Public variable (can be accessed directly from outside the class)
    brand = "Toyota"


    # Public method (can be called from outside the class)
    def start(self):
        print(f"The {self.brand} car has started.")


# Class ko instantiate karte hain
my_car = Car()  # Car ka object banaya


# Public variable ko access karte hain
print("Car Brand:", my_car.brand)  # "Toyota" print karega

# Public method ko call karte hain
my_car.start()  # "The Toyota car has started." print karega