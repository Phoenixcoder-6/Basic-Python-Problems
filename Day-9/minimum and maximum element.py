arr=[]
n= int(input("Enter the length of the array:"))
for i in range(n):
    ele= int(input(f"Enter the element at position {i}:"))
    arr.append(ele)

freq={}
def check(arr):
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1

    return freq

maximum= max(check(arr))
minimum= min(check(arr))

print("The array:",arr)

print("Maximum element:",maximum)
print("Minimum element:",minimum)


