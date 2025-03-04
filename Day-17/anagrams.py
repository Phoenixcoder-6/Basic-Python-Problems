def anagrams(string1,string2):
    if set(string1.lower()) == set(string2.lower()):
        return "Anagram"
    else:
        return "Not Anagram"
    
string1="Silent"
string2= "Listen"

res= anagrams(string1, string2)
print(res)
