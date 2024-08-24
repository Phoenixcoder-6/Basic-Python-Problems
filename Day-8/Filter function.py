def is_even(a):
    return a%2==0

l1=[3,4,2,5,6,7,8]
evens= list(filter(is_even,l1))
print(evens)