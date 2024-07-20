arr = []
n = int(input("Enter the number of elements you want to store in that array: "))

for i in range(n):
    num = int(input(f"Enter the number at position {i + 1}: "))
    arr.append(num)

d = int(input("Enter the number of times you want to rotate the array: "))
rotation_type = input("Enter 'L' for left rotation or 'R' for right rotation: ").strip().upper()

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def left_rotate(arr, d):
    n = len(arr)
    d = d % n  # To handle cases when d >= n
    reverse(arr, 0, d - 1)
    reverse(arr, d, n - 1)
    reverse(arr, 0, n - 1)
    return arr

def right_rotate(arr, d):
    n = len(arr)
    d = d % n  # To handle cases when d >= n
    reverse(arr, n - d, n - 1)
    reverse(arr, 0, n - d - 1)
    reverse(arr, 0, n - 1)
    return arr

if rotation_type == 'L':
    arr = left_rotate(arr, d)
    print("The array after left rotation is:", arr)
elif rotation_type == 'R':
    arr = right_rotate(arr, d)
    print("The array after right rotation is:", arr)
else:
    print("Invalid rotation type entered.")

