#shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit):")
    if food.lower() == "q":
        break
    else:
        price = float(input("Enter the price of the food: {food} $"))
        foods.append(food)
        prices.append(price)


print("Here is your shopping cart:")
for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print(f"Your total is: ${total}")
