arr=[7,10,4,3,20,15]
print("Original array:",arr)
arr.sort()
print("Sorted array:",arr)

k= int(input("Enter value:"))

if 1<=k<=len(arr):
    print(arr[k-1])
else:
    print("Invalid input..")