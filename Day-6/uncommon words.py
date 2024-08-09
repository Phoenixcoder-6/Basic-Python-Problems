string1= input("Enter the string 1:")
string2= input("Enter the string 2:")
words1=string1.split(" ")
words2= string2.split(" ")
list1=[]
list2=[]

for word in words1:
    if word not in words2:
        list1.append(word)
for word in words2:
    if word not in words1:
        list2.append(word)
print(list1 + list2)

