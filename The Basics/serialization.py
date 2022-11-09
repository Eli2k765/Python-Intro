#Serialization allows us to save the state of an object to a file, and then load it back later.

import pickle
import sys

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person({self.name}, {self.age})"

    def __str__(self):
        return f"Person {self.name} is {self.age} years old."

def main():
    p1 = Person("John", 36)
    print(p1)
    # Serialize the object
    with open("person.pickle", "wb") as file:
        pickle.dump(p1, file)

    # Deserialize the object
    with open("person.pickle", "rb") as file:
        p2 = pickle.load(file)
    print(p2)

if __name__ == "__main__":
    main()

