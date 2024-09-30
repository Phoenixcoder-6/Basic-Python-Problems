def difference(arr1,arr2):
    lst=[]
    for i in arr1:
        if i not in arr2:
            lst.append(i)

    return lst

arr1=[10,20,30,40]
arr2= [10,20,50,60]
result=difference(arr1,arr2)
print(result)
