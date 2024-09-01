def binary_search(arr, num):
    n = len(arr)
    sorted_arr = sorted(arr)  # Sort the array, but keep the original unchanged
    lower_bound = 0
    upper_bound = n - 1

    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2

        if num < sorted_arr[mid]:
            upper_bound = mid - 1
        elif num > sorted_arr[mid]:
            lower_bound = mid + 1
        else:
            return arr.index(num)  # Return the original index of the element

    return -1  # Element not found in the array

if __name__ == '__main__':
    arr = [5, 8, 2, 9, 3]
    num = int(input("Enter the number to search for: "))
    result = binary_search(arr, num)
    if result != -1:
        print(f"Element found at its original index {result}")
    else:
        print("Element not found in the list")


