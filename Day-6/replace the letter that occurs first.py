string= input("Enter the string:")
r= string[0]
print(r)
string1= string[1:].replace(r, "$",1)
    
print(r+ string1)