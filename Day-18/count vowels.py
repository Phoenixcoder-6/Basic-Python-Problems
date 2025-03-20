def count_vowel(string):
    count=0
    string= string.lower()
    for i in string:
        if i in ['a','e','i','o','u']:
            count+=1
    return count


string= 'ariona'
print("Total numver of vowels are:", (count_vowel(string)))

