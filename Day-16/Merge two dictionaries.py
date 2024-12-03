def merge_dictionary(dictionary1,dictionary2):
    z= dictionary1.copy()
    z.update(dictionary2)
    return z

n1= int(input("Enter the number of elements in 1st dictionary:"))
n2= int(input("Enter the number of elements in 2nd dictionary:"))

sample1={}
sample2={}
for _ in range(n1):
    k=input("Enter the key value:")
    v= input("Enter the value:")
    sample1[k]=v

for _ in range(n2):
    k=input("Enter the key value:")
    v= input("Enter the value:")
    sample2[k]=v


res=merge_dictionary(sample1,sample2)
print(res)