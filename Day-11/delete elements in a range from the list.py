def new_list(arr,sr,er):
    
    for i in arr[:]:
        if i>=sr and i <= er:
            arr.remove(i)

    return arr

arr=[10,20,30,40,50]
result= new_list(arr,20,30)
print(result)