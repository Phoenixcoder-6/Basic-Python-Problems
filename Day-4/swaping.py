#swaping using third variable
temp=0
def swapping(x,y)-> int:
    temp=x
    x=y
    y=temp
    return x,y

x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
print(swapping(x,y))