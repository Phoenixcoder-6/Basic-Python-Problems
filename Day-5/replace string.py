def replace_string(string, old,new):
    if old in string:
        string= string.replace(old,new)
        return string
    
string1=input("Enter actual string:")
old=input("Enter the old string:")
new= input("Replacable string:")
mn= replace_string(string1,old,new)
print(mn)
