def reverse_string(s:str) ->str:
    rev= ''.join(reversed(s))
    return rev

string= input("Enter a string you want to reverse:")
res= reverse_string(string)

print("The reversed string is:", res)