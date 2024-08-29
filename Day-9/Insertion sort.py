#import sys
def insertion_sort(arr):
    n=len(arr)

    for i in range(1,n):
        key=arr[i]
        j=i-1

        while(j>=0 and key<arr[j]):
            arr[j+1] =arr[j]
            j=j-1

        arr[j+1] = key

    return arr

if __name__=='__main__':
    arr=[]
    n=int(input("Enter the length of the array:"))
    for i in range(n):
        ele= int(input(f"Enter the element at position {i}:"))
        arr.append(ele)
    
    print("Unsorted array:",arr)
    print("Sorted array:",insertion_sort(arr))


    

