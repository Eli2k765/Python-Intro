#Booleans were first introduced in the varsAndTypes.py snippet but we'll cover them more in depth here.

#Booleans are a data type that can only be True or False.
t1_bool = True
t2_bool = False

# == is the equality operator and returns True if the two values are equal.

t3_bool = 42 == 42
print(t3_bool)

# != is the inequality operator and returns True if the two values are not equal.
t4_bool = 42 != 42
print(t4_bool)

#Some other comparison operators are: <, >, <=, >=, and is.
print(41 < 42)
print(41 > 42)
print(42 <= 42)
print(42 >= 42)

#is checks if two variables are the same object.
t5_bool = t1_bool is t2_bool
print(t5_bool)

#There are some special operators that can be used with booleans. The and operator returns True if both values are True.
t6_bool = True and True
print(t6_bool)

#The or operator returns True if either value is True.
t7_bool = True or False
print(t7_bool)

#The not operator returns the opposite of the value.
t8_bool = not True
print(t8_bool)

#The in operator returns True if the value is in the container.
t9_bool = 42 in [42, 43, 44]

#That is roughly the boolean operatols. There are some other operators for expressions.
#The basic operators are: +, -, *, /, //, %, **, and ~.
#If you see += or -=, it is the same as x = x + 1 or x = x - 1.
#I will not cover the basic operators here but I will cover the //, %, ~ and ** operators.


#The // operator is the floor division operator and returns the integer part of the quotient.
t10_int = 42 // 5
print(t10_int)

#The % operator is the modulus operator and returns the remainder of the division.
t11_int = 42 % 5
print(t11_int)

#The ~ operator is the bitwise not operator and returns the bitwise complement of the number.
t12_int = ~42
print(t12_int)

#The ** operator is the exponentiation operator and returns the value of the first number raised to the power of the second number.
t13_int = 2 ** 3
print(t13_int)

#The bitwise operators are: &, |, ^, <<, and >>.
#Let's cover this in binary

x = 42
print(bin(x))
print(bin(x)[2:].rjust(8, '0'))

y = 15
print(bin(y))
print(bin(y)[2:].rjust(8, '0'))

#The & operator is the bitwise and operator and returns the bitwise and of the two numbers.
print(bin(x & y)[2:].rjust(8, '0'))

#The | operator is the bitwise or operator and returns the bitwise or of the two numbers.
print(bin(x | y)[2:].rjust(8, '0'))

#The ^ operator is the bitwise xor operator and returns the bitwise xor of the two numbers.
print(bin(x ^ y)[2:].rjust(8, '0'))

#The << operator is the bitwise left shift operator and returns the bitwise left shift of the first number by the second number.
print(bin(x << 1)[2:].rjust(8, '0'))

#The >> operator is the bitwise right shift operator and returns the bitwise right shift of the first number by the second number.
print(bin(x >> 1)[2:].rjust(8, '0'))


