#We already talked about defining different types of numbers in Python.
#I'm going to show you a few more types of numbers with a different base.

#42 in hex is 0x2a
#42 in octal is 0o52
#42 in binary is 0b101010

t1_hex = 0x2a
t2_oct = 0o52
t3_bin = 0b101010

#When you print these out, you'll see that they are all of type int and have a value of 42.

print(t1_hex, t2_oct, t3_bin)
print(t1_hex + t2_oct + t3_bin)

print(type(t1_hex))

#You can also use the built-in functions hex(), oct(), and bin() to convert a number to a string in a different base.

t4_hex = hex(42)
t5_oct = oct(42)
t6_bin = bin(42)


print(t4_hex, t5_oct, t6_bin)
#But if you check the type of these, you'll see that they are all of type str.
print(type(t4_hex))

#You can use the built-in function int() to convert a string to an int in a different base but you need to declare the base like so:
t7_int = int(t4_hex, 16)
print(t7_int)
print(type(t7_int))

#Some more built-in functions for numbers are: abs(), divmod(), pow(), round(), min(), max(), sum(), and sorted().

#abs() returns the absolute value of a number.
t8_abs = abs(-42)
print(t8_abs)

#divmod() returns the quotient and remainder of a division.
t9_divmod = divmod(42, 5)
print(t9_divmod)

#pow() returns the power of a number.
t10_pow = pow(2, 3)
print(t10_pow)

#round() returns the rounded value of a number.
t11_round = round(3.141592653589793, 2)
print(t11_round)

#min() returns the smallest value of a list.
t12_min = min([1, 2, 3, 4, 5])
print(t12_min)

#max() returns the largest value of a list.
t13_max = max([1, 2, 3, 4, 5])
print(t13_max)

#sum() returns the sum of a list.
t14_sum = sum([1, 2, 3, 4, 5])
print(t14_sum)

#sorted() returns a sorted list.
t15_sorted = sorted([5, 4, 3, 2, 1])
print(t15_sorted)

#You can also use the built-in functions all() and any() to check if all or any of the values in a list are True or False.

#all() returns True if all values in a list are True.
t16_all = all([True, True, True, True, True])
print(t16_all)

#any() returns True if any value in a list is True.
t17_any = any([True, False, False, False, False])
print(t17_any)
