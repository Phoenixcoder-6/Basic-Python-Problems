def new_arr(arr1,arr2):
    lst=[]
    rst=[]
    for i in range(0,len(arr1)):
        if arr1[i]%2 !=0 :
                lst.append(arr1[i])
        if arr2[i]%2 != 0:
            lst.append(arr2[i])

    for i in range(len(arr2)):
        if arr2[i]%2 == 0:
            lst.append(arr2[i])
        if arr2[i] % 2 ==0:
             rst.append(arr2[i])
         


    arr3= lst+rst
    return arr3
            



arr1=[1,2,3,4]
arr2=[5,6,7,8]
result=new_arr(arr1,arr2)
print(result)