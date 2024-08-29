import sys
def bubble(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp

    return arr

if __name__=='__main__':
    arr=[]
    n=int(input("Enter the length:"))
    for i in range(n):
        ele=int(input(f"Enter at position {i}:"))
        arr.append(ele)

    print("Unsorted array:",arr)
    print("Sorted array:",bubble(arr))
    