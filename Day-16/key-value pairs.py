n= int(input("Enter the number of elements present in a dictionary:"))
sample_dict={}
for _ in range(n):
    k= input("Enter the key values:")
    v= input("Enter the values:")
    sample_dict[k]=v

print("Key values:")
for x in sample_dict:
    print(x)

print("Values:")
for x in sample_dict.values():
    print(x)

print("Full dictionary:")
for x,y in sample_dict.items():
    print(x,":",y)