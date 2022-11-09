#Lambdas are anonymous functions that can take any number of arguments, but can only have one expression.

add4 = lambda x: x + 4

print(add4(5))

#Lambdas can take multiple arguments.
add = lambda x, y: x + y

print(add(5, 6))

#Lambdas can be used in list comprehensions.
list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1)
list2 = [x for x in list1 if x%2==0]
print(list2)
list3 = [x for x in list1 if add4(x)%2==0]
print(list3)

#We can define a lambda and then call it in one line of code.
print((lambda x: x + 4)(5))

#Lambdas are useful when you need a quick function to do something simple.

blocks = lambda x, y : [x[i:i+y] for i in range(0, len(x), y)]

print(blocks('Hello World', 2))


