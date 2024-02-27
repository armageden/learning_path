# Task 3
class GreenPhone:
    def __init__(self,name,ver,cam):
        self.name=name
        self.ver=ver
        self.cam=cam
        self.can_update=0
        if self.name[0]=="A" :
            self.can_update=2
        elif self.name[0]=="M" :
            self.can_update=3
        elif self.name[0]=="U":
            self.can_update=4
    def showSpecification(self):
        print("Phone Company: GreenPhone")
        print(f"Model Name: {self.name}")
        print(f"Android Version: {self.ver}")
        print(f"Number of Cameras: {self.cam}")
    def updatePhone(self):
        if self.ver<self.ver+self.can_update:
            
            self.ver+=1
            self.can_update-=1
            print(f"Your phone Greenphone {self.name} is upgraded to Android Version: {self.ver}")
        else:
            print(f"Your phone Greenphone {self.name} is already up to date.")
        
# Driver Code
print('1=======================')
p1 = GreenPhone('A1', 12, 3)
p2 = GreenPhone('M11', 12, 4)
p3 = GreenPhone('U20', 12, 5)
p1.showSpecification()
print('2=======================')
p2.showSpecification()
print('3=======================')
p1.updatePhone()
print('4=======================')
p1.updatePhone()
p2.updatePhone()
p3.updatePhone()
print('5=======================')
p1.updatePhone()
p2.updatePhone()
p3.updatePhone()
print('6=======================')
p2.updatePhone()
p3.updatePhone()
print('7=======================')
p1.showSpecification()
p3.showSpecification()
