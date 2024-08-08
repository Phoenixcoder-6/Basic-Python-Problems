string= input("Enter the string:")
coll= input("Enter separator:")

string1= string.split(' ')
res= coll.join(string1)
print(res)