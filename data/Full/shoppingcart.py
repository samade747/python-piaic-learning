# Excercise 2 - Shopping Cart prgram

item = input("Enter the name of the item: ")
quantity = int(input("Enter the quantity: "))
price = float(input("Enter the price of the item: "))
total = quantity * price

print(f"Item: {item}")

print(f"Quantity: {quantity}")

print(f"Price: ${price}")

print(f"Total: ${total}")

print(f"Total: ${total:.2f}")
