class Transport:
    total_traveller = 0
    
    def __init__(self, name, fare):
        self.name = name
        self.baseFare = fare
    
    def __str__(self):
        s =  "Name: "+self.name+", Base fare: "+str(self.baseFare)
        return s

# Write your codes here.
class Bus(Transport):
    def __init__(self,name,fare):
        super().__init__(name,fare)
        self.passenger=[]
        self.fare=[]
        print(f"Base-fare of {self.name} is {self.baseFare} Taka")
    def addPassengerWithBags(self,*str1):
        for i in str1:
            if type(i)==str:
                self.passenger.append(i)
            else:
                if i<=2:
                    self.fare.append(self.baseFare)
                elif 3<=i<=5:
                    self.fare.append(self.baseFare+60)
                elif i>5:
                    self.fare.append(self.baseFare+105)
        Transport.total_traveller+=len(self.passenger)
    def __str__(self):
        c=""
        for i in range (len(self.passenger)):
            c+=(f"Name: {self.passenger[i]},Fare: {self.fare[i]}\n")
        return f"Name: {self.name}, Base fare: {self.baseFare}\nTotal Passenger(s):{len(self.passenger)}\nPassenger details:\n{c}"
class Train(Transport):
    def __init__(self,name,fare):
        super().__init__(name,fare)
        self.passenger=[]
        self.fare=[]
        print(f"Base-fare of {self.name} is {self.baseFare} Taka")
    def addPassengerWithBags(self,*str1):
        for i in str1:
            if type(i)==str:
                self.passenger.append(i)
            else:
                if i<=2:
                    self.fare.append(self.baseFare)
                elif 3<=i<=5:
                    self.fare.append(self.baseFare+60)
                elif i>5:
                    self.fare.append(self.baseFare+105)
        Transport.total_traveller+=len(self.passenger)
    def __str__(self):
        c=""
        for i in range (len(self.passenger)):
            c+=(f"Name: {self.passenger[i]},Fare: {self.fare[i]}\n")
        return f"Name: {self.name}, Base fare: {self.baseFare}\nTotal Passenger(s):{len(self.passenger)}\nPassenger details:\n{c}"
# Do not change the following lines of code.
t1 = Bus("Volvo", 950)
print("=================================")
t1.addPassengerWithBags("David", 6,  "Mike", 1, "Carol", 3)
print("=================================")
print(t1)
print("=================================")
t2 = Train("Silk City", 850)
print("=================================")
t2.addPassengerWithBags("Bob", 2, "Simon", 4)
print("=================================")
print(t2)
print("=================================")
print("Total Passengers in Transport: ", Transport.total_traveller)
