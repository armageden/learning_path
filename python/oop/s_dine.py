#task 3
class SultansDine:
  total_branch=0
  branch=[]
  sell_total=0
  def __init__(self,name):
    self.branch=name
    self.sell=0
    SultansDine.total_branch+=1
    SultansDine.branch.append(self)
  @classmethod
  def details(cls):
    print(f"Total Number of branch(s): {cls.total_branch}\nTotal Sell: {cls.sell_total}")
    for branch in (cls.branch):
      percent=round((branch.sell/cls.sell_total)*100,2)
      print(f"Branch Name: {branch.branch} Branch Sell: {branch.sell}\nBranch consists of total sell's: {percent}%")

  def sellQuantity(self,num):
    if num<10:
      self.sell=num*300
    elif num<20:
      self.sell=num*350
    else:
      self.sell=num*400
    SultansDine.sell_total+=self.sell
  def branchInformation(self):
    print(f"Branch Name: {self.branch}\nBranch Sell: {self.sell} Taka")
  




# Write your code here

SultansDine.details()
print('########################')
dhanmondi = SultansDine('Dhanmondi')
dhanmondi.sellQuantity(25)
dhanmondi.branchInformation()
print('-----------------------------------------')
SultansDine.details()

print('========================')

baily_road = SultansDine('Baily Road')
baily_road.sellQuantity(15)
baily_road.branchInformation()
print('-----------------------------------------')
SultansDine.details()

print('========================')

gulshan = SultansDine('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('-----------------------------------------')
SultansDine.details()
