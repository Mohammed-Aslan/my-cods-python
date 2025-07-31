#matrix=[[ i*j for j in range(3)] for i in range(3) ]
#print (matrix)
matrix=[]
for i in range(3):
    in3=[]
    for j in range (3):  
        in3.append(i*j)
    matrix.extend(in3)    
print (matrix)    