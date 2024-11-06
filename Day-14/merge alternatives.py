def mergeAlternately(word1: str, word2: str) -> str:
    string=""
    length= max(len(word1),len(word2))
    for i in range(length):
        if i<len(word1):
            string+=word1[i]
        if i<len(word2):
            string+= word2[i]

    return string

word1="abcd"
word2="pqrs"
res= mergeAlternately(word1,word2)
print(res)

        