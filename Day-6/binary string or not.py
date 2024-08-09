def check_binary(string):
    collec = {'0', '1'}
    for i in string:
        if i not in collec:
            return "Not Binary"
    return "Binary"

string = input("Enter a string: ")
res = check_binary(string)
print(res)
