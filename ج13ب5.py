class Engine:
    def __init__(self ,hoursepower):
        self.hoursepower=hoursepower
    def start(self):
        print(f"engine started whith {self.hoursepower} hoursepower")
        
class Car:
    def __init__(self ,model):
        self .model=model
        self .engine=Engine("120")
    def start_car(self):
        print(f"starting car model {self.model}")
        self.engine.start()
        

k2=  Car("mersedes")      
k2.start_car()
        
        