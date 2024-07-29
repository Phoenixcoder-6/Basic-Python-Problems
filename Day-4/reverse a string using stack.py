def reverse_str(s):
    stack=[]
    for i in s:
        stack.append(i)

    reversed_str= ''

    while stack:
        reversed_str+=stack.pop()
    
    return reversed_str


string=input("Enter a string to make it reverse:")
res= reverse_str(string)
print("The reversed string is:", {res})