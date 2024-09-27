def new_list(arr,ele,position):
    arr.insert(position,ele)
    return arr

arr=[4,5,2,3,4]
pos= 3
element=7
result= new_list(arr,element,pos)
print("The new list is:", result)