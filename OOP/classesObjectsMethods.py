#OOP is a programming paradigm that uses objects and their interactions to design applications and computer programs.

#Methods are functions that are defined inside of a class. They are the actions that an object can perform on itself or with other objects.


#Classes are the blueprints for objects. They are the templates that define the methods and properties that objects of that class will have.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#Objects are instances of a class. They are the concrete manifestations of the class. They are the things that you interact with in your program.
p1 = Person("John", 36)
p2 = Person("Jane", 39)
print(p1.name)
print(p2.name)

#Inheritance is a way to form new classes using classes that have already been defined. The new classes are called derived classes, the classes that we derive from are called base classes. Important benefits of inheritance are code reuse and reduction of complexity of a program.
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

s1 = Student("Bill", 21, 12345)
print(s1.name)
print(s1.student_id)

#Polymorphism is the ability to take multiple forms. In programming, polymorphism allows us to define methods in the child class with the same name as the methods in the parent class. In inheritance, the child class inherits the methods from the parent class. However, it is possible to modify a method in a child class that it has inherited from the parent class. This is particularly useful in cases where the method inherited from the parent class doesn’t quite fit the child class. This is known as method overriding.
class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Cat(Animal):
    def talk(self):
        return "Meow!"

class Dog(Animal):
    def talk(self):
        return "Woof!"

animals = [Cat("Missy"), Cat("Mr. Mistoffelees"), Dog("Lassie")]

for animal in animals:
    print(animal.name + ": " + animal.talk())

#Encapsulation is the idea of bundling data and methods that work on that data within one unit. In object-oriented programming, this gives us the ability to restrict access to methods and variables. This prevents data from direct modification which is called encapsulation. To prevent accidental change, an object’s variable can only be changed by an object’s method. Those types of variables are known as private variables.
class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def set_make(self, make):
        self.__make = make

    def get_make(self):
        return self.__make

    def set_model(self, model):
        self.__model = model

    def get_model(self):
        return self.__model

    def set_year(self, year):
        self.__year = year

    def get_year(self):
        return self.__year

    def __str__(self):
        return f"{self.__make} {self.__model} ({self.__year})"

c = Car("Ford", "Mustang", 1969)
print(c)

#Abstraction is the process of hiding the implementation details from the user, only the functionality will be provided to the user. In other words, the user will have the information on what the object does instead of how it does it.
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

class Square(Shape):
    def __init__(self, x, y, side):
        super().__init__(x, y)
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return self.side * 4

class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

s = Square(0, 0, 5)
print(s.area())
print(s.perimeter())

c = Circle(0, 0, 5)
print(c.area())
print(c.perimeter())

#Operator overloading is the ability to use operators in a way that is different from their normal purpose. For example, the + operator can be used to add two numbers, but it can also be used to concatenate two strings. This is an example of operator overloading.
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2D(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Vector2D(self.x / other.x, self.y / other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"
v1 = Vector2D(5, 7)
v2 = Vector2D(3, 9)
print(v1 + v2)
print(v1 - v2)
print(v1 * v2)
print(v1 / v2)

#Class Decorators are functions that take a class as an argument and return a modified class. They are used to modify the functionality of a class without modifying the class itself.
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi())



