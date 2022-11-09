#Functions are a way to reuse code. They are also a way to organize code.
#Functions are defined using the def keyword.
def test1():
    print('This is a test function.')

test1()
test1()

#Functions can take arguments.
def test2(test):
    print('This is a test function with an argument: ', test)

test2('Hello World')

#Functions can return values.
def test3(test):
    return test

print(test3('Hello World'))

#Functions can take multiple arguments.
def test4(test1, test2):
    return test1, test2

print(test4('Hello', 'World'))

#Functions can take default arguments.
def test5(test1, test2='World'):
    return test1, test2

print(test5('Hello'))
print(test5('Goodbye'))

#Default arguments can be overridden.
print(test5('Hello', 'Universe'))

#Functions can take variable arguments.
def test6(*args):
    return args

print(test6('Hello', 'World', 'This', 'is', 'a', 'test'))

#Functions can take keyword arguments.
def test7(**kwargs):
    return kwargs

print(test7(test1='Hello', test2='World', test3='This', test4='is', test5='a', test6='test'))

#Functions can take more arguments than are defined.
def test8(s1, *more):
    return s1, more

print(test8('Hello', 'World', 'This', 'is', 'a', 'test'))

#Functions can take multiple types of arguments.
def test9(a, b, c, d):
    print(type(a), type(b), type(c), type(d))

test9("1", 2, ['l', 'i'], 4.0)

#Global variables can be accessed from within functions and outside of them.
globalVar = 'This is a global variable.'

def test10():
    print(globalVar)

test10()

print(globalVar)

#Local variables can be accessed from within functions but not outside of them.
def test11():
    localVar = 'This is a local variable.'
    print(localVar)

test11()

#Uncomment the following line to see the error.
#print(localVar)

#You can recusively call a function.
def test12(k):
    if k > 0:
        result = k + test12(k - 1)
        print(result)
    else:
        result = 0
    return result

print(test12(20))

