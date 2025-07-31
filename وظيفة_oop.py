class Engine:
    def __init__(self,whieght,fueltype):
        self.whieght=whieght
        self.fueltype=fueltype
class Light:
    def __init__(self,color,angle):
        self.color=color
        self.angle=angle
    
class Car:
    def __init__(self,color,speed,e):
        self.color=color
        self.speed=speed
        self.engin=e
        self.lights=[]

l1=Light("red",44)
l2=Light("blue",78)

k1=Car("white",200,3) 

k1.lights.append(l1)
k1.lights.append(l2)
print(l1)
  