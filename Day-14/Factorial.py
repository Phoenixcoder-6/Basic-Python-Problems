def factorial(num):
    if num==1:
        return 1
    else:
        return num*factorial(num-1)
    
num=5
res=factorial(num)
print(res)