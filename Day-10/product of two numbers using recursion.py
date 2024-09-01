def product(num1,num2):
    if num2==0:
        return 0
    else:
        return num1+product(num1,num2-1)
    
if __name__=='__main__':
    num1= int(input("Enter the number1:"))
    num2= int(input("Enter the number2:"))
    print("The product of two numbers are", product(num1,num2))