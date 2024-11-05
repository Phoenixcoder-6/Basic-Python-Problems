def max_min(arr):
    maximum= max(arr)
    minimum= min(arr)
    return maximum,minimum

arr=[1,34,2,3,5,90]
res1,res2= max_min(arr)
print("Maximum element:",res1,"Minimum element is:", res2)