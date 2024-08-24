class Profit:
    def getProfit(self):
        self.profit= int(input("Enter the profit:"))
    def putProfit(self):
        print(f"Profit:",self.profit)
class Loss:
    def getLoss(self):
        self.loss= int(input("Enter loss:"))
    def putLoss(self):
        print("Loss", self.loss)
class Balance(Profit,Loss):
    def getBalance(self):
        self.getProfit()
        self.getLoss()
        self.balance= self.profit-self.loss
    def putBalance(self):
        self.putProfit()
        self.putLoss()
        print("Balance:",self.balance)


b1=Balance()
b1.getBalance()
b1.putBalance()