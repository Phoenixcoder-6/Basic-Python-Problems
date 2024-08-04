def count_letters(string):
    count_lower=0
    count_upper=0
    letters= list[string]
    for c in string:
        if c.islower():
            count_lower += 1
        if c.isupper():
            count_upper += 1
    return count_lower, count_upper
string= input()
res=count_letters(string)
print("Lowercase and Uppercase:",res)
