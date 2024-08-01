def remove_char(string,n)->str:
    if n<0:
        return 'error'
    else:
        front=string[:n]
        end= string[n+1:]
        return front+end
    
string=input()
n= int(input())
res= remove_char(string,n)

print(res)