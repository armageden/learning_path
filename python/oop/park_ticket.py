# task 1
class Customer:
    def __init__(self):
        print("Welcome to ABC Memorial Park")
        self.total=0
        self.ticket=0
        
    def buyTicket(self,name,age):
        if self.ticket<3:
            if age>10:
                self.total+=100
                self.ticket+=1
                print(f"Successfully purchased a ticket for {name}!")
            else:
                self.total+=50
                self.ticket+=1
                print(f"Successfully purchased a ticket for {name}!")
        else:
            print("You can't buy more than 3 tickets")
    def showDetails(self):
        print(f"Amount of tickets: {self.ticket}")
        print(f"Total price: {self.total} Taka ")
    
print('1-------------------------')
customer1 = Customer()
print('2-------------------------')
customer1.buyTicket('Bob', 23)
customer1.buyTicket('Henry', 7)
customer1.buyTicket('Alexa', 30)
customer1.buyTicket('Jonas', 43)
print('3-------------------------')
customer1.showDetails()
print('4-------------------------')
customer2 = Customer()
print('5-------------------------')
customer2.buyTicket('Harry', 60)
customer2.buyTicket('Tomas', 28)
print('6-------------------------')
customer2.showDetails()
