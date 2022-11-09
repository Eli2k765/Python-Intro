#Sets can be used to store multiple items in a single variable. Sets are unordered, unchangeable, and do not allow duplicate values.
#Sets are written with curly brackets.

set1 = {"a", "b", "c", "d", "e"}
print(set1)

#You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
#But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
for i in set1:
    print(i)

#Once a set is created, you cannot change its items, but you can add new items.
set1.add("f")
print(set1)

#To add more than one item to a set use the update() method.
set1.update(["g", "h", "i"])
print(set1)

#It's also possible to add items from another set, or any other iterable.
set2 = {"j", "k", "l"}
set1.update(set2)
print(set1)

#We can create an empty set using the set() constructor.
set3 = set()
print(set3)

#We can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another.
set4 = set1.union(set2)
print(set4)

#To remove an item in a set, use the remove(), or the discard() method.
set4.remove("a")
print(set4)

#If the item to remove does not exist, remove() will raise an error.
#If the item to remove does not exist, discard() will NOT raise an error.
set4.discard("a")
print(set4)

#We can also use the pop() method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.
set4.pop()
print(set4)

#The clear() method empties the set.
set4.clear()
print(set4)

#The del keyword will delete the set completely.
del set4

#The set() constructor also takes an iterable object (tuples, lists, dictionaries, etc.) and will make a set of the elements in the iterable.
list1 = ["a", "b", "c", "d", "e"]
set5 = set(list1)
print(set5)
