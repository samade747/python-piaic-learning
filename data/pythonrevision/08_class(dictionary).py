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


#  >>>>>>>>




#  >>>>>>>>




#  >>>>>>>>




#  >>>>>>>>



#  >>>>>>>>





#  >>>>>>>>




#  >>>>>>>>



#  >>>>>>>>






#  >>>>>>>>
