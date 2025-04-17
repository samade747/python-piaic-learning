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