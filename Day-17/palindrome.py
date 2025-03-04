def palindrome(string):
    rev= string[::-1]
    if string== rev:
        return True
    else:
        return False
    
string="Africa"
res= palindrome(string)

if res != False:
    print("This string is Palindrome")
else:
    print("This string is not a palindrome.")
