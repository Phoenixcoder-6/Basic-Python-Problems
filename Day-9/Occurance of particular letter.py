def check(arr,x):
    arr.sort()
    #count=0
    freq={}
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1

    return freq.get(x,0)
    """for r in freq:
        if r == x:
            count=count+1
    return count"""
    

arr=[]
x= int(input("Enter the value of x:"))
n= int(input("Enter the size of the array:"))
for i in range(n):
    ele= int(input(f"Enter the value at position {i}:"))
    arr.append(ele)

print("The frequency is:",check(arr,x))