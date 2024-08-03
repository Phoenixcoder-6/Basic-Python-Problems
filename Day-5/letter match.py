def find_letter(string1, list1):
    n = 0
    for char in string1:
        if char in list1:
            n += 1
    return n

# Input from the user
string = input("Enter a string: ")
list1 = input("Enter a list of characters: ")

# Check the number of matching characters
res = find_letter(string, list1)

# Print the result
if res == len(string):
    print("Completely IN")
else:
    print("Not IN")

print(f"{res} matches")
