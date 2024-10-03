def new_list(arr):
    lst=[]
    for i in arr:
        if i%2 != 0:
            lst.append(i)
    return lst

arr=[11,22,33,44,55]
print(new_list(arr))