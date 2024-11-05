def rotate_array(arr,k):
    arr1= arr[-k:]
    arr2= arr[:-k]
    return arr1+ arr2

arr=[1,2,3,4,5]
k=3
res=rotate_array(arr,k)
print(res)