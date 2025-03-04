def duplicates(arr):
    freq={}
    arr2=[]
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    
    for key,value in freq.items():
        if value >1:
            arr2.append(key)

    return arr2

arr=[1,2,3,1,2,5,6,7,8]
res= duplicates(arr)
print(res)
