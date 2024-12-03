n= int(input("Enter the number of items in a dictionary:"))
sample_dict={}
for _ in range(n):
    k= input("Enter the key value:")
    v=input("Enter the value:")
    sample_dict[k]=v

print("\nOriginal distionary:",sample_dict)

sample2= list(sample_dict.items())
sample2.sort()
print("Ascending orderd:", dict(sample2))

sample2.sort(reverse=True)
print("Decending order:", dict(sample2))