arr=[]
n= int(input("Enter the range of array:"))
for i in range(n):
    num= int(input(f"Enter the value at position {i}:"))
    arr.append(num)
s= sum(arr)
print(s)

