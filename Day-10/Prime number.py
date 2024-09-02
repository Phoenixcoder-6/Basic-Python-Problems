def prime_no(num,i=2):
    if num%i ==0:
        return False
    elif num==i:
        return True
    return prime_no(num,i+1)

if __name__=='__main__':
    num= int(input("Enter number:"))
    check=prime_no(num)
    if check:
        print("YES",num,"is prime number")
    else:
        print("Not a prime number..")