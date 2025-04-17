# Function
# pre-define function
# provided by in language
# user-define function
# custom function
# Similar properties on both typd
# Return and None-return function
# Return
# we can assign this function output in any variable
# None-Return
# only run we can't assign value to variable
# components
# function declaration
# function body
# function calling
# Syntax function
# def function_name(param1:type, param2:type,...)->Return_type:
#     function_body

# function_name(arg1,arg2)
# Syntaxt lambda function
# one line function
# without name
# only use in this line
# lambda param1,param2 : function_body
 
# Pre-define function
# print
# len
# id
# dir
# chr
# ord
# exec
# Return and None-return function

#  >>>>>>>>

a : int = len("Pakistan") # a = 8 Return

display(a)# 
8

#  >>>>>>>>

def piaic()->None: # declaration/function signature
    # function body start
    print("PIAIC Generative Artificial Intelligence") # statment1
    print("Python Crash course") # statment2
    # function body end


piaic() # calling
PIAIC Generative Artificial Intelligence
Python Crash course

#  >>>>>>>>

#                   param1       param2
def add_two_numbers(num1 : int , num2 : int)->int:
    return num1 + num2

add_two_numbers(7,20)# agr1, arg2

#  >>>>>>>>

def add_two_numbers(num1: int, num2:int = 0) -> int:
    print(num1, num2)
    return num1 + num2

add_two_numbers(7,2)
7 2
9

#  >>>>>>>>


# Syntaxt lambda function
# one line function
# without name
# only use in this line
# lambda param1,param2 : function_body



a = lambda num1, num2 : num1 + num2

a(7,8)
15



#  >>>>>>>>

from typing import Callable

add: Callable[[int, int], int] = lambda x, y: x + y
result = add(10, 20)  # result will be 30
print(result)
30


#  >>>>>>>>

data : list[int] = [1,2,3,4,5,6,7,8,9,10]

data = list(map(lambda x:x**2 , data))

data
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#  >>>>>>>>
data:list[int] = list(filter(lambda x:x%2==0 ,range(1,101)))

data
[2,
 4,
 6,
 8,
 10,
 12,
 14,
 16,
 18,
 20,
 22,
 24,
 26,
 28,
 30,
 32,
 34,
 36,
 38,
 40,
 42,
 44,
 46,
 48,
 50,
 52,
 54,
 56,
 58,
 60,
 62,
 64,
 66,
 68,
 70,
 72,
 74,
 76,
 78,
 80,
 82,
 84,
 86,
 88,
 90,
 92,
 94,
 96,
 98,
 100]

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

