def position(arr,ele):
    for i in range(len(arr)):
        if arr[i] == ele:
            return i
    return -1

arr=[10,20,30,40]
ele=40
result= position(arr,ele)
print(result)

