arr=[]
n= int(input("Enter the number of elements you want to enter: "))
if n <= 0:
    print("The number of elements must be greater than 0.")
else:
    for i in range(n):
        num= int(input(f"Enter the numbers you want to enter in that array {i+1}:"))
        arr.append(num)

lar=arr[0]
for j in arr[1:]:
    if j>lar:
        lar=j
print("The largest element is:",lar)