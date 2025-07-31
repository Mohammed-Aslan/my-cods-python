def padd(text,length,char):
    if len(text)>=length:
        print (text)
    else:
        
        for i in range(1,length-len(text)+1):
            text=text+char
        print (text)            
        
        
padd("jasem",6,"*")   



