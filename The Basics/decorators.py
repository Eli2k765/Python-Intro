#Decorators are a way to modify functions using other functions.

from datetime import datetime
import time

#Decorator function
def time_it(func):
    def wrapper():
        start = datetime.now()
        func()
        end = datetime.now()
        print('Total time: {}'.format(end - start))
    return wrapper

#Function to be decorated
@time_it
def test():
    time.sleep(1)
    print('Hello World')

test()

#Decorators are useful for adding functionality to existing functions without modifying the function itself.
