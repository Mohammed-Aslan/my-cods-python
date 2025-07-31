class Animal:
    def __init__(self):
        pass
    def speek(self):
      print("is done" ) 
class Dok(Animal):
    
    def __init__(self):
        pass
    def speek3(self):
        print("W")        

class Cat(Dok):
    def __init__(self):
        pass        
    def speek1(self):
        print("M")   
x=Cat()
x.speek()        
        