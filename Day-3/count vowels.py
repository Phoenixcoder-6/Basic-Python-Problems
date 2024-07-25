str= input("Enter any string:")
c=0
for j in str:
    if j in "aeiouAEIOU":
        c=c+1
    
print(c)