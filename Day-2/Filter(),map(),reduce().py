from functools import reduce
def update(n):
    return n*2

nums=[3,4,6,2,6]
evens=list(filter(lambda n:n%2==0,nums))
print(evens)
double= list(map(update,nums))
print(double)

sum= reduce(lambda a,b:a+b,double)
print(sum)