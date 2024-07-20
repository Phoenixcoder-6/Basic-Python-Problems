def find_divisor(arr,d):
    product=1

    for num in arr:
        product *= num

    remain= product % d
    return remain 

arr=[]
n= int(input(f"Enter the number the elements you want to enter in array:"))
for i in range (n):
    num= int(input(f"Enter the numbers at position {i+1}:"))
    arr.append(num)

d= int(input(f"Enter the value of d:"))

ans= find_divisor(arr,d)
print("The divisor is:", ans)

