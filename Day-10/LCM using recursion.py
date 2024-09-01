def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
    
def lcm(a,b):
    return abs(a*b)// gcd(a,b)

if __name__=='__main__':
    num1= int(input("Enter the number1:"))
    num2= int(input("Enter the number2:"))
    print("The lcm of two numbers are:", lcm(num1,num2))