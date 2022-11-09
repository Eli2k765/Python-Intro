#Generator functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop.

#Generator function
def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

#Generator object
val = countdown(5)

#Iterate through the generator object
for x in val:
    print(x)

#Generators are useful when you have a large amount of data that you don't want to store in memory.
