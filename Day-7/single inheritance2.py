class book:
    def __init__(self,author,pages):
        self.author=author
        self.pages= pages

class ebook(book):
    def __init__(self,author,pages,refno,price):
        super().__init__(author,pages)
        self.refno=refno
        self.price=price

b1=ebook("RNTagore",100,"R-56",670)
print(b1.price)