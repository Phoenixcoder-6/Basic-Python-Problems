class account():

    def __init__(self,account_no,initial_balance=0):
        self.balance= initial_balance
        self.account_no= account_no

    @staticmethod
    def showdetails(account_no,balance):
        print(f"Account Number:{account_no}")
        print(f"current balance:{balance}")

    def debit(self):
        amount=int(input("Enter how much amount you want to add:"))
        self.balance+= amount
        print(self.balance)
    
    def credit(self):
        amount=int(input("Enter how much amount you want to deduct:"))
        self.balance-=amount
        print(self.balance)


def main():
    account_no = int(input("Enter your account number: "))
    initial_balance = int(input("Enter your initial balance: "))
    a1= account(account_no,initial_balance)
    a1.debit()
    a1.credit()
    account.showdetails(a1.account_no,a1.balance)

if __name__== "__main__":
    main()
