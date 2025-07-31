class MathUtils:
    def avge(self ,list1):
        s=0
        for i in list1:
            s=s+i
        l=0    
        for j in list1:
            l=l+1
        return s/l     
    def mediator(self,list2):
        list2.sort()
        l=0    
        for j in list2:
            l=l+1
        if l%2==0:
            return (list2[(l//2)-1]+list2[l//2])/2
        else:
            return list2[l//2]
        
    def Q1(self,list3):
        list3.sort()
        l1=0  
        for j in list3:
            l1=l1+1
        if l1%2==0:
            x=(list3[(l1//2)-1]+list3[l1//2])/2
            return x
        else:
            x= list3[l1//2]
            return x
        list4=list3[:x]   
        l2=0  
        for j in list4:
            l2=l2+1
        if l2%2==0:
            x1=(list4[(l2//2)-1]+list4[l2//2])/2
            return x1
        else:
            x1= list4[l2//2]
            return x1  
    def Q3(self,list5):
        list5.sort()
        l2 = len(list5)
        if l2 % 2 == 0:
            upper_half = list5[l2 // 2:]
        else:
            upper_half = list5[(l2 // 2) + 1:]
        long = len(upper_half)
        if long % 2 == 0:
            return (upper_half[long // 2 - 1] + upper_half[long // 2]) / 2
        else:
            return upper_half[long // 2]
    def min_value(self ,list6)    :
        min=list6[0]
        for i in list6:
            if i<min:
                min=i
        return min
    def max_value(self,list7):
        max=list7[0]
        for i in list7:
            if i>max:
                max=i
        return max
    def range_minmax(self,list8):
        return list8[min(list8):max(list8)]
    
    def tabaun(self,data):
        n = len(data)
        mean = sum(data) / n
        total = 0
        for x in data:
            total += (x - mean) ** 2
        return total / n 
    def enheraf(self,data):
        n = len(data)
        mean = sum(data) / n
        total = 0
        for x in data:
            total += (x - mean) ** 2
        variance = total / n
        std_dev = variance ** 0.5
        return std_dev
    def all_data(self, lisst):
        print("...........................")

        print(f"avge : {self.avge(lisst)}")
        print(f"mediator : {self.mediator(lisst)}")
        print(f"Q1 : {self.Q1(lisst)}")
        print(f"Q3 : {self.Q3(lisst)}")
        print(f"min_value : {self.min_value(lisst)}")
        print(f"max_value : {self.max_value(lisst)}")
        print(f"rang : {self.range_minmax(lisst)}")
        print(f"t : {self.tabaun(lisst)}")
        print(f"e : {self.enheraf(lisst)}") 
 
        

k3=MathUtils()
print (k3.avge([3,4,5,2,4]))

print(k3.mediator([9,11,12,20,3,1,5]))

print(k3.Q1([2,5,4,5]))
print(k3.Q3([2,5,4,8,6,8,5]))
print (k3.max_value([2,5,4,8,6,8,5]))
print (k3.min_value([2,5,4,8,6,8,5]))
print (k3.range_minmax([2,5,4,8,6,8,5]))
print (k3.tabaun([2,5,4,8,6,8,5]))
print (k3.enheraf([2,5,4,8,6,8,5]))


k3.all_data([2,5,4,8,6,8,5])
