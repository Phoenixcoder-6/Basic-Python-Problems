def counter(string):
    res=string.split()
    count_letters= 0
    count_digits=0

    for c in string:
        count_letters+= c.isalpha()
        count_digits+= c.isdigit()
    return count_letters, count_digits

string= input("Enter the string:")
res= counter(string)
print("Digits and numbers are:", res)