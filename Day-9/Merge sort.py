import sys
sys.setrecursionlimit(1500)  # Increase the recursion limit if needed

def divide(arr):
    if len(arr) <= 1:  # Base case: A list with 0 or 1 elements is already sorted
        return arr
    else:
        mid = len(arr) // 2  # Find the midpoint
        l_half = arr[:mid]  # Divide the array into left half
        r_half = arr[mid:]  # Divide the array into right half

        # Recursively sort the left and right halves
        l_half = divide(l_half)
        r_half = divide(r_half)

        return conquer(l_half, r_half)  # Merge the sorted halves

def conquer(left, right):
    new = []  # Array to store the merged result
    i, j = 0, 0  # Pointers for left and right subarrays

    # Merge the two sorted subarrays
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1

    # Add any remaining elements from left or right subarray
    new.extend(left[i:])
    new.extend(right[j:])
    
    return new

if __name__ == "__main__":
    arr = []
    n = int(input("Enter the length of the array: "))
    for i in range(n):
        ele = int(input(f"Enter the value at position {i}: "))
        arr.append(ele)

    sorted_arr = divide(arr)  # Sort the array using divide and conquer
    print("Sorted array:", sorted_arr)  # Print the sorted array
