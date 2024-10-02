def sublist(arr,start,end):
    lst=[]
    for num in range(start,end+1):
        lst.append(arr[num])
    return lst

arr=[10,20,30,40,50,60]
print(sublist(arr,1,4))
