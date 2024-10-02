def new_lists(arr,midpoint):
    lst1=[]
    lst2=[]
    lst1.append(arr[midpoint:])
    lst2.append(arr[:midpoint])
    return lst1,lst2

arr=[10,20,30,40,50,60]
ll,rl= new_lists(arr,3)
print(ll)
print(rl)
