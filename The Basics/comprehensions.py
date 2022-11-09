#List comprehensions are a way to create lists in a single line of code.

list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1)
list2 = [x for x in list1 if x%2==0]
print(list2)

#The above code is equivalent to:
list3 = [1,2,3,4,5,6,7,8,9,10]
print(list3)
list4 = []
for x in list3:
    if x%2==0:
        list4.append(x)
    
print(list4)

#It is also possible to use if/else statements in list comprehensions.
list5 = [1,2,3,4,5,6,7,8,9,10]
print(list5)
list6 = [x if x%2==0 else 'odd' for x in list5]
print(list6)

#It is also possible to use nested if statements in list comprehensions.
list7 = [0,1,2,3,4,5,6,7,8,9,10]
print(list7)
list8 = [x if x%2==0 else 'odd' if x%2-1==0 else 'not odd or even' for x in list7]
print(list8)

#We can use join() to join the elements of a list into a string.
list9 = ['a','b','c','d','e','f','g','h','i','j']
print(list9)
print('-'.join(list9))
