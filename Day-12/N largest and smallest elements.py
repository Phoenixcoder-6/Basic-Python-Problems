def check(arr,n):
    arr.sort()
    smallest_list=arr[:n]
    largest_list=arr[-n:]
    return smallest_list, largest_list


arr=[1,8,2,23,7,-4,18,23,42,37,2]
small,large=check(arr,2)
print("Smallest elements list:",small)
print("Largest elements list:",large)