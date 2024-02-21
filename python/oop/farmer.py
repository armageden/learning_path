class Farmer:
    def __init__(self,name=None):
        self.name=name
        if self.name==None:
            print(f"Welcome to your farm!")
        else:
            if type(self.name)==str:
                print(f"Welcome to your farm! {self.name}")
            else:
                print(f"Welcome to your farm. Your farm ID is {self.name}")
    def addCrops(self,*names):
        self.crops=names
        print(f"")
    def addFishes(self,*names):
        self.fishes=names
    def showGoods(self,):
        self.crops=names
        
        

# DRIVER CODE
f1 = Farmer()
print("-------------------")
f1.addCrops('Rice', "Jute", "Cinnamon")
print("-------------------")
f1.addFishes()
print("-------------------")
f1.addCrops('Mustard')
print("-------------------")
f1.showGoods()
print("-------------------")
f2 = Farmer("Korim Mia")
print("-------------------")
f2.addFishes('Pangash', 'Magur')
print("-------------------")
f2.addCrops("Wheat", "Potato")
print("-------------------")
f2.addFishes("Koi", "Tuna", "Sardine")
print("-------------------")
f2.showGoods()
print("-------------------")
f3 = Farmer(2865127000)
print("-------------------")
f3.addCrops()
print("-------------------")
f3.addFishes("Katla")
print("-------------------")
f3.showGoods()
print("-------------------")        