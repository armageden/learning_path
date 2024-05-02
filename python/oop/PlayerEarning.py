class PlayerEarning:
    def __init__(self,name):
        self.name=name
        self.salary=0
        self.bonus=0
        self.goal=0
    def calculateTotal(self,base,goal=0):
        self.salary=base
        self.goal=goal
        if self.goal>30:
            self.bonus=(5/100)*base+10000
        else:
            self.bonus=(5/100)*base
    def printDetails(self):
        if self.goal==0:
            print(f"Player Name: {self.name}\nPlayer Season Earning without bonus: {int(self.salary)}\nBonus: 0\nPlayer Season Earning After Bonus: {int(self.salary)}")
        else:
            
            print(f"Player Name: {self.name}\nPlayer Season Earning without bonus: {int(self.salary)}\nBonus: {self.bonus}\nPlayer Season Earning After Bonus: {int(self.salary+self.bonus)}")
        
        


# Write your code here

print("**********************")
player1 = PlayerEarning('Buffon')
player1.calculateTotal(250000)
player1.printDetails()

print("\n**********************")
player2 = PlayerEarning('Dybala')
player2.calculateTotal(250000, 31)
player2.printDetails()

print("\n**********************")
player3 = PlayerEarning('Cuadrado')
player3.calculateTotal(250000, 20)
player3.printDetails()
