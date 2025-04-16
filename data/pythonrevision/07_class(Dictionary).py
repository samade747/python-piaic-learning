# 07_class(Dictionary)

#  >>>>>>>>

# List                    0                1            2
data : list[str] = ["Muhammad Aslam","Muhammad Qasim","MSDS"]

print(data[1])
# Muhammad Qasim


#  >>>>>>>>

data : set = {7,1,2,1,1,1,1,3,2}
print(data) # return unique
{1, 2, 3, 7}



#  >>>>>>>>

[i for i in dir(data) if "__" not in i]
['add',
 'clear',
 'copy',
 'difference',
 'difference_update',
 'discard',
 'intersection',
 'intersection_update',
 'isdisjoint',
 'issubset',
 'issuperset',
 'pop',
 'remove',
 'symmetric_difference',
 'symmetric_difference_update',
 'union',
 'update']

#  >>>>>>>>

# data : set = {7,1,2,1,1,1,1,3,2}
# print(data[0]) # return unique
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# Cell In[22], line 2
#       1 data : set = {7,1,2,1,1,1,1,3,2}
# ----> 2 print(data[0]) # return unique

# TypeError: 'set' object is not subscriptable


#  >>>>>>>>

# Dictionary
# key:value (items)

# key replacement of indexes
# value item
# dict_variable[key]

# dict_variable[new_key] = new_value
# add new value
# update value


#  >>>>>>>>

from typing import Dict
import pprint

# List                    0                1            2
data : Dict[str,str] = {
                        "fname":"Muhammad Aslam",
                        "name":"Muhammad Qasim",
                        "education": "MSDS"
                        }

pprint.pprint(data)


# {'education': 'MSDS', 'fname': 'Muhammad Aslam', 'name': 'Muhammad Qasim'}


#  >>>>>>>>

from typing import Dict, Union, Optional
import pprint


Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

# List                    0                1            2
data : Dict[Key,Value] = {
                        "fname":"Muhammad Aslam",
                        "name":"Muhammad Qasim",
                        "education": "MSDS"
                        }

pprint.pprint(data)

# {'education': 'MSDS', 'fname': 'Muhammad Aslam', 'name': 'Muhammad Qasim'}

#  >>>>>>>>


from typing import Dict, Union, Optional
import pprint


Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

# List                    0                1            2
data : Dict[Key,Value] = {
                        "fname":"Muhammad Aslam",
                        "name":"Muhammad Qasim",
                        "education": "MSDS"
                        }

pprint.pprint(data)
print(data["name"])
print(data['fname'])
print(data['education'])
{'education': 'MSDS', 'fname': 'Muhammad Aslam', 'name': 'Muhammad Qasim'}
# Muhammad Qasim
# Muhammad Aslam
# MSDS



#  >>>>>>>>

from typing import Dict, Union, Optional
import pprint

Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

# List                    0                1            2
data : Dict[Key,Value] = {
                        "fname":"Muhammad Aslam",
                        "name":"Muhammad Qasim",
                        "education": "MSDS",
                        0 : "Pakistan"
                        }

pprint.pprint(data)
print(data["name"])
print(data['fname'])
print(data['education'])
print(data[0]) # index = key
{0: 'Pakistan',
 'education': 'MSDS',
 'fname': 'Muhammad Aslam',
 'name': 'Muhammad Qasim'}
# Muhammad Qasim
# Muhammad Aslam
# MSDS
# Pakistan


#  >>>>>>>>

from typing import Dict, Union, Optional
import pprint


Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

# List                    0                1            2
data : Dict[Key,Value] = {
                        "fname":"Muhammad Aslam",
                        "name":"Muhammad Qasim",
                        "education": "MSDS",
                        # [1,2,3] : "Pakistan", # error
                        # (1,2,3) : "Pakistan", #error
                        # {1,2,3} : "pakistan", #error
                        }

pprint.pprint(data)
print(data["name"])
print(data['fname'])
print(data['education'])
# print(data[0]) # index = key


#  >>>>>>>>

from typing import Dict, Union, Optional
import pprint


Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

# List                    0                1            2
data : Dict[Key,Value] = {
                        "fname":"Muhammad Aslam",
                        "name":"Muhammad Qasim",
                        "education": "MSDS",
                        "abc" : [1,2,3],
                        'xyz': {1,2,3},
                        'efg' : (1,2,3),
                        'cde' : {"a":1, "b":2}
                        # [1,2,3] : "Pakistan", # error
                        # (1,2,3) : "Pakistan", #error
                        # {1,2,3} : "pakistan", #error
                        }

pprint.pprint(data)
print(data["name"])
print(data['fname'])

print(data['xyz'])
print(data['education'])
{'abc': [1, 2, 3],
 'cde': {'a': 1, 'b': 2},
 'education': 'MSDS',
 'efg': (1, 2, 3),
 'fname': 'Muhammad Aslam',
 'name': 'Muhammad Qasim',
 'xyz': {1, 2, 3}}
Muhammad Qasim
Muhammad Aslam
{1, 2, 3}
MSDS


#  >>>>>>>>


abc : set = {1,2,3,2,2,2,1}
print(abc)
xyz : list[int] = list(abc)
print(xyz)
{1, 2, 3}
[1, 2, 3]

#  >>>>>>>>

from typing import Dict, Union, Optional
import pprint


Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

# List                    0                1            2
data : Dict[Key,Value] = {
                        "fname":"Muhammad Aslam",
                        "name":"Muhammad Qasim",
                        "education": "MSDS",
                        "abc" : [1,2,3],
                        'xyz': {1,2,3},
                        'efg' : (1,2,3),
                        'cde' : {"a":1, "b":2}
                        # [1,2,3] : "Pakistan", # error
                        # (1,2,3) : "Pakistan", #error
                        # {1,2,3} : "pakistan", #error
                        }

data['cde']['b']
2

#  >>>>>>>>


from typing import Dict, Union, Optional
import pprint


Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

data : dict[Key,Value] = {}

data['name'] = "Muhammad Qasim" #add new key and values
data['fname'] = "Muhammad Aslam"
data['education'] = "MSDS"

print(data)
{'name': 'Muhammad Qasim', 'fname': 'Muhammad Aslam', 'education': 'MSDS'}
#  >>>>>>>>

from typing import Dict, Union, Optional
import pprint


Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

data : Dict[Key,Value] = {
                        "fname":"Muhammad Aslam",
                        "name":"Muhammad Qasim",
                        "education": "MSDS"}


print(data)

data['name'] = "M.Qasim" # update

print(data)
{'fname': 'Muhammad Aslam', 'name': 'Muhammad Qasim', 'education': 'MSDS'}
{'fname': 'Muhammad Aslam', 'name': 'M.Qasim', 'education': 'MSDS'}


#  >>>>>>>>

from typing import Dict, Union, Optional
import pprint


Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

data : Dict[Key,Value] = {
                        "fname":"Muhammad Aslam",
                        "name":"Muhammad Qasim",
                        "education": "MSDS"}



print(data['pakistan'])

[i for i in dir(data) if "__" not in i]
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
Cell In[35], line 15
      6 Value = Union[int, str, list, dict, tuple, set]
      8 data : Dict[Key,Value] = {
      9                         "fname":"Muhammad Aslam",
     10                         "name":"Muhammad Qasim",
     11                         "education": "MSDS"}
---> 15 print(data['pakistan'])
     17 [i for i in dir(data) if "__" not in i]

KeyError: 'pakistan'


#  >>>>>>>>

from typing import Dict, Union, Optional
import pprint


Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

data : Dict[Key,Value] = {
                        "fname":"Muhammad Aslam",
                        "name":"Muhammad Qasim",
                        "education": "MSDS"}


#                 key
print(data.get('pakistan',"NA"))
print(data.get('name',"NA"))

[i for i in dir(data) if "__" not in i]
NA
Muhammad Qasim
['clear',
 'copy',
 'fromkeys',
 'get',
 'items',
 'keys',
 'pop',
 'popitem',
 'setdefault',
 'update',
 'values']

#  >>>>>>>>

from typing import Dict, Union, Optional
import pprint


Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

data : Dict[Key,Value] = {
                        "fname":"Muhammad Aslam",
                        "name":"Muhammad Qasim",
                        "education": "MSDS"}


for d in data:
    print(d) # keys


# [i for i in dir(data) if "__" not in i]
# fname
# name
# education



#  >>>>>>>>

from typing import Dict, Union, Optional
import pprint


Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

data : Dict[Key,Value] = {
                        "fname":"Muhammad Aslam",
                        "name":"Muhammad Qasim",
                        "education": "MSDS"}


print(data.keys()) # keys
print(data.values()) # values
print(data.items())

for k in data.keys():
    print(k)


# [i for i in dir(data) if "__" not in i]
# dict_keys(['fname', 'name', 'education'])
# dict_values(['Muhammad Aslam', 'Muhammad Qasim', 'MSDS'])
# dict_items([('fname', 'Muhammad Aslam'), ('name', 'Muhammad Qasim'), ('education', 'MSDS')])
# fname
# name
# education



#  >>>>>>>>


from typing import Dict, Union, Optional
import pprint


Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

data : Dict[Key,Value] = {
                        "fname":"Muhammad Aslam",
                        "name":"Muhammad Qasim",
                        "education": "MSDS"}


print(data.keys()) # keys
print(data.values()) # values
print(data.items())

for v in data.values():
    print(v)


# [i for i in dir(data) if "__" not in i]
# dict_keys(['fname', 'name', 'education'])
# dict_values(['Muhammad Aslam', 'Muhammad Qasim', 'MSDS'])
# dict_items([('fname', 'Muhammad Aslam'), ('name', 'Muhammad Qasim'), ('education', 'MSDS')])
# Muhammad Aslam
# Muhammad Qasim
# MSDS

#  >>>>>>>>

from typing import Dict, Union, Optional
import pprint


Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

data : Dict[Key,Value] = {
                        "fname":"Muhammad Aslam",
                        "name":"Muhammad Qasim",
                        "education": "MSDS"}


print(data.keys()) # keys
print(data.values()) # values
print(data.items())

for k,v in data.items():
    print(k,v)
dict_keys(['fname', 'name', 'education'])
dict_values(['Muhammad Aslam', 'Muhammad Qasim', 'MSDS'])
dict_items([('fname', 'Muhammad Aslam'), ('name', 'Muhammad Qasim'), ('education', 'MSDS')])
fname Muhammad Aslam
name Muhammad Qasim
education MSDS

#  >>>>>>>>

{v:k for k,v in data.items()}
{'Muhammad Aslam': 'fname', 'Muhammad Qasim': 'name', 'MSDS': 'education'}

#  >>>>>>>>


a : int = 7
b : int = 9

a, b = b, a # shuffle

print(a,b)
9 7


#  >>>>>>>>

keys : list[str] = ['id','name','fname','course']

data : dict[Key,Value] = {}

print(data)

data = data.fromkeys(keys) # inline

print(data)
{}
{'id': None, 'name': None, 'fname': None, 'course': None}