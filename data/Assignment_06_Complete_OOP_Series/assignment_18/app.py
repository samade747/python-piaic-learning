# Property Decorators: @property, @setter, and @deleter
# Create a class Product with a private attribute _price. Use @property to get the price,
#  @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        # yahan main price ka private variable bana raha hoon
        self._price = price


    @property
    def price(self):
        # ye property decorator use kiya hai taake price ko directly access kar sakein
        return self._price

    @price.setter
    def price(self, value):
        # agar mujhe price update karni ho to ye setter use hota hai
        # negative price ka check bhi rakha hai, just to be safe
        if value >= 0:
            self._price = value
        else:
           print("Price cannot be negative 😕")

    @price.deleter
    def price(self):
        # jab mujhe price delete karni ho to ye method chalega
        print("Deleting Price")  # thoda dramatic hai 😅
        del self._price

# ab main Product class ka object bana rahi hoon
p = Product(100)

# pehli baar price check kar rhe 
print(p.price)  # Output: 100

# ab price update kar rahe hain
p.price = 150

# check kar lete hoon ke price update hui ya nahi
print(p.price)  # Output: 150

# ab main price delete kar rahe hain
del p.price

# agar ab dubara print karun gi to error aayega because price delete ho chuki hai
# print(p.price)  # ye line error degi, isliye comment mein rakh rahe hain