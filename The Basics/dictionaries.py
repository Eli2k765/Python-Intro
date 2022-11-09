#A dictionary is a collection of key-value pairs that are unordered, changeable, and indexed. 
#In Python dictionaries are written with curly brackets.

dict1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print(dict1)

#You can access the items of a dictionary by referring to its key name, inside square brackets.
print(dict1["a"])

#There is also a method called get() that will give you the same result.
print(dict1.get("a"))

#You can change the value of a specific item by referring to its key name.
dict1["a"] = 6
print(dict1["a"])

#You can not have duplicate key names in a dictionary.

#You can loop through a dictionary by using a for loop.
for i in dict1:
    print(i)
#When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
for i in dict1:
    print(dict1[i])

#You can also use the values() method to return values of a dictionary.
for i in dict1.values():
    print(i)

#You can use the items() method to return both keys and values of a dictionary.
for i, j in dict1.items():
    print(i, j)

