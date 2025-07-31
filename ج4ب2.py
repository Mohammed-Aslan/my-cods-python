#lambda_m=lambda x,y :max(x,y)
#print (lambda_m(3,6))

#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#even_numbers=list(filter ( lambda x: x%2==0,numbers))
#print(even_numbers)

#numbers =[1,2,4,5]
#d_numbers=list(map(lambda x:x*2,numbers))
#print(d_numbers)

#pairs = [(1, 3), (5, 1), (10, 2)]
#b=sorted(pairs,key=lambda x:x[0])
#print (b)


list_name=["Ahmed","fadi","Jasem","Mohammed"]
bool_list=list(map(lambda x:True if x[0].isupper() else False  ,list_name))
print (bool_list)
