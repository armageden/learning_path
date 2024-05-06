# Write your codes here.
class Smartphone:
    def __init__(self,name=None):
        self.name=name
        self.Display=""
        self.panel=""
        self.Ram=""
        self.ddr=""
    def setName(self,name):
        self.name=name
    def addFeature(self,*feature):
        if self.name==None:
            print("Feature can not be added without phone name")
            
        else:
            name,feat=feature
            if name=="Ram":
                if feat[0]=="D":
                    self.ddr=feat
                else:
                    self.Ram=feat
            elif name=="Display":
                if feat[0]=="A":
                    self.panel=feat
                else:
                    self.Display=feat
    def printDetail(self):
        print(f"Phone Name: {self.name}")
        if self.panel==None:
            print(f"Display: {self.Display}")
        else:
            print(f"Display: {self.Display}, {self.panel}")
        if self.ddr==None:
            print(f"Ram: {self.Ram}")
        else:
            print(f"Ram: {self.Ram}, {self.ddr}")
 
 
# Do not change the following lines of code.
s1 = Smartphone()
print("=================================")
s1.addFeature("Display"," 6.1 inch")
print("=================================")
s1.setName("Samsung Note 20")
s1.addFeature("Display", "6.1 inch")
s1.printDetail()
print("=================================")
s2 = Smartphone("Iphone 12 Pro")
s2.addFeature("Display", "6.2 inch")
s2.addFeature("Ram", "6 GB")
print("=================================")
s2.printDetail()
s2.addFeature("Display", "Amoled panel")
s2.addFeature("Ram", "DDR5")
print("=================================")
s2.printDetail()
print("=================================")