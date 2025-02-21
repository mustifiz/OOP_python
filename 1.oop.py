class Person : 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Name: {self.name}({self.age})"    

p1 = Person("John", 36)
print(p1)    


#Create a class named Person, use the __init__() function to assign values for name and age:
#The __str__() function controls what should be returned when the class object is represented as a string.