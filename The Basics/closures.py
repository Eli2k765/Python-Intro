#Closures are functions that refer to variables from the enclosing scope.

#The enclosing scope is the scope in which the function is defined, not the scope in which the function is called.

def outer_func():
    message = 'Hi'
    def inner_func():
        print(message)
    return inner_func

my_func = outer_func()
my_func()

#The inner_func() function is a closure because it refers to the message variable from the enclosing scope.

#Closures are useful because they allow us to avoid using global variables and they provide some form of data hiding.
