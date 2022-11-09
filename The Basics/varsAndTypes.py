#The basic way to declare a variable is to use the = operator
#The basic types are: int, float, str, list, dict, tuple, set, bool, and None

t1_int = 1
t2_float = 1.0
t3_str = "1"
t4_list = [1, 2, 3]
t5_dict = {"one": 1, "two": 2, "three": 3}
t6_tuple = (1, 2, 3)
t7_set = {1, 2, 3}
t8_bool = True
t9_none = None

#There are some other types that are not basic but are built-in
t10_bytes = b"123"
t11_bytearray = bytearray(b"123")
t12_range = range(1, 4)
t13_frozenset = frozenset({1, 2, 3})
t14_complex = 1 + 2j
t15_memoryview = memoryview(bytes(5))

#You can use the built-in function type() to check the type of a variable.
print("t1_int is of type: ", type(t1_int), "and has a value of: ", t1_int)
print("t2_float is of type: ", type(t2_float), "and has a value of: ", t2_float)
print("t3_str is of type: ", type(t3_str), "and has a value of: ", t3_str)
print("t4_list is of type: ", type(t4_list), "and has a value of: ", t4_list)
print("t5_dict is of type: ", type(t5_dict), "and has a value of: ", t5_dict)
print("t6_tuple is of type: ", type(t6_tuple), "and has a value of: ", t6_tuple)
print("t7_set is of type: ", type(t7_set), "and has a value of: ", t7_set)
print("t8_bool is of type: ", type(t8_bool), "and has a value of: ", t8_bool)
print("t9_none is of type: ", type(t9_none), "and has a value of: ", t9_none)
print("t10_bytes is of type: ", type(t10_bytes), "and has a value of: ", t10_bytes)
print("t11_bytearray is of type: ", type(t11_bytearray), "and has a value of: ", t11_bytearray)
print("t12_range is of type: ", type(t12_range), "and has a value of: ", t12_range)
print("t13_frozenset is of type: ", type(t13_frozenset), "and has a value of: ", t13_frozenset)
print("t14_complex is of type: ", type(t14_complex), "and has a value of: ", t14_complex)
print("t15_memoryview is of type: ", type(t15_memoryview), "and has a value of: ", t15_memoryview)

#You can also use some built-in functions to convert between types. 
#These are: int(), float(), str(), list(), dict(), tuple(), set(), bool(), and bytes(). 
