class Program :
    def __init__(self ,nameprogram):
        self.nameprogram=nameprogram
        self.students=[]
    def printinformation(self):
        for i in self.students:
            i.printinformation()
            
        
class Student:
    def __init__(self,fn,ln,p,avg):
        self.firstname=fn
        self.lastname=ln
        self.program=p
        self.avg=avg
        self.program.students.append(self)
    def printinformation(self):
         print(self.firstname +" "+self.lastname+" "+str(self.avg))
   
p=Program("ITE")  
p1= Program("math")      
st1=Student("mohammed","badawie",p,90)
st2=Student("sami","trkien",p,44)
st3=Student("jasem","aslan",p1,67)
st4=Student("tark","aslan",p1,93)
st5=Student("mohammed","aslan",p1,83)


print(st1.program)
print(st2.program)
print(st3.program)
print(st4.program)
print(st5.program)

st1.printinformation()
list=[p,p1]
for prog in list:
    prog.printinformation()
    

      