def repeat_char(string, m, n):
    string1= string[:m]
    result= string1 * n

    return result

string=input("Enter the string:")
m= int(input("Enter the number of characters you want to cut:"))
n=int(input("Enter how many times you want to repeat:"))

res= repeat_char(string,m,n)
print(res)