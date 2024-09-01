def cum(num):
    if num==0:
        return 0
    else:
        return (num%10)+ cum(num//10) 
    
if __name__=='__main__':
    num= int(input("Enter he number to check:"))
    print("The sum of the digits are:", cum(num))