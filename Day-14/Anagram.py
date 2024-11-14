def anagram(s1,s2):
    s1=sorted(s1.lower())
    s2=sorted(s2.lower())

    if s1==s2:
        return "Anagram"
    else:
        return "Not Anagram"
    
s1="Geek"
s2="Keeg"
res= anagram(s1,s2)
print(res)
