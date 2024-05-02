class Bird:
    def __init__(self,name,fly=False):
        self.name=name
        self.canfly="not fly"
        if fly==True:
            self.canfly="fly"
        self.__type="Flightless Birds"
    def fly(self):
        print(f"{self.name} can {self.canfly}")
    def setType(self,type):
        self.__type=type
    def getType(self):
        return self.__type
    def printDetail(self):
        print(f"Name: {self.name}\nType: {self.__type}")


# Driver Code
ostrich = Bird('Ostrich')
duck = Bird("Duck", True)
owl = Bird('Owl', True)
print("###########################")
ostrich.fly()
duck.fly()
owl.fly()
duck.setType('Water Birds')
owl.setType('Birds of Prey')
print("=========================")
ostrich.printDetail()
print("=========================")
duck.printDetail()
print("=========================")
owl.printDetail()

