# Loop and input from user
# while
# for
# controls
# break
# continue
# pass
# input with input function
# input from console
# Loop working on iterative data types
# list
# dictionary
# tuple
# string

#  >>>>>>>>

#                 0 1 2 3 4 5
l1 : list[int] = [1,2,3,4,5,6]
print(l1)
[1, 2, 3, 4, 5, 6]

#  >>>>>>>>


#                 0 1 2 3 4 5
l1 : list[int] = [1,2,3,4,5,6]

for n in l1:
    print(n)
1
2
3
4
5
6

#  >>>>>>>>

#                 0 1 2 3 4 5
l1 : list[int] = [1,2,3,4,5,6]

for n in l1:
    print(f"current number :{n}")
current number :1
current number :2
current number :3
current number :4
current number :5
current number :6

#  >>>>>>>>

#                 0 1 2 3 4 5
l1 : tuple[int] = (1,2,3,4,5,6)

for n in l1:
    print(f"current number :{n}")
current number :1
current number :2
current number :3
current number :4
current number :5
current number :6


#  >>>>>>>>

#           01234567
l1 : str = "Pakistan"

for c in l1:
    print(f"current character :{c}")
current character :P
current character :a
current character :k
current character :i
current character :s
current character :t
current character :a
current character :n


#  >>>>>>>>

#           iteration perform on keys
l1 : dict[str,str] = {"name":"Muhammad Qasim","fname":"Muhammad Aslam"}

for k in l1:
    print(f"dictionary key {k} and value is {l1[k]}")
dictionary key name and value is Muhammad Qasim
dictionary key fname and value is Muhammad Aslam

#  >>>>>>>>

#           iteration perform on keys
l1 : set[int] = {1,2,3,4,1,1,1,1}

for k in l1:
    print(f"set item is  {k} ")
set item is  1 
set item is  2 
set item is  3 
set item is  4 

#  >>>>>>>>

#                     
l1 : list[set[int]] = list({1,2,3,4,1,1,1,1})

for k in l1:
    print(f"value from list of set : {k} ")
# value from list of set : 1 
# value from list of set : 2 
# value from list of set : 3 
# value from list of set : 4 

#  >>>>>>>>


# input from user
# input function
# defualt type = string
# sys.argv (for console input in abc.py file)
# defualt type = str

#  >>>>>>>>

name : str = input("What is your name? : \t")

print(type(name))

print(f"Welecom dear User Mr/Miss {name}!")
<class 'str'>
# Welecom dear User Mr/Miss Zia khan!

#  >>>>>>>>

names : list[str] = ['a','b','c']
fname : list[str] = ['x','y','z']
age : list[int] = [1,2,3]

zip(names,fname,age)
<zip at 0x1208b1100>

#  >>>>>>>>

names : list[str] = ['a','b','c']
fname : list[str] = ['x','y','z']
age : list[int] = [1,2,3]

list(zip(names,fname,age))

for name,fn, ag in zip(names,fname,age):
    print(f"Welcome dear {name}, s/o {fn}!")
Welcome dear a, s/o x!
Welcome dear b, s/o y!
Welcome dear c, s/o z!


#  >>>>>>>>


# While loop
# while logic: # True/False
#     loop_body
flag : bool = True #flag

current_number : int = 0 #

while flag:
    print(f"current number is :{current_number}")
    current_number += 1

    if current_number == 10: # flag false at some point
        break
# current number is :0
# current number is :1
# current number is :2
# current number is :3
# current number is :4
# current number is :5
# current number is :6
# current number is :7
# current number is :8
# current number is :9


#  >>>>>>>>


l1: list[int] = [100,200,300]

index : int = 0 #

while index < len(l1):
    print(f"current index is :{index} and list value is {l1[index]}")
    index += 1

   
# current index is :0 and list value is 100
# current index is :1 and list value is 200
# current index is :2 and list value is 300

#  >>>>>>>>

data : list[dict[str,str]] = []

flag : bool = True

while flag:
    print("write quite or exit to stop this program")
    name : str = input ("Your good name ? \t:")
    eduction: str = input("Your last education? \t")

    if name in ['exit','quite','close','stop'] or eduction  in ['exit','quite','close','stop']:
        flag=False
        break
    data.append({"name":name,
                 "education": eduction})

# display(data)    
# write quite or exit to stop this program
# write quite or exit to stop this program
# write quite or exit to stop this program
# write quite or exit to stop this program
# write quite or exit to stop this program
# [{'name': 'a', 'education': 'a'},
#  {'name': 'b', 'education': 'b'},
#  {'name': 'c', 'education': 'c'},
#  {'name': 'd', 'education': 'd'}]

#  >>>>>>>>

# controls
# break
# continue
#     skip
# pass


#  >>>>>>>>

or i in range(1,11):
    print(i)
    if i == 5:
        break
1
2
3
4
5



#  >>>>>>>>


for i in range(1,11):
    print(f"2 X {i} = {i*2}")
    break
2 X 1 = 2

#  >>>>>>>>

for i in range(1,11):
    print(f"2 X {i} = {i*2}")
2 X 1 = 2
2 X 2 = 4
2 X 3 = 6
2 X 4 = 8
2 X 5 = 10
2 X 6 = 12
2 X 7 = 14
2 X 8 = 16
2 X 9 = 18
2 X 10 = 20

#  >>>>>>>>
for i in range(1, 11):  # Creating a range from 1 to 10
    if i == 5:
        continue  # Skipping the iteration when i is 5
    print(i)
1
2
3
4
6
7
8
9
10
pass

#  >>>>>>>>

for i in range(1,1000):
    
  Cell In[38], line 2
    
    ^
SyntaxError: incomplete input


#  >>>>>>>>

if True:
    pass

print("pakistan")
print("Second")
pakistan
Second


#  >>>>>>>>

if True:
    name : str = input("Your name?")
    print(name)
qasim

#  >>>>>>>>

if False:
    name : str = input("Your name?")
    print(name)
print(1 + 7 + 3 + 4)

#  >>>>>>>>

print(1 + 7 \
      + 3\
         + 4)
15


#  >>>>>>>>
prompt = """If you share your name, we can personalize the messages you see.\
What is your first name? """


name = input(prompt)
print(f"\nHello, {name}!")
Hello, qasim
#  >>>>>>>>

age:str = input("How old are you? ")
age >= 18
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[51], line 2
      1 age:str = input("How old are you? ")
----> 2 age >= 18

TypeError: '>=' not supported between instances of 'str' and 'int'

#  >>>>>>>>

age:int = int(input("How old are you? "))
age >= 18
True

#  >>>>>>>>

data : list[int] = [1,3,5,6,3,15,18]

# extract even numbers from this list

[i  for i in data if i%2==0]
[6, 18]

#  >>>>>>>>

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 != 0:
        continue
    print(current_number)
2
4
6
8
10

#  >>>>>>>>

data : list[int] = [1,3,5,6,3,15,18]

# extract even numbers from this list

[i  for i in data if i%2!=0]
[1, 3, 5, 3, 15]

#  >>>>>>>>

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
1
3
5
7
9

#  >>>>>>>>
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
1
b
c
quit

#  >>>>>>>>

prompt:str = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "


active = True 

while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
q
b
c


#  >>>>>>>>

# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users : list[str] = ['alice', 'brian', 'candace']
confirmed_users : list[str] = []
  # Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users. 2 
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
# Verifying user: Candace
# Verifying user: Brian
# Verifying user: Alice

# The following users have been confirmed:
# Candace
# Brian
# Alice


#  >>>>>>>>


data : list[int] = [1,2,3]

while data:
    n : int = data.pop()
    print(n)
3
2
1

#  >>>>>>>>

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat'] 
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)
['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
['dog', 'dog', 'goldfish', 'rabbit']

#  >>>>>>>>

#  >>>>>>>>

#  >>>>>>>>




#  >>>>>>>>




#  >>>>>>>>





#  >>>>>>>>




#  >>>>>>>>
