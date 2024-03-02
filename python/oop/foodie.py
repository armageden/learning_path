# Task 2
class Foodie:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.menu = {
            'Chicken Lollipop': 15,
            'Beef Nugget': 20,
            'Americano': 180,
            'Red Velvet': 150,
            'Prawn Tempura': 80,
            'Saute Veg': 200
        }
        self.total = 0

    def pay_tips(self, tip=0):
        self.total += tip
        if tip==0:
            print("No tips to the waiter.")
        else:
            print(f"Gives {tip}/- tips to the waiter.")

    def order(self, *items):
        for item in items:
            food, amount = item.split("-")
            amount = int(amount)
            if food in self.menu:
                per_price = self.menu[food]
                price = per_price * amount
                self.total += price
                self.items.append((food, amount, per_price, price))
            print(f"Ordered - {food}, quantity - {amount}, price (per Unit) - {per_price}. \nTotal price - {price}")

    def show_orders(self):
        if not self.items:
            return f"{self.name} has 0 item(s) in the cart.\nItems: []\nTotal spent: {self.total}."  
        else:
            items_list = []
            for food,amount,per_price,price in self.items:
                items_list.append(food)
            return f"{self.name} has {len(self.items)} item(s) in the cart.\nItems: {items_list}\nTotal spent: {self.total}."
       

        
# Driver Code
menu = {'Chicken Lollipop':15,'Beef Nugget':20,'Americano':180,'Red Velvet':150,'Prawn Tempura':80,'Saute Veg':200}


f1 = Foodie('Frodo')
print(f1.show_orders())
print('1----------------------')
f1.order('Chicken Lollipop-3','Beef Nugget-6','Americano-1')
print('2----------------------')
print(f1.show_orders())
print('3----------------------')
f1.order('Red Velvet-1')
print('4----------------------')
f1.pay_tips(20)
print('5----------------------')
print(f1.show_orders())
f2 = Foodie('Bilbo')
print('6----------------------')
f2.order('Prawn Tempura-6','Saute Veg-1')
print('7----------------------')
f2.pay_tips()
print('8----------------------')
print(f2.show_orders())

