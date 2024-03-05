# Task 4
class Shopidify:
    def __init__(self, name='Guest'):
        self.serial=0
        self.status=True
        self.name = name
        self.cart = {}
        if self.name != 'Guest':
            print(f"Welcome {self.name} to Shopidify")
        else:
            print("Welcome to Shopidify")

    def add_to_cart(self, *args):
        if self.serial!=0 and self.status==True:
            self.status=False
        if len(args)==1:
            for items in args:
                if type(items)!=list:
                    if items in self.cart:
                        self.cart[items]+=1
                    else:
                        self.cart[items]=1
                
                else:
                    for i in range(len(items)-1):
                        if type(items[i])==str and type(items[i+1])==int:
                            self.cart[items[i]]=items[i+1]
                        if (type(items[i])==str and type(items[i+1])==str)  or i+1==len(items):
                            self.cart[items[i]]=1
        
        else:
            for i in range(len(args)-1):
                self.cart[args[1]]=args[i+1]
    
    def display_cart(self):
        print(f"Items in the cart for {self.name}")
        for item in self.cart:
            print(f"- {item}: {self.cart[item]}x")
    def checkout(self):
        self.status=True
        self.serial+=1
        print(f"Checkout completed for {self.name}")
    def display_history(self):
        print(f"Purchase history for {self.name}")
        
        print(f"Transaction {self.serial}:")
        for item in self.cart:
            print(f"- {item}: {self.cart[item]}x")    
        
        
        
                    
            

# Test the Shopidify class
guest_account = Shopidify()
print("1xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account = Shopidify("John")
print("2xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.add_to_cart("Air Jordan", 2)
guest_account.add_to_cart("Luffy Action Figure")
guest_account.display_cart()
print("3xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account.add_to_cart(["Chocolate Chip Cookies", 3,"Goku Action Figure",2,"Dumbbells-5kg",2])
john_account.display_cart()
print("4xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.add_to_cart("Air Jordan")
guest_account.display_cart()
print("5xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.checkout()
print("6xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.display_history()
print("7xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account.checkout()
print("8xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account.display_history()
print("9xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")