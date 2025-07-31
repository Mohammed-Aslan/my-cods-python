class A:
    def __init__(self):
      self.__i=10

        
class C(A):
    def __init__(self):
        super().__init__()
    def printinfo(self):
        print(self._A__i)
c1=C()
c1.printinfo()
                
        
        