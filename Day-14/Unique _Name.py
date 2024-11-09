def unique_name(string):
    n=len(string)
    arr=" "
    for i in range(n):
        if string[i] not in arr:
            arr+=string[i]         
    return arr
string=" AAAnkhi"
res2= unique_name(string)
print(res2)
