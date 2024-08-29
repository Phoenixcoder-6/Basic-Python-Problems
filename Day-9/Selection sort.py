import sys
def selection_sort(arr):
    n=len(arr)
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

if __name__=='__main__':
    arr=[]
    n=int(input("Enter the length of the array:"))
    for i in range(n):
        ele= int(input(f"Enter the element at position {i}:"))
        arr.append(ele)
    
    print("Unsorted array:",arr)
    print("Sorted array:",selection_sort(arr))




