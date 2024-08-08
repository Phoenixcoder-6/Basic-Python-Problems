#removing ith element using slicing
string= input("Enter the string")
i= int(input("Enter the index of the string:"))

resstring= string[:i] + string[(i+1):]
print(resstring)