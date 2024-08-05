def check_string(string,var):
    if var in string:
        return "yes"
    else:
        return "Not present"
    
string= input()
var= input()
res= check_string(string,var)
print(res)