#Basic conditional
if True:
    print("This is true")
else:
    print("This is false")

#If the condition is true, the code block will be executed
#If the condition is false, the code block will not be executed
if False:
    print("This won't print because it is true")
else:
    print("This will print because it is true")

if 1 == 1:
    print("This is true")

if not 1 == 2:
    print("This is the same as 1 != 2")

if 1 > 1:
    print("1 is greater than 1")
elif 1 < 1:
    print("1 is less than 1")
elif 1 == 1:
    print("1 is equal to 1")
else:
    print("This will not print")

if 1 == 1 and 2 == 2:
    print("This is true")

if 1 == 1 and 2 == 3:
    print("This will not print")

if 1 == 1 or 2 == 3:
    print("This is true")

if (1 == 2 or 2 == 3) or 3 == 3:
    print("This is true")

if (1 == 2 or 2 == 3) and 3 == 3:
    print("This will not print")

if 1 == 1: print("One equals one")

#This is equal to if 1 == 1: print("One equals one") else: print("One does not equal one")
print("This is true") if 1 == 1 else print("This will not print")


