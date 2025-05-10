# Creating a Custom Exception
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises 
# this exception if age < 18. Handle it with try...except.


# Custom exception class banate hain
class InvalidAgeError(Exception):
    # Exception message define kar rahe hain
    def __init__(self, message="Age must be 18 or older."):
        self.message = message
        super().__init__(self.message)

# Function jismein age check karenge
def check_age(age):
    # Agar age 18 se kam hai, to custom exception raise karenge
    if age < 18:
        raise InvalidAgeError("Sorry, you must be at least 18 years old.")  # Custom exception ko raise kar rahe hain
    else:
        return "You are eligible."

# Try-except block ke saath exception handle karenge
try:
    # Test kar rahe hain function ko ek invalid age ke saath
    result = check_age(16)
    print(result)
except InvalidAgeError as e:
    # Agar exception raise hota hai to yeh handle hoga
    print(f"Error: {e}")