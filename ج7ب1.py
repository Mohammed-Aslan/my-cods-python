num=[1,1,3,4,5,6,7,8]
left=0
right=len(num)-1
target=10
while left<right:
    if num[right]+num[left]>target:
        right-=1
    elif num[right]+num[left]<target:
        left+=1
    else :
        print(f"{num[right]}+{num[left]}={num[right]+num[left]}")
        break