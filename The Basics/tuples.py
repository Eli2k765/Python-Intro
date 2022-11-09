#Tuples are immutable lists and cannot be changed after they are created. They are declared using parentheses instead of square brackets.

t1_tuple = (1, 2, 3, 4, 5)
print("t1_tuple is of type: ", type(t1_tuple), "and has a value of: ", t1_tuple)

#Tuples can be indexed and sliced just like lists.
print("t1_tuple[0] is: ", t1_tuple[0])

#If you wanted to print the first 3 elements of the tuple, you could do this:
print("t1_tuple[0:3] is: ", t1_tuple[0:3])

#You can also use negative indexes to access elements from the end of the tuple.
print("t1_tuple[-1] is: ", t1_tuple[-1])

#Tuples can also be strings
t2_tuple = ("one", "two", "three", "four", "five")

#Tuples can be iterated over just like lists.
for i in t2_tuple:
    print(i)

#Tuples can be concatenated just like lists.
t3_tuple = t1_tuple + t2_tuple

#Tuples can be multiplied just like lists.
t4_tuple = t1_tuple * 2

#Tuples can be compared just like lists.
print("t1_tuple == t2_tuple: ", t1_tuple == t2_tuple)

#Tuples can be checked for membership just like lists.
print("1 in t1_tuple: ", 1 in t1_tuple)

#Tuples can also be unpacked just like lists.
t5_tuple = (1, 2, 3, 4, 5)
a, b, c, d, e = t5_tuple
print("a: ", a, "b: ", b, "c: ", c, "d: ", d, "e: ", e)

#Tuples can be used as keys in dictionaries.
t6_dict = {t1_tuple: "t1_tuple", t2_tuple: "t2_tuple"}
print("t6_dict: ", t6_dict)

