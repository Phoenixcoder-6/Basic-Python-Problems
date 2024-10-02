def check(arr,m,n):
    lst=[]
    for num in arr:
        if num %m ==0 and num % n==0:
            lst.append(num)
    return lst

arr=[10,15,20,25,30]
result= check(arr,3,5)
print(result)
    