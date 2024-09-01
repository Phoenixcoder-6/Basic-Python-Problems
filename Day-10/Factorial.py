def check(num):
    if num==0:
        return 1
    else:
        return num*check(num-1)
    
if __name__=='__main__':
    n=6
    print(check(n))