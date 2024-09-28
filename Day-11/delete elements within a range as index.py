def new_list(arr,f_pos,l_pos):

    del arr[f_pos:l_pos]

    return arr

arr=[10,20,30,40,50]
result= new_list(arr,1,3)
print(result)
