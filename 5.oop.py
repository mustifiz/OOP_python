# Class Polymorphism
# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.
x = "hello world!"

#print(len(x)) # len() is a built-in Python function that returns the length of an object.

mytuple = ("apple", "banana", "cherry")

#print(len(mytuple))

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#print(len(thisdict))

# Class Polymorphism
#Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

#For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("The car is moving")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model 

    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
            print("Fly!")

#Now we can create objects from each class and call the same method on each object:

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
  x.move()