arr=[]
ni= int(input("Enter the number to check:"))

n= int(input("Enter the number of elements:"))
for i in range(n):
    num= int(input(f"Enter the value at position {i}:"))
    arr.append(num)

count= arr.count(ni)
if count<=0:
    print("The number not present.")
else:
    print(f" The number {ni} occurs {count} times in that array.")




