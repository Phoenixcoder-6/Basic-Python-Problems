def check_string(string):
    list1="[@_!#$%^&*()<>?/\|}{~:]" 
    for i in string:
        if i in list1:
            return"Yes"
        else:
            return "NO"
        
string= input("Enter the string:")
res= check_string(string)
print(res)