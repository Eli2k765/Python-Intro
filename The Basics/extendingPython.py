#To import modules we use the import keyword
import sys

#To import a specific function from a module we use the from keyword
from math import sqrt

#To import a specific function from a module and rename it we use the from keyword and the as keyword
from datetime import datetime as dt

#If you want to know what functions are available in a module you can use the dir() function
print(dir(sys))

#If you are using a module that has a lot of functions you can use the help() function to get more information about the module
#help(sys)

mathShowcase = sqrt(121)

print(mathShowcase)

#Since we imported datetime as dt we can use dt instead of datetime
print(dt.now())

#Lets create a custom module and import it
#To create a custom module we create a file with the .py extension and add the functions we want to use
file = open("customModule.py", "w")
file.write("def customFunction():\n\tprint(\"This is a custom function\")")
file.close()

#We can also import custom modules that we have created in the same directory
import customModule

#Then we can use the functions in the custom module
customModule.customFunction()

#There are also modules that are not included in the standard library but are available for download. You can learn more about these by visiting https://pypi.org/

#To install a module we use the pip command in the terminal
#pip install <module name>

#To uninstall a module we use the pip command in the terminal
#pip uninstall <module name>

#Once we have installed a module we can import it just like any other module

from pwntools import *

#We will cover pwntools in more detail later
