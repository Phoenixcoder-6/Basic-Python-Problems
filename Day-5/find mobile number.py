import re

# Input from the user
string = input("Enter a string: ")

# Compile the regular expression for a 12-digit mobile number
Phonenumber = re.compile(r'\d{12}')

# Search for the mobile number in the input string
m = Phonenumber.search(string)

# Check if a match is found and print the result
if m:
    print("The mobile number is:", m.group())
else:
    print("No mobile number found.")
