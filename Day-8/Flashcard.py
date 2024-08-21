class Flashcard:
    def __init__(self,word,meaning):
        self.word= word
        self.meaning=meaning
    def getword(self):
        return self.word
    def getmeaning(self):
        return self.meaning
    def __str__(self):
        return  str(self.getword()) + ':' + str(self.getmeaning())


def Flash(rec,word,meaning):
    rec.append(Flashcard(word,meaning))
    return rec

record=[]
x= 'y'
while x== 'y':
    word= input("Enter the actual Word:")
    meaning=input("Enter the meaning:")
    record= Flash(record,word,meaning)
    x= input("Want to enter another item:: y/n")

n=1
print("---Your own personal Flashcard---")
for ele in record:
    print(n,'.',ele)
    n=n+1
