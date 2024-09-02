def check(num,power):
    if power<=0:
        return 1
    else:
        return num* check(num,power-1)
    
if __name__=='__main__':
    num= int(input("Enter the value:"))
    power= int(input("Enter the power:"))
    result= check(num,power)
    print("The result is:",check(num,power))