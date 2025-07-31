from abc import ABC,abstractmethod
class Animal(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def speak(self):
        pass
    
class doc(Animal):
    def __init__(self):
        pass
    
    def speak(self):
        print("woof")
class cat(Animal)   :
    def __init__(self):
        pass
    def speak(self):
        print("mew")
 
k1=cat()
k1.speak()      