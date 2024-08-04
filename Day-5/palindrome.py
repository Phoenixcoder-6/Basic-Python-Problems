def palindrome(string):
    rev= string[::-1]
    if rev==string:
        return "Palindrome"
    else:
        return False
    
string=input("Enter the string to check:")
res= palindrome(string)
print(res)