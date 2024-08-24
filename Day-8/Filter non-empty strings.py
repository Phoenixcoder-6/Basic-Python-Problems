def is_not_empty(string):
    # Return True only for strings that are not empty and not just whitespace
    return len(string.strip()) != 0

str1 = ["Ankita", " ", "Job", " "]
f = list(filter(is_not_empty, str1))
print(f)
