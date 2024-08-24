def length(string):
    if len(string)>2:
        return True

str1= ['Ankita','ok','ice']
f= list(filter(length,str1))
print(f)