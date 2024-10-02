def create_list(start,end):
    lst=[]
    square_lst=[]
    cube_lst=[]
    for i in range(start,end+1):
        lst.append(i)
        square_lst.append(i*i)
        cube_lst.append(i**3)
    
    return lst, square_lst, cube_lst


org_list, sq_list,cu_list= create_list(1,10)
print("Numbers:", org_list)
print("Squares:", sq_list)
print("Cubes: ", cu_list)
