arr1=list(map(int,input("Enter the elements of 1st array:").split()))
arr2= list(map(int,input("Enter the elements of 2nd array:").split()))

uni= list(set(arr1)&set(arr2))
inter= list(set(arr1)| set(arr2))

print("The union of two array is: ", uni)
print("The intersection of two array is :", inter)