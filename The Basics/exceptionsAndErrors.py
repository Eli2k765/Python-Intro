#Python does little error checking. It is up to the programmer to make sure that the code does what it is supposed to do.

#The common methods of handling errors are: try, except, else, finally.

#The try block lets you test a block of code for errors and the except block lets you handle the error.
while True:
    try:
        test = int(input("Enter an integer: "))
        break
    except:
        print("That's not an integer, try again.")

#The else block lets you execute code if the try block does not raise an error.
while True:
    try:
        test = int(input("Enter an integer: "))
    except:
        print("That's not an integer, try again.")
    else:
        print("You entered: ", test)
        break

#The finally block lets you execute code, regardless of the result of the try- and except blocks.
while True:
    try:
        test = int(input("Enter an integer: "))
    except:
        print("That's not an integer, try again.")
    else:
        print("You entered: ", test)
        break
    finally:
        print("This is the finally block.")

