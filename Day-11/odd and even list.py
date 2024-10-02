def list_create(arr):
    odd_list=[]
    even_list=[]
    for i in arr:
        if i%2==0:
            even_list.append(i)
        else:
            odd_list.append(i)

    return odd_list, even_list

arr=[11,22,33,44,55]
odd_num,even_num= list_create(arr)
print(odd_num)
print(even_num)
