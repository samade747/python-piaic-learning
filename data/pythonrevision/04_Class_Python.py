#list 
# mutliple value store in single variable
#dynamic length 
# hetorgerous data type (Multipe types of data)
# indexing
#  postive 0 to n-1
#  negative -1 to length 


# ->  0      1      2
names = ["samad", "maryam", "ali", "sara", "ahmed"]
# ->           -5     -4     -3     -2      -1


print(names[0]) # samad
print(names[-4]) # maryam 

# >>>>>>>


from typing import Any

# ->                    0        1         2
names : list[Any] = ["Qasim","Sir Zia", "Sir Inam", 20, True]
# <-                    -3     -2          -1

print(names[-2])

# >>>>>>>


list('abcdef') # ['a', 'b', 'c', 'd', 'e', 'f']


# >>>>>>>

characters : list[str] = list("ABCDEFGHIJKLMNOPQRSTUVWXYX")
print(characters) # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X']

# >>>>>>>
#  Doing slicing on list    
# 
# # >>>>>> list[start : end : step]
#                          0    1    2                                                                                                                 25
characters : list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'X']
#                         -26   -25  -24                                                                                                                         -1

# defualt slicing go from left to right
print(characters[0:2]) # 0= include : index 2-1 = 1
print(characters[:2]) # not pass any number = all
print(characters[-26:-24])# 0= include : index -24-1 = -25
print(characters[0:2:1]) # 0= include : index 2-1 = 1
print(characters[0:2:]) # 0= include : index 2-1 = 1...

# output
# ['A', 'B']
# ['A', 'B']
# ['A', 'B']
# ['A', 'B']
# ['A', 'B']

characters : list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'X']

print(characters[::]) 

# ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'X']

# >>>>>>>

characters : list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'X']

print(characters[::2])
['A', 'C', 'E', 'G', 'I', 'K', 'M', 'O', 'Q', 'S', 'U', 'W', 'Y']

# >>>>>>>

#                          0    1    2    3    4   5     6    7
characters : list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
#                         -8    -7   -6  -5    -4   -3   -2   -1

print(characters[1:-3]) # 'B', 'C', 'D', 'E'
['B', 'C', 'D', 'E']

# >>>>>>>

#                          0    1    2    3    4   5     6    7
characters : list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
#                         -8    -7   -6  -5    -4   -3   -2   -1

# iteration slicing ->
# step -> positive
# step <- negative
print(characters[-2:-5]) 
[]

# >>>>>>>

#                          0    1    2    3    4   5     6    7
characters : list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
#                         -8    -7   -6  -5    -4   -3   -2   -1

# iteration slicing ->
# step -> positive
# step <- negative
print(characters[-2:-5:-1]) 
['G', 'F', 'E']


# >>>>>>>

# Define a list of characters from A to Z
characters: list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
                         'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
                         'U', 'V', 'W', 'X', 'Y', 'Z']

# Print the list in reverse order using slicing
print(characters[::-1])

# Explanation of characters[::-1]:
# - start: not given → so it starts from the last element ('Z')
# - end: not given → so it ends after the first element ('A')
# - step: -1 → move backward one step at a time
# This results in the entire list being reversed

# Output:
# ['Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O',
#  'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']


# >>>>>>>

# List methods

# >>>>>>>

[i for i in dir(list) if "__" not in i]
['append',
 'clear',
 'copy',
 'count',
 'extend',
 'index',
 'insert',
 'pop',
 'remove',
 'reverse',
 'sort']

# >>>>>>>
a: list[str] = [1,2,3]
print(a)
[1, 2, 3]

# >>>>>>>

a: list[str] = [1,2,3]
del a # remove object from memory
print(a)
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# Cell In[49], line 3
#       1 a: list[str] = [1,2,3]
#       2 del a
# ----> 3 print(a)

# NameError: name 'a' is not defined

# >>>>>>>
a: list[str] = [1,2,3]
a.clear()# remove all element but object is ramin
print(a)
[]


# >>>>>>>

# ->                    0        1         2
names : list[Any] = ["Qasim","Sir Zia", "Sir Inam", 20, True]
# <-                    -3     -2          -1

print(names)

names[0] = "Muhammad Qasim" # mutable -> editable

print(names)
['Qasim', 'Sir Zia', 'Sir Inam', 20, True]
['Muhammad Qasim', 'Sir Zia', 'Sir Inam', 20, True]

# >>>>>>>

a : str = print("Pakistan") # none-return function
# display(a)
# Pakistan
# None

# >>>>>>>

a : str = id(names) # return function
# display(a)
4440742592


# >>>>>>>

# ->                    0        1         2
names : list[Any] = ["Qasim","Sir Zia", "Sir Inam", 20, True]
# <-                    -3     -2          -1

del names[3]
names
['Qasim', 'Sir Zia', 'Sir Inam', True]

# >>>>>>>


# pop method
# ->                    0        1         2
names : list[Any] = ["Qasim","Sir Zia", "Sir Inam", 20, True]
# <-
print(names)
a : str = names.pop() # pop return method

print(a)
['Qasim', 'Sir Zia', 'Sir Inam', 20, True]
True


# >>>>>>>>

# ->                    0        1         2
names : list[Any] = ["Qasim","Sir Zia", "Sir Inam", 20, True]
# <-
print(names)
a : str = names.pop(0) # pop return method

print(a)
print(names)
['Qasim', 'Sir Zia', 'Sir Inam', 20, True]
# Qasim
['Sir Zia', 'Sir Inam', 20, True]


# >>>>>>>>

# append method add element in last
names : list[str] = ['a','b']

names.append("Sir Zia")# add element in last
names.append("Sir Inam") # add element in last
names.append("Qasim")# add element in last

print(names)
['a', 'b', 'Sir Zia', 'Sir Inam', 'Qasim']
