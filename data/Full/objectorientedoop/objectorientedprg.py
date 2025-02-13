
from car import Car

car1 = Car("Toyota", 2019, "Red", True)
car2 = Car("Honda", 2020, "Blue", False)
car3 = Car("Ford", 2018, "Black", True)


print(car1.model)
print(car2.year)
print(car3.color)
print(car1.for_sale)
print(car2.for_sale)
print(car3.for_sale)

car1.describe