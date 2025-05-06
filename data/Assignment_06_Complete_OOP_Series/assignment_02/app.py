# 2. Using cls
# Create a class Counter that keeps track of how many objects have been created. 
# Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count = 0 # yeh ek class var hai jo obj ki total count rakhta hai

    def __init__(self):
        # har bar naaya object banega, count mein 1 add hoga 
        Counter.count += 1


    # Yeh ek class method hai, jo class variable ko access karke count show karta hai
    @classmethod
    def show_count(cls):
          # yeh print karega total objects ka count
        print("Total Object Create :",cls.count)


# example usage
# Jab bhi naya object banta hai, count automatically barh jata hai
c1 = Counter() 
c2 = Counter()
c3 = Counter()

Counter.show_count() # output total objects created 3 