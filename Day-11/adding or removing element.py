def adding(arr,ele):
    arr.append(ele)
    return arr

def removing(arr,ele):
    arr.pop(arr[ele])
    return arr

arr=[2,3,4]
ele=9
result= adding(arr,ele)
arr2= [1,3,4,5,2,6,56,7]
ele2= 4
result1= removing(arr2,ele2)
print("After adding a new element:", result)
print("List after removing that particular element:",result1)