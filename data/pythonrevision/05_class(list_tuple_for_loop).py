# List
# iteration operation with loop
# apply any operation on element


#  >>>>>>>>

names : list[str] = ['Sir Zia',"Muhammad Qasim","DR Noman"]
print(names)
['Sir Zia', 'Muhammad Qasim', 'DR Noman']

#  >>>>>>>>

names:list[str] = ['Sir Zia', "Muhammad Qasim", "DR Noman"]

for name in names:
    print(name)

# Sir zia
# "Muhammad Qasim"
# DR Noman
# Sir Zia
# Muhammad Qasim
# DR Noman

#  >>>>>>>>

for name in names:
    print(f'Welcome Dear Tacher {name.title()}')
# Welcome Dear Tacher Sir Zia
# Welcome Dear Tacher Muhammad Qasim
# Welcome Dear Tacher Dr Noman

#  >>>>>>>>

names:list[str] = ['Sir Zia', "Muhammad Qasim", "DR Noman"]

for name in names:
    print(f'Welcome Dear Tacher {name.title()}')
    print("PIAIC Gen AI Team\n")
# Welcome Dear Tacher Sir Zia
# PIAIC Gen AI Team

# Welcome Dear Tacher Muhammad Qasim
# PIAIC Gen AI Team

# Welcome Dear Tacher Dr Noman
# PIAIC Gen AI Team

#  >>>>>>>>

names:list[str] = ['Sir Zia', "Muhammad Qasim", "DR Noman"]

for name in names:
    print(f'Welcome Dear Tacher {name.title()}')
    print("PIAIC Gen AI Team\n")

print("Pakistan zinda bad")
# Welcome Dear Tacher Sir Zia
# PIAIC Gen AI Team

# Welcome Dear Tacher Muhammad Qasim
# PIAIC Gen AI Team

# Welcome Dear Tacher Dr Noman
# PIAIC Gen AI Team

# Pakistan zinda bad


#  >>>>>>>>


names:list[str] = ['Sir Zia', "Muhammad Qasim", "DR Noman"]

for name in names[-2:]:
    print(f'Welcome Dear Tacher {name.title()}')
    print("PIAIC Gen AI Team\n")

print("Pakistan zinda bad")
# Welcome Dear Tacher Muhammad Qasim
# PIAIC Gen AI Team

# Welcome Dear Tacher Dr Noman
# PIAIC Gen AI Team

# Pakistan zinda bad


#  >>>>>>>>


names:list[str] = ['Sir Zia', "Muhammad Qasim", "DR Noman"]

for name in names[::-1]:
    print(f'Welcome Dear Tacher {name.upper()}')
    print("PIAIC Gen AI Team\n")
print("Pakistan zinda bad\n")
# Welcome Dear Tacher DR NOMAN
# PIAIC Gen AI Team

# Welcome Dear Tacher MUHAMMAD QASIM
# PIAIC Gen AI Team

# Welcome Dear Tacher SIR ZIA
# PIAIC Gen AI Team

# Pakistan zinda bad


#  >>>>>>>>

data_base : list[tuple[str,str]] = [("qasim",'123'),
                                    ("sirzia",'345'),
                                    ('ikhlas','789')
                                    ]

for row in data_base:
    print(row)
# ('qasim', '123') 
# ('sirzia', '345')
# ('ikhlas', '789')

#  >>>>>>>>


data_base : list[tuple[str,str]] = [("qasim",'123'),
                                    ("sirzia",'345'),
                                    ('ikhlas','789')
                                    ]

for row in data_base:
    user, password = row
    print(user, password)
# qasim 123
# sirzia 345
# ikhlas 789


#  >>>>>>>>

input_user : str = input("Enter user name")
print(input_user)
# Muhammad Qasim Pakistan zinda bad


#  >>>>>>>>

data_base : list[tuple[str,str]] = [("qasim",'123'),
                                    ("sirzia",'345'),
                                    ('ikhlas','789')
                                    ]
input_user : str = input("Enter user name")
input_password : str = input("Enter user password")



for row in data_base:
    user, password = row
    if input_user == user and input_password == password:
        print(f"Valid User {user}")
        break
else:
    print("Not found or Invalid user name")
    
# Valid User qasim


#  >>>>>>>>

data_base : list[tuple[str,str]] = [("qasim",'123'),
                                    ("samad",'019'),
                                    ('mmaryam','019')
                                    ]
input_user : str = input("Enter user name")
input_password : str = input("Enter user password")



for row in data_base:
    user, password = row # ("qasim",'123')
    if input_user == user and input_password == password:
        print("Valid User")
        break
else:
    print("Not found or Invalid user name")
    
# Not found or Invalid user name

#  >>>>>>>>


data_base : list[tuple[str,str]] = [("qasim",'123'),
                                    ("sirzia",'345'),
                                    ('ikhlas','789')
                                    ]
input_user : str = input("Enter user name")
input_password : str = input("Enter user password")

# user , password = ("qasim",'123')
# user = name[0]
# password = name[1]

for row in data_base:
    user, password = row  # ("qasim",'123')
    if input_user == user and input_password == password:
        print("Valid User")
        break
else:
    print("Not found or Invalid user name")
    
# Valid User

#  >>>>>>>>

names:list[str] = ['Sir Zia', "Muhammad Qasim", "DR Noman"]

for name in names:
    print(name)
else:
    print("Hello world")
    
# Sir Zia
# Muhammad Qasim
# DR Noman
# Hello world

#  >>>>>>>>

names:list[str] = ['Sir Zia', "Muhammad Qasim", "DR Noman"]

for name in names:
    print(name)
    break
    
print("Hello world")
    
# Sir Zia
# Hello world

#  >>>>>>>>

names:list[str] = ['Sir Zia', "Muhammad Qasim", "DR Noman"]

for name in names:
# print(name)
#   Cell In[35], line 4
#     print(name)
#     ^
# IndentationError: expected an indented block after 'for' statement on line 3


#  >>>>>>>>

names:list[str] = ['Sir Zia', "Muhammad Qasim", "DR Noman"]

for name in names
    print(name)
#   Cell In[36], line 3
#     for name in names
#                      ^
# SyntaxError: expected ':'

#  >>>>>>>>

magicians: list[str] = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    

print(f"I can't wait to see your next trick, {magician.title()}.\n")
# Alice, that was a great trick!
# David, that was a great trick!
# Carolina, that was a great trick!
# I can't wait to see your next trick, Carolina.


#  >>>>>>>>

message = "Hello Python world!" 
    print(message)
#   Cell In[41], line 2
#     print(message)
#     ^
# IndentationError: unexpected indent

#  >>>>>>>>

message = "Hello Python world!" 
 print(message)
  Cell In[42], line 2
    print(message)
    ^
IndentationError: unexpected indent

#  >>>>>>>>

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
    
print("Thank you everyone, that was a great magic show!")# last message for everyone

# Alice, that was a great trick!
# I can't wait to see your next trick, Alice.

# David, that was a great trick!
# I can't wait to see your next trick, David.

# Carolina, that was a great trick!
# I can't wait to see your next trick, Carolina.

# Thank you everyone, that was a great magic show!


#  >>>>>>>>

#              0        1         2
magicians = ['alice', 'david', 'carolina']

list(enumerate(magicians))
[(0, 'alice'), (1, 'david'), (2, 'carolina')]

#  >>>>>>>>

#              0        1         2
magicians = ['alice', 'david', 'carolina']

for index, name in enumerate(magicians):
    print(index, name)
# 0 alice
# 1 david
# 2 carolina

#  >>>>>>>>

#  >>>>>>>>

#  >>>>>>>>

# Numbers with loop

# range(start,end,step)

range(10)
range(0, 10)

#  >>>>>>>>

list(range(10))# starting=0, ending = n-1
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#  >>>>>>>>

list(range(2,10))# starting=0, ending = n-1
[2, 3, 4, 5, 6, 7, 8, 9]

#  >>>>>>>>

list(range(2,21,2))# starting=0, ending = n-1 21-1=20, step
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#  >>>>>>>>

for n in range(1,11):
    print(n)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

#  >>>>>>>>

for n in range(1,11):
    print(f"{2} X {n} = {n*2}")
# 2 X 1 = 2
# 2 X 2 = 4
# 2 X 3 = 6
# 2 X 4 = 8
# 2 X 5 = 10
# 2 X 6 = 12
# 2 X 7 = 14
# 2 X 8 = 16
# 2 X 9 = 18
# 2 X 10 = 20

#  >>>>>>>>

squares:list[int] = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#  >>>>>>>>


list(range(1,11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#  >>>>>>>>

for i in range(1,11):
    print(i**2)
1
4
9
16
25
36
49
64
81
100



#  >>>>>>>>

'line1'
'line2'
'line3' # always return last line
'line3'

#  >>>>>>>>

[i**2 for i in range(1,11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


#  >>>>>>>>

digits:list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(digits)
print(max(digits))
print(min(digits))
print(sum(digits))


[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
9
0
45

#  >>>>>>>>


my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:] # deep copy

print(my_foods)
print(friend_foods)

friend_foods[0] = "Tikka"

print(my_foods)
print(friend_foods)

['pizza', 'falafel', 'carrot cake']
['pizza', 'falafel', 'carrot cake']
['pizza', 'falafel', 'carrot cake']
['Tikka', 'falafel', 'carrot cake']


#  >>>>>>>>

# Tuples


names:tuple[str] = ('A',"B",'C')
print(names[0])
print(names[0:2])


A
('A', 'B')

#  >>>>>>>>

names:tuple[str] = ('A',"B",'C')

names[0] = "Pakistan"

# KeyError: 'tuple' object does not support item assignment

#  >>>>>>>>

from typing import Any
data : tuple[Any] = ("A",[1,2,3], True)

print(data)

('A', [1, 2, 3], True)


#  >>>>>>>>

from typing import Any
data : tuple[Any] = ("A",[1,2,3], True)

print(data)
('A', [1, 2, 3], True)

#  >>>>>>>>

data : tuple[Any] = ("A",[1,2,3], True)

print(data[1])
data[1].append(20)
print(data)

[1, 2, 3]
('A', [1, 2, 3, 20], True)

#  >>>>>>>>

a  = input("abc") # return string type
print(type(a))
print(a)

<class 'str'>
123

#  >>>>>>>>


sorted([7,8,1,3])
[1, 3, 7, 8]


#  >>>>>>>>
sorted([7,8,1,3], reverse=True)
[8, 7, 3, 1]

#  >>>>>>>>