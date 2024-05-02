class Account:
    count=0
    def __init__(self,name,age,job,ammount):
        self.name=name
        self.age=age
        self.job=job
        self.ammount=ammount
        Account.count+=1
    def addMoney(self,num):
        self.ammount+=num
    def withdrawMoney(self,num):
        if self.ammount>=num:
          self.ammount-=num
    def printDetails(self):
        print(f"Name: {self.name}\nAge: {self.age}\nOccupation:  {self.job}\nTotal Amount:  {self.ammount}")


# Write your code here
 
print('No of account holders:', Account.count)
print("=========================")
p1 = Account("Abdul", 45, "Service Holder", 500000)
p1.addMoney(300000)
p1.printDetails()
print("=========================")
p2 = Account("Rahim", 55, "Businessman", 700000)
p2.withdrawMoney(700000)
p2.printDetails()
print("=========================")
p3 = Account("Ashraf", 62, "Govt. Officer", 200000)
p3.withdrawMoney(250000)
p3.printDetails()
print("=========================") 
print('No of account holders:', Account.count)
