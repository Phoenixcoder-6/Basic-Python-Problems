def string_slicing(string,n):
    string= string[:n]
    return string

string= input("Enter the string:")
n=int(input("Enter the position:"))
res= string_slicing(string,n)
print(res)