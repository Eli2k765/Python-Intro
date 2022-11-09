#Lists are a data structure in Python that is a mutable, or changeable, ordered sequence of elements. Each element or value that is inside of a list is called an item. Just as strings are defined as characters between quotes, lists are defined by having values between square brackets [ ].

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']

#You can access the values in a list by using the index of the item.
print("list1[0] is: ", list1[0])
print("list2[0] is: ", list2[0])

#You can also access the values in a list by using negative indexing.
print("list1[-1] is: ", list1[-1])
print("list2[-1] is: ", list2[-1])

#You can change the value of a specific item by using its index.
list1[0] = 6
list2[0] = 'f'

#You can print out the list to see the new values.
print("list1 is now: ", list1)
print("list2 is now: ", list2)

#You can use the built-in function len() to check the length of a list.
print("The length of list1 is: ", len(list1))

#You can also nest lists (have a list inside of a list).
list3 = [list1, list2]
print("list3 is: ", list3)

#You can access the items in the nested list by using both indexes.
print("list3[0][1] is: ", list3[0][1], " and list3[1][1] is: ", list3[1][1])

#You can find the maximum and minimum values in a list.
print("The maximum value in list1 is: ", max(list1))
print("The minimum value in list2 is: ", min(list1))

#You can add items to the end of a list with the append() method.
list1.append(1)

#You can also add items anywhere in your list with the insert() method.
list1.insert(2, 1)

#If you want to check how many times an item appears in your list, you can use the count() method.
print("The number of times 1 appears in list1 is: ", list1.count(1))

#You can remove items from a list with the remove() method.
list1.remove(2)

#You can also set the value of a specific item by using its index.
list1[0] = 1
print("list1 is now: ", list1)

#The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
def times2(var):
    return var * 2

print(list(map(times2, list1)))
