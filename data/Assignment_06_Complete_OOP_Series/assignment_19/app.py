# callable() and __call__()
# Create a class Multiplier with an __init__() to set a factor. Define a __call__()
#  method that multiplies an input by the factor. Test it with callable() and by calling 
# the object like a function.


class Multiplier:
    def __init__(self, factor):
        # Factor set kar rahe hain jisse multiplication hoga
        self.factor = factor

    def __call__(self, num):
                # Ye __call__ method hai jo number ko factor se multiply karega
        return num * self.factor



# Object bana rahe hain multiplier ka
multiply_by_3 = Multiplier(3)

# callable() se check kar rahe hain agar object ko call kiya ja sakta hai
print(callable(multiply_by_3))  # Output: True, kyunki humne __call__ method define kiya hai

# Ab multiply_by_3 ko function ki tarah call karte hain
result = multiply_by_3(5)  # 5 ko 3 se multiply karenge
print(result)  # Output: 15, kyunki 5 * 3 = 15