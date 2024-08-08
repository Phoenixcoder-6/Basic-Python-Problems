def accept_string(string):
    vowels='aeiou'
    for i in string:
        if i in vowels:
            return "Yes"
        else:
            return "No"

string1= input("Enter the string:")
res= accept_string(string1)
print(res)
