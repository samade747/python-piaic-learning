#  >>>>>>>>


from typing import Dict, Union, Optional
import pprint


Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

data : Dict[Key,Value] = {
                        "fname":"Muhammad Aslam",
                        "name":"Muhammad Qasim",
                        "education": "MSDS"}


methods : list[str] = [m for m in dir(data) if "__" not in m]
print(methods)
['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']


#  >>>>>>>>


from typing import Dict, Union, Optional
import pprint


Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

data : Dict[Key,Value] = {
                        "fname":"Muhammad Aslam",
                        "name":"Muhammad Qasim",
                        "education": "MSDS"}

print("Before", data)

data.clear()
print("After", data)

methods : list[str] = [m for m in dir(data) if "__" not in m]
print(methods)
Before {'fname': 'Muhammad Aslam', 'name': 'Muhammad Qasim', 'education': 'MSDS'}
After {}
['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']



#  >>>>>>>>

from typing import Dict, Union, Optional
import pprint


Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

data : Dict[Key,Value] = {
                        "fname":"Muhammad Aslam",
                        "name":"Muhammad Qasim",
                        "education": "MSDS"}

print("Before", data)

del data

print("After", data)

methods : list[str] = [m for m in dir(data) if "__" not in m]
print(methods)
Before {'fname': 'Muhammad Aslam', 'name': 'Muhammad Qasim', 'education': 'MSDS'}
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[4], line 17
     13 print("Before", data)
     15 del data
---> 17 print("After", data)
     19 methods : list[str] = [m for m in dir(data) if "__" not in m]
     20 print(methods)

NameError: name 'data' is not defined


#  >>>>>>>>


from typing import Dict, Union, Optional
import pprint


Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

data : Dict[Key,Value] = {
                        "fname":"Muhammad Aslam",
                        "name":"Muhammad Qasim",
                        "education": "MSDS"}

print("Before", data)

a : str = data.pop("education")
print(a)

print("After", data)

methods : list[str] = [m for m in dir(data) if "__" not in m]
print(methods)
Before {'fname': 'Muhammad Aslam', 'name': 'Muhammad Qasim', 'education': 'MSDS'}
MSDS
After {'fname': 'Muhammad Aslam', 'name': 'Muhammad Qasim'}
['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']




#  >>>>>>>>

from typing import Dict, Union, Optional
import pprint


Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

data : Dict[Key,Value] = {
                        "fname":"Muhammad Aslam",
                        "name":"Muhammad Qasim",
                        "education": "MSDS"}

print("Before", data)

a : str = data.get("Pakistan","NA")
print(a)

print("After", data)

methods : list[str] = [m for m in dir(data) if "__" not in m]
print(methods)
Before {'fname': 'Muhammad Aslam', 'name': 'Muhammad Qasim', 'education': 'MSDS'}
NA
After {'fname': 'Muhammad Aslam', 'name': 'Muhammad Qasim', 'education': 'MSDS'}
['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']


#  >>>>>>>>


from typing import Dict, Union, Optional
import pprint


Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

data : Dict[Key,Value] = {
                        "fname":"Muhammad Aslam",
                        "name":"Muhammad Qasim",
                        "education": "MSDS"}

print("Before", data)

a : str = data.setdefault("Pakistan","Empty value")
print(a)

print("After", data)

methods : list[str] = [m for m in dir(data) if "__" not in m]
print(methods)
# Before {'fname': 'Muhammad Aslam', 'name': 'Muhammad Qasim', 'education': 'MSDS'}
# Empty value
# After {'fname': 'Muhammad Aslam', 'name': 'Muhammad Qasim', 'education': 'MSDS', 'Pakistan': 'Empty value'}
# ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']


#  >>>>>>>>

Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

data : Dict[Key,Value] = {
                        "fname":"Muhammad Aslam",
                        "name":"Muhammad Qasim",
                        "education": "MSDS"}


data1 : Dict[Key,Value] = {"name":"M.Qasim",
                           "age":30,
                           "Height": "6 Feet"}

data.update(data1)

data
{'fname': 'Muhammad Aslam',
 'name': 'M.Qasim',
 'education': 'MSDS',
 'age': 30,
 'Height': '6 Feet'}



#  >>>>>>>>

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed. 1 
alien_0['speed'] = 'fast'
# 
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment. 2
# alien_0['x_position'] = alien_0['x_position'] + x_increment
alien_0['x_position'] +=  x_increment
print(f"New position: {alien_0['x_position']}")
Original position: 0
New position: 3



#  >>>>>>>>

Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

data : Dict[Key,Value] = {
                        "fname":"Muhammad Aslam",
                        "name":"Muhammad Qasim",
                        "education": "MSDS",
                        "name":"M.Qasim"}

print(data)
{'fname': 'Muhammad Aslam', 'name': 'M.Qasim', 'education': 'MSDS'}

#  >>>>>>>>


favorite_languages = {
      'jen': 'python',
      'sarah': 'c',
      'edward': 'rust',
      'phil': 'python',
      }
language = favorite_languages['jen'].title() 
print(f"Sarah's favorite language is {language}.")
# Sarah's favorite language is Python.



#  >>>>>>>>


favorite_languages = {
      'jen': 'python',
      'sarah': 'c',
      'edward': 'rust',
      'phil': 'python',
      }

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
Hi Jen.
Hi Sarah.
	Sarah, I see you love C!
Hi Edward.
Hi Phil.
	Phil, I see you love Python!


#  >>>>>>>>

print('erin' not in favorite_languages.keys())
print(favorite_languages.keys())
True
dict_keys(['jen', 'sarah', 'edward', 'phil'])


#  >>>>>>>>

"Qasim" in """My Name is Muhammad Qasim, I'm working as Chief Data Scientist!"""
True

#  >>>>>>>>

alien_0: list[Key, Value] = {'color': 'green', 'points': 5}
alien_1: list[Key, Value] = {'color': 'yellow', 'points': 10}
alien_2: list[Key, Value] = {'color': 'red', 'points': 15}

aliens:list[Dict[str,str]] = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
{'color': 'green', 'points': 5}
{'color': 'yellow', 'points': 10}
{'color': 'red', 'points': 15}


#  >>>>>>>>

# Make an empty list for storing aliens.
aliens : list[Dict[str,str]] = []
import pprint
print(aliens)
# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
pprint.pprint(aliens)
[]
[{'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'}]

#  >>>>>>>>


pprint.pprint(aliens[:5])
[{'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'}]

#  >>>>>>>>

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
aliens[:10]


#  >>>>>>>>


aliens[:10]
[{'color': 'yellow', 'points': 10, 'speed': 'medium'},
 {'color': 'yellow', 'points': 10, 'speed': 'medium'},
 {'color': 'yellow', 'points': 10, 'speed': 'medium'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'}]

#  >>>>>>>>

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

aliens
[{'color': 'red', 'points': 15, 'speed': 'fast'},
 {'color': 'red', 'points': 15, 'speed': 'fast'},
 {'color': 'red', 'points': 15, 'speed': 'fast'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'},
 {'color': 'green', 'points': 5, 'speed': 'slow'}]


#  >>>>>>>>

Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

data : Dict[Key,Value] = {
                        "fname":"Muhammad Aslam",
                        "name":"Muhammad Qasim",
                        "education": "MSDS"}

print(data)
print(type(data))
{'fname': 'Muhammad Aslam', 'name': 'Muhammad Qasim', 'education': 'MSDS'}
<class 'dict'>


#  >>>>>>>>

import json

data1  = json.dumps(data, indent=4)

print(type(data1))
display(data1)
print(data1)
<class 'str'>
'{\n    "fname": "Muhammad Aslam",\n    "name": "Muhammad Qasim",\n    "education": "MSDS"\n}'
{
    "fname": "Muhammad Aslam",
    "name": "Muhammad Qasim",
    "education": "MSDS"
}




#  >>>>>>>>

# Nested Dictionary error solution

from typing import Union, TypedDict, Tuple, Set, List
import pprint

cdeDataType = TypedDict(
    'cdeDataType',
    {
        "a": int,
        "b": int
    }
)

myDataType = TypedDict(
    'myDataType', {
        "fname": str,
        "name": str,
        "education": str,
        "abc": List[int],
        'xyz': Set[int],
        'efg': Tuple,
        'cde': cdeDataType
    }
)


# Key = Union[int, str]  # create custom type
# Value = Union[int, str, list, tuple, set]


data: myDataType = {
    "fname": "Muhammad Aslam",
    "name": "Muhammad Qasim",
    "education": "MSDS",
    "abc": [1, 2, 3],
    'xyz': {1, 2, 3},
    'efg': (1, 2, 3),
    'cde': {"a": 1, "b": 2}
}

print(data['cde']['b'])
2


#  >>>>>>>>




#  >>>>>>>>




#  >>>>>>>>




#  >>>>>>>>



#  >>>>>>>>



#  >>>>>>>>




#  >>>>>>>>


