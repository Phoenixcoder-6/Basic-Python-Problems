def count_occurrence(string, var):
    freq = {}
    count = 0
    for word in string.split():
        if word == var:
            count += 1
    if count > 0:
        freq[var] = count
    return freq

string = input("Enter the string: ")
var = input("Enter the word you want to check: ")
res = count_occurrence(string, var)
print(res)
