
# this is a class

class House:
    address:str = "samad house no. 313"
    number_of_doors: int = 5
    number_of_rooms: int = 3

# this is an object 
samad_house = House()

print(samad_house.address)
print(samad_house.number_of_doors)
print(samad_house.number_of_rooms)

print(f"samad house has {samad_house.number_of_doors} doors")
print(f"samad house has {samad_house.number_of_rooms} rooms")

