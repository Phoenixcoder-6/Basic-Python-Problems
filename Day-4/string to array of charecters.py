string= input("Enter a string:")

def string_converter(string):
    arr= list(string)
    res=[]
    for  word in arr:
        res.append(word)

    return res

ref= string_converter(string)
print(ref)