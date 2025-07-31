def shart(condition):
    class A:
        def printinfo(self):
            print("A")
     
    class B:
        def  printinfo(self):
            print("B")
       
    c=A if condition  else B  
    h=c()
    h.printinfo()
shart(False)