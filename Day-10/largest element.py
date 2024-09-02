def check(arr,i):
    if i==1:
        return arr[0]
    max_ele= check(arr,i-1)
    return max(arr[i-1], max_ele)
        

if __name__=='__main__':
    num= [9,6,3,5,23]
    check1=check(num,len(num))
    print("Largest number is:",check1)
    