class Bank:
    def __init__(self):
        self.name=" "
        self.account=0
        self.balance=0
    def OpenAccount(self):
        self.name= input("Enter Account holder name:")
        self.account= int(input("Enter account no:"))
        self.balance= int(input("Enter the balance:"))
    def Showaccount(self):
        print(f"Name: {self.name} | Account No: {self.account} | Balance: {self.balance}")

def main():
    b1= Bank()
    b1.OpenAccount()
    b2= Bank()
    b2.OpenAccount()

    b1.Showaccount()
    b2.Showaccount()

if __name__=="__main__":
    main()


