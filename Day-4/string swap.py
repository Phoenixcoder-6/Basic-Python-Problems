def swap(string: str) -> str:
    if len(string) <= 1:
        return string
    mid = string[1: len(string)-1]
    return string[-1] + mid + string[0]

string = input("Enter the string: ")
print(swap(string))
