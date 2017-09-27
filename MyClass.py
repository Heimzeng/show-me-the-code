import sys
class Person:
    def __init__(self,name):
        print ("init of Person")
        self.name = name
    def sayHi(self):
        print (self.name)

class Student(Person):
    def __init__(self,name,age):
        Person.__init__(self,name)
        self.age = age
        print ("init of Student")
    def sayHi(self):
        print ("im a student,im"),(self.name)
        print ("im"),self.age,("years old")