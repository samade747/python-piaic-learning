# Single and double quotes
single_quote_string = 'Hello'
double_quote_string = "World"

print(single_quote_string)  # Output: Hello
print(double_quote_string)  # Output: World




# Multiline string
multiline_string = '''This is a
multiline string.'''
print(multiline_string)


# Accessing characters
greeting = "Hello"
print(greeting[0])  # First character: H
print(greeting[-1]) # Last character: o


# Combining strings
first_name = "Alice"
last_name = "Johnson"

full_name = first_name + " " + last_name
print(full_name)  # Output: Alice Johnson


name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")  # Output: My name is Alice and I am 25 years old.

print("My name is {} and I am {} years old.".format(name, age))

# type casting
print(f"My name is {name} and I am {age} years old.")  # Output: My name is Alice and I am 25 years old.

print("My name is %s and I am %d years old." % (name, age))  # Output: My name is Alice and I am 25 years old.

#one more example of %d and %s
name = "samad"
age = 25
skill = "Mern stack"
job = "developer"
gitub = "https://github.com/samade747"
linkedin = "https://www.linkedin.com/in/samaddeveloper/"
current_company = "pakistan stock exchange"


message: str = f"***
name: {name} 
age: {age} old.
skill: {skill} developer
jog: {job}
github: {gitub}
linkedin: {linkedin}
current company: {current_company}
***"    

print(message)


print("My name is %s and I am %d years old." % (name, age))  # Output: My name is samad and I am 25 years old.
print("My name is %s and I am %d years old and I am a %s developer." % (name, age, skill))  # Output: My name is samad and I am 25 years old.


print ("My name is " + name + " and I am " + str(age) + " years old.")  # Output: My name is Alice and I am 25 years old.

print ("My name is " + name + " and I am " + str(age) + " years old.")  # Output: My name is Alice and I am 25 years old.

#suugetion for f string 
print(f"My name is {name} and I am {age} years old.")  # Output: My name is Alice and I am 25 years old.
print(f"My name is {name} and I am {age} years old and I am a {skill} developer.")  # Output: My name is Alice and I am 25 years old.



text = "  Python Programming  "

# Changing case
print(text.upper())   # PYTHON PROGRAMMING
print(text.lower())   # python programming

# Removing whitespace
print(text.strip())   # Python Programming

# Splitting and joining
words = text.strip().split()  # ['Python', 'Programming']
print(" ".join(words))        # Python Programming

# Finding and replacing
print(text.find("Pro"))       # 8 (index of "Pro")
print(text.replace("Python", "JavaScript"))  # JavaScript Programming


text = "Hello, World!"
print(text[0:5])   # Hello
print(text[:5])    # Hello (same as above)
print(text[7:])    # World!


# Checking for a substring
text = "Python is awesome"
print("Python" in text)      # True
print("Java" not in text)    # True


# Using special characters
text = "She said, \"Python is fun!\""
print(text)  # She said, "Python is fun!"

# Task: Input your first and last name, then display a greeting message.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print(f"Hello, {first_name} {last_name}! Welcome to Python programming.")


#methods of string how to get list of methods of string
[print(method) for method in dir(str) if not method.startswith("_")]
# capitalize()	Converts the first character to upper case  
# casefold()	Converts string into lower case  
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string to the specified number of spaces
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning
# Task: Input a string and check if it is a palindrome.
string = input("Enter a string: ")

if string == string[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")   
# Task: Input a string and check if it is a palindrome.

# Task: Input a string and check if it is a palindrome.
string = input("Enter a string: ")

if string == string[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

# Task: Input a string and check if it is a palindrome.
string = input("Enter a string: ")

if string == string[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


# Task: Input a string and check if it is a palindrome.
string = input("Enter a string: ")

if string == string[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

# Task: Input a string and check if it is a palindrome.
string = input("Enter a string: ")

if string == string[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

# Task: Input a string and check if it is a palindrome.
string = input("Enter a string: ")

if string == string[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")



