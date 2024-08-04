def converter(string):
    words= string.split()
    upper_case= []
    for word in words:
        upper_case.append(word.capitalize())
    result= ' '.join(upper_case)
    return result

string= input()
res= converter(string)
print(res)