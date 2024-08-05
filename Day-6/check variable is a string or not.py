def check_type(var):
    try:
        int(var)
        return "It is not a string"
    except ValueError:
        return "It is a string"
    
string= input()
res= check_type(string)
print(res)