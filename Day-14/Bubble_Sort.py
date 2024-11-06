def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                temp= arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp

    return arr

arr=[]
n=int(input("Enter the number of elements in that unsorted array:"))
for i in range(n):
    num=int(input(f"Enter the number at position {i+1}: "))
    arr.append(num)
result= bubble_sort(arr)
print(result)