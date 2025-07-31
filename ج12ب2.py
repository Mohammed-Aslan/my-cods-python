class Person :
    def __init__(self,fn,ln):
        self.father=fn
        self.lastname=ln
    def printdataperson(self):
        print("person")
    
class Student(Person) :
    def __init__(self,fn,ln,avg):
        super().__init__(fn,ln)
        self.avg=avg

class Employee(Person) :
    def __init__(self,fn,ln,age):
        super().__init__(fn,ln)
        self.age=age

class Teacher(Person) :
    def __init__(self,fn,ln,salary):
        super().__init__(fn,ln)
        self.salary=salary
        
s1=Student("mohammed","aslan",56)
E1=Employee("kasem","hak",44)
T1=Teacher("jana","mohammed",300)
print(E1.__dict__)
print(T1.__dict__)
p=Person("ahmed","saeed")
print(p.__dict__)