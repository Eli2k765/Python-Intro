#Loops are used to iterate over a block of code a number of times.
#Python has two primitive loop commands: while and for.
#The while loop will execute a set of statements as long as a condition is true.
a = 0
while a < 10:
    print('a is currently: ',a)
    print('a is still less than 10, adding 1 to a')
    a+=1


#The for loop is used to iterate over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
for letter in 'Python':
   print ('Current Letter :', letter)

#The break and continue statements can alter the flow of a normal loop.
#The continue statement rejects all the remaining statements in the current iteration of the loop and moves the control back to the top of the loop.
while a > 0:
    print('a is currently: ',a)
    print('a is still less than 10, adding 1 to a')
    a-=1
    if a==3:
        print('Hey a is 3!')
    else:
        print('continuing...')
        continue

#The break statement breaks out of the current closest enclosing loop.
while a < 10:
    print('a is currently: ',a)
    print('a is still less than 10, adding 1 to a')
    a+=1
    if a==3:
        print('Hey a is 3!')
    else:
        print('continuing...')
        continue
    break

#You can also have nested loops, where you have a loop inside a loop.
for i in range(1,11):
    for j in range(1,11):
        print(i,'x',j,'=',i*j)
    print('Next i')

#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for i in range(1,11):
    print(i)
