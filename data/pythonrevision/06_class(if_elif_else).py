# If-else-elif
# if logic:
#     True_block
# else:
#     False_block
# comprehensive if-else
# True_block if logic else False_block
# if
# if-else
# if-elif-else

#  >>>>>>>>

if True:
    print("Pakistan zinda bad")
else:
    print("Hello world!")

# Pakistan zinda bad

#  >>>>>>>>

# Comparison operators
# ==
# >=
# <=
# !=
# logic
# and
# or
# not

#  >>>>>>>>

if True:
    print("True Pakistan block")

print("1")
print("2")
True Pakistan block
1
2


#  >>>>>>>>

if True:
    print("True_block")
elif False:
    print("elif logic1")
elif False:
    print("elif logic2")
elif False:
    print("elif logic3")
else:
    print("final else block")
True_block


#  >>>>>>>>

if False:
    print("True_block")
elif True:
    print("elif logic1")
elif False:
    print("elif logic2")
elif False:
    print("elif logic3")
else:
    print("final else block")
elif logic1


#  >>>>>>>>


# chain1 run only one block 
if False:
    print("True_block")
elif False:
    print("elif logic1")
elif True:
    print("elif logic2")
elif True:
    print("elif logic3")
else:
    print("final else block")

# chain2 run only one block 
if False:
    print("True_block")
elif False:
    print("elif logic1")
elif False:
    print("elif logic2")
elif False:
    print("elif logic3")
else:
    print("final else block")

print("Pakistan")
elif logic2
final else block
Pakistan


#  >>>>>>>>


from typing import Union

per : Union[int, float] = 88
grade :Union[str, None] = None

if per >= 80:
    grade = "A+"
elif per >= 70:
    grade = "A"
elif per >= 60:
    grade = "B"
elif per >= 50:
    grade = "C"
elif per >= 40:
    grade = "D"
elif per >= 33:
    grade = "E"
else:
    grade = "Fail"

print(f"Dear Student your percentage is {per} now your calculated grade is:\t {grade}")
    
# Dear Student your percentage is 88 now your calculated grade is:	 A+

#  >>>>>>>>

a = input("Enter your percentage:\t")
print(type(a))
print(a)

# <class 'str'>
# 81

#  >>>>>>>>

from typing import Union

per : Union[int, float] = int(input("Enter your percentage:\t"))
grade : Union[str, None] = None

if per >= 80:
    grade = "A+"
elif per >= 70:
    grade = "A"
elif per >= 60:
    grade = "B"
elif per >= 50:
    grade = "C"
elif per >= 40:
    grade = "D"
elif per >= 33:
    grade = "E"
else:
    grade = "Fail"

print(f"Dear Student your percentage is {per} now your calculated grade is:\t {grade}")
    
# Dear Student your percentage is 78 now your calculated grade is:	 A

#  >>>>>>>>

from typing import Union, Optional

per : Union[int, float] = 88
# per : int | float = 88

grade :Optional[str] = None

if per >= 80:
    grade = "A+"
elif per >= 70:
    grade = "A"
elif per >= 60:
    grade = "B"
elif per >= 50:
    grade = "C"
elif per >= 40:
    grade = "D"
elif per >= 33:
    grade = "E"
else:
    grade = "Fail"

#  >>>>>>>>

# LOgical Error
from typing import Union

per : Union[int, float] = int(input("Enter your percentage:\t"))
grade : Union[str, None] = None

if per >= 0:
    grade = "Fail"
elif per >= 33:
    grade = "E"
elif per >= 40:
    grade = "D"
elif per >= 50:
    grade = "C"
elif per >= 60:
    grade = "B"
elif per >= 70:
    grade = "A"
else:
    grade = "A+"

print(f"Dear Student your percentage is {per} now your calculated grade is:\t {grade}")
    
# Dear Student your percentage is 99 now your calculated grade is:	 Fail

#  >>>>>>>>

from typing import Union

per : Union[int, float] = int(input("Enter your percentage:\t"))
grade : Union[str, None] = None

if per >= 0 and per < 33:
    grade = "Fail"
elif per >= 33 and per < 40:
    grade = "E"
elif per >= 40 and per < 50:
    grade = "D"
elif per >= 50 and per < 60:
    grade = "C"
elif per >= 60 and per <70 :
    grade = "B"
elif per >= 70 and per <80 :
    grade = "A"
elif per >=80 and per <= 100:
    grade = "A+"

print(f"Dear Student your percentage is {per} now your calculated grade is:\t {grade}")
    
# Dear Student your percentage is 99 now your calculated grade is:	 A+

#  >>>>>>>>

# Student percentages
# https://peps.python.org/pep-0484/#type-aliases

from typing import Union
PerType = Union[float, int]

percentages : list[PerType] = [88, 99.9, 50, 51,65,70]

grades : list[str] = []

for per in percentages:
    grade : str = ""

    if (per >= 0) and (per < 33):
        grade = "Fail"
    elif (per >= 33) and (per < 40):
        grade = "E"
    elif (per >= 40) and (per < 50):
        grade = "D"
    elif (per >= 50) and (per < 60):
        grade = "C"
    elif (per >= 60) and (per <70) :
        grade = "B"
    elif (per >= 70) and (per <80) :
        grade = "A"
    elif (per >=80) and (per <= 100):
        grade = "A+"

    grades.append(grade)

print(percentages)
print(grades)

    
[88, 99.9, 50, 51, 65, 70]
['A+', 'A+', 'C', 'C', 'B', 'A']


#  >>>>>>>>

names: list[str] = ['Sir Zia']

names.append("Qasim")
names.append("Sir Inam")
print(names)
['Sir Zia', 'Qasim', 'Sir Inam']

#  >>>>>>>>


zip(percentages, grades) # <zip at 0x10c2c00c0> generator function iteration perform->list, for
<zip at 0x10c2c00c0>
#  >>>>>>>>

roll_no: list[int] = list(range(len(percentages)))
roll_no
[0, 1, 2, 3, 4, 5]

#  >>>>>>>>

data_base = list(zip(roll_no,percentages, grades))
data_base
[(0, 88, 'A+'),
 (1, 99.9, 'A+'),
 (2, 50, 'C'),
 (3, 51, 'C'),
 (4, 65, 'B'),
 (5, 70, 'A')]

#  >>>>>>>>

display(data_base)
sorted(data_base)
[(0, 88, 'A+'),
 (1, 99.9, 'A+'),
 (2, 50, 'C'),
 (3, 51, 'C'),
 (4, 65, 'B'),
 (5, 70, 'A')]
[(0, 88, 'A+'),
 (1, 99.9, 'A+'),
 (2, 50, 'C'),
 (3, 51, 'C'),
 (4, 65, 'B'),
 (5, 70, 'A')]

#  >>>>>>>>

display(data_base)
sorted(data_base, key=lambda x:x[1])
[(0, 88, 'A+'),
 (1, 99.9, 'A+'),
 (2, 50, 'C'),
 (3, 51, 'C'),
 (4, 65, 'B'),
 (5, 70, 'A')]
[(2, 50, 'C'),
 (3, 51, 'C'),
 (4, 65, 'B'),
 (5, 70, 'A'),
 (0, 88, 'A+'),
 (1, 99.9, 'A+')]



#  >>>>>>>>

isplay(data_base)
sorted(data_base, key=lambda x:x[1], reverse=True)
[(0, 88, 'A+'),
 (1, 99.9, 'A+'),
 (2, 50, 'C'),
 (3, 51, 'C'),
 (4, 65, 'B'),
 (5, 70, 'A')]
[(1, 99.9, 'A+'),
 (0, 88, 'A+'),
 (5, 70, 'A'),
 (4, 65, 'B'),
 (3, 51, 'C'),
 (2, 50, 'C')]

#  >>>>>>>>



#  >>>>>>>>

#  >>>>>>>>



#  >>>>>>>>

#  >>>>>>>>



#  >>>>>>>>

#  >>>>>>>>