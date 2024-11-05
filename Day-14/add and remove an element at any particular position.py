#adding an element

def add_element(arr,n,number):
    arr1=arr[n:]
    arr2=arr[:n]
    return arr1 + [number] + arr2

arr=[1,2,3,4,5]
n=2
number=90

res= add_element(arr,n,number)
print(res)


def delete_element(arr,n):
    arr.pop(n)
    return arr

arr=[1,2,3,4,5]
n=2
result= delete_element(arr,n)
print(result)
    
def add_element(arr,n,position):
    arr.insert(position,n)
    return arr

arr=[1,2,3,4,5]
n=23
position=3
res=add_element(arr,n,position)
print(res)