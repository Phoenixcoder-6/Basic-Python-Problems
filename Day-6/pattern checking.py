def pattern_checking(arr, pattern):
    matching_strings = []
    
    for string in arr:
        if pattern in string:
            matching_strings.append(string)
    
    if matching_strings:
        return matching_strings
    return "No match found"

# Collecting input from the user
arr = []
n = int(input("Enter the number of strings: "))
for i in range(n):
    string = input(f"Enter the string at position {i+1}: ")
    arr.append(string)

pattern = input("Enter the pattern you want to check: ")
res = pattern_checking(arr, pattern)

if res != "No match found":
    print("Strings containing the pattern are:")
    for s in res:
        print(s)
else:
    print(res)
