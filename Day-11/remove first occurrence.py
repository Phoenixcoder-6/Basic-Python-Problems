def rev(arr):
    ele= arr[0]
    arr.remove(ele)
    return arr

arr=[10,20,33,56]
result= rev(arr)
print(result)