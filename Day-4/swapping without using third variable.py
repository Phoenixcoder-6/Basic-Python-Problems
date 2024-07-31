#swapping without using third variable

def swapping(a,b)-> int:
    a= a+b
    b= a-b
    a = a-b

    return a,b

x,y= map(int,input("Enter the two numbers").split())
print(swapping(x,y))
