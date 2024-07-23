import math
arr=[]
n= int(input("Enter the number of array elemnts:"))

for i in range(n):
    num= int(input(f"enter the elemnt at position {i+1}:"))
    arr.append(num)
print (arr)

def find_lcm(arr):
    lcm=arr[0]
    for j in range (1,len(arr)):
        lcm= lcm*arr[j] // math.gcd(lcm,arr[j])
    return lcm

print(find_lcm(arr))