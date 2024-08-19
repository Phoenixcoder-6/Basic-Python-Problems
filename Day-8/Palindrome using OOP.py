class check:
    def __init__(self,text):
        self.txt=text
    
    def palindrome(self):
        rev= self.txt[:: -1]

        if rev == self.txt:
            return True
        else:
            return False

def main():
    t1= check("AKA")
    print(t1.palindrome())

if __name__== "__main__":
    main()
