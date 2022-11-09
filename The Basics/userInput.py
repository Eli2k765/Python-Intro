#The input() function allows us to prompt the user for input.
test = input("Enter a test string: ")
print("You entered: ", test)

#The input() function will always return a string.
print("The type of the input is: ", type(test))
intTest = int(input("Enter an integer: "))
print("You entered: ", intTest, " which is a ", type(intTest))

#We can use the input() function in a loop to get multiple inputs.
while True:
    test = input("Enter a test string, type quit to leave: ")
    if test == "quit":
        break
    print("You entered: ", test)
