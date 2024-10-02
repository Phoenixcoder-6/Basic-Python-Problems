def remdup(arr):
    lst=[]
    for i in arr:
        if i not in lst:
            lst.append(i)
    return lst

arr=[10,20,30,10,20,10]
result= remdup(arr)
print("Original list:",arr)
print("After removing duplicates:", result)