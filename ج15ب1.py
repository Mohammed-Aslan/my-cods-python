class person :
    def __init__(self,name,nickname):
        self.name=name
        self.nickname=nickname
    def __str__(self):
        return f"{self.name},{self.nickname}"
    def __repr__(self):
        return f"('{self.name}','{self.nickname}')"
    def __format__(self,country):
        if len(country)>3 :
            return f"('{self.name}','{self.nickname}')from : {country}"
        else:
            return f"('{self.name}','{self.nickname}')from : {'(not specific)'}"
            
        

k=person("mohammed ","aslan")
print(k)   
print(str(k)) 
print(repr(k))
print(format(k,"ew"))