arr=[170,45,75,7,98,6]
n= len(arr)
def selection_sort(arr):
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[min_index] > arr[j]:
                min_index=j

        if (i != min_index):
            temp= arr[i]
            arr[i]=arr[min_index]
            arr[min_index] = temp

    return arr
print("Actual array:",arr)
print("Sorted array:",selection_sort(arr))


