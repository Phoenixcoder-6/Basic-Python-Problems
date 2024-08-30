def check(arr,k):
    n=len(arr)
    if k>len(arr):
        return
    else:
        for i in range(n):
            for j in range(i+1,min(i+k+1,n)):
                if arr[i]==arr[j]:
                    return True
                else:
                    return False
                
arr=[2,3,5,1,6,3,5,7]
k=4
print(check(arr,k))