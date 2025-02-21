#collection = single "variable" used to store mutliple values

#LIST = [] ordered, changeable, allows duplicates

#TUPLE = () ordered, unchangeable, allows duplicates

#SET = {} unordered, unchangeable, no duplicates

#DICTIONARY = {key:value} ordered, changeable, no duplicates

# fruits = ["apple", "banana", "cherry"]
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple in fruits:", "pineapple" in fruits)
# print(f"{fruits}s")


fruits = ("apple", "banana", "cherry")
# fruits[0] = "pineapple" #change value of list
fruits.append("pineapple") #add value to list
fruits.remove("banana") #remove value from list
fruits.pop(1) #remove value from list
fruits.insert(1, "banana") #insert value at index
fruits.sort() #sort list
fruits.reverse() #reverse list
fruits.clear() #clear list
print(fruits.index("apple")) #return index of value
print(fruits.count("apple")) #return count of value
fruits2 = fruits.copy() #copy list
fruits3 = list(fruits) #copy list


#set
fruits.add("apple") #add value to set
fruits.remove("apple") #remove value from set
fruits.discard("apple") #remove value from set
fruits.clear() #clear set
print(fruits) 


#tuple
fruits = ("apple", "banana", "cherry")
# fruits[0] = "pineapple" #change value of tuple
fruits = list(fruits) #convert tuple to list
fruits = tuple(fruits) #convert list to tuple
fruits = set(fruits) #convert list to set
fruits = list(fruits) #convert set to list
fruits = tuple(fruits) #convert list to tuple


#dictionary
fruits = {"apple": 1, "banana": 2, "cherry": 3}
fruits = dict(apple=1, banana=2, cherry=3)
fruits = dict([("apple", 1), ("banana", 2), ("cherry", 3)])
