from re import sub
def converter(string):
    words= string.split()
    camel_case= words[0].lower()
    for word in words[1:]:
        camel_case+= word.capitalize()
    return camel_case

string=input()
res= converter(string)
print(res)

