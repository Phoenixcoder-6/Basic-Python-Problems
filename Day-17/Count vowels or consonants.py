def vowel_cons(string):
    string=string.lower()
    vowel=0
    consonant=0
    for i in string:
        if i in "aeiou":
            vowel+=1
        else:
            consonant+=1

    return vowel, consonant

string="AnkitaGhosh"
res1,res2= vowel_cons(string)
print(res1,res2)

