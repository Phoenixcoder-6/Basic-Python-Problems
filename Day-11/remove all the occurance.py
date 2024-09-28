def new_list(arr,num):
    lst=[]
    for i in arr:
        if i != num:
            lst.append(i)
    return lst

arr=[10,20,30,40,10,10,20,10]
result= new_list(arr,10)
print("The new list is:",result)
