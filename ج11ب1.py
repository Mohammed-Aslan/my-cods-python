class Employee:
    def __init__(self,fname,lname,age):
        if len(fname)>3 and len(lname)>3 and age>=18: 
            self.__fname=fname
            self.__lname=lname
            self.__age=age
        else:
            self.fname="null"
            self.lname="null"
            self.age="null"
            
    def setter(self,newfname):
            self.__fname=newfname
    def  getter (self)  :
            return self.__fname
    def p_detalis(self):
        print(f"{self.__fname},{self.__lname},{self.__age}")
  
k=Employee("ahmed","kenan",30)
k._Employee__fname="same" #متغير جديد للكائن 
k.p_detalis()   
print  (k._Employee__fname)
print(k.getter())  
