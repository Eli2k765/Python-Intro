#We covered basic string declaration in the varsAndTypes.py snippet but there are a few more things we can do with strings.

#We can use the built-in function len() to get the length of a string.
t1_len = len("Hello World!")
print(t1_len)

#We can declare a long string using triple quotes.
t2_longString = """This is a long string.
It has multiple lines.
It is declared using triple quotes.
"""
print(t2_longString)

#We can escape characters using a backslash which is especially useful for newlines, backslashes and hex.
t3_escape = "This is a string with a \" in it. It also has \n a newline, a \\, and a hex value of \x2a all written on one line!"
print(t3_escape)

#Strings can be concatenated using the + operator or the += operator.
t4_concat = "Hello" + " " + "World!"
print(t4_concat)
t4_concat += " This is a concatenated string."
print(t4_concat)

#Strings can also be multiplied by an integer using the * operator.
t5_multiply = "Hello World! " * 3
print(t5_multiply)

#Strings can be indexed using square brackets. We'll cover lists in the next snippet.
t6_index = "Hello World!"
print(t6_index[3])

#There are also some built-in functions that can be used on strings.
t7_upper = "Hello World!".upper()
print(t7_upper)
t8_lower = "Hello World!".lower()
print(t8_lower)

#Another built in function is strip() which removes whitespace from the beginning and end of a string.
t9_strip = "    Hello World!    ".strip()
print(t9_strip)

#replace() can be used to replace a substring with another substring.
t10_replace = "Hello World!".replace("World", "Universe")
print(t10_replace)

#encode() can be used to convert a string an encoding method of your choice, without an arg it will encode to bytes.
t11_encode = "Hello World!".encode("utf-8"))
print(t11_encode)

#format() can be used to format a string with variables.
t12_format = "Hello {}!".format("World")
print(t12_format)

#We can also use f-strings to format a string with variables.
t13_fstring = f"Hello {'World'}!"
print(t13_fstring)




