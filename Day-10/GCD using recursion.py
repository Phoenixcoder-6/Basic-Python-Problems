def gcd(n1,n2):
    if n2==0:
        return n1
    else:
        return gcd(n2,n1%n2)
    
if __name__=='__main__':
    num1= int(input("Enter the number1:"))
    num2= int(input("Enter the number2:"))
    print("The gcd of two numbers are", gcd(num1,num2))