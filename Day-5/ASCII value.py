def find_ascii(string):
    m=[]
    for i in range (len(string)):
        m.append(ord(string[i]))
    return m
    
string=input()
res= find_ascii(string)
print(res)
    