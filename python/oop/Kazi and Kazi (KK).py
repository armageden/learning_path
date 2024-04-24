# task 3
class KK_tea:
    boxes=0
    dict1={'KK Regular Tea': 0}
    def __init__(self,price,tea_bag=50):
        KK_tea.boxes+=1
        self.flavour="Regular"
        self.price=price
        self.tea_bag=tea_bag
        self.weight=self.tea_bag*2
        self.status=False
    def product_detail(self):
        print(f"Name: KK {self.flavour} Tea, Weight: {self.weight}\nTea Bags: {self.tea_bag}, Price: {self.price}\nStatus: {self.status}")
    @classmethod
    def total_sales(cls):
        print(f"Total sales:{cls.dict1}")
    @classmethod
    def update_sold_status_regular(cls,*obj):
        
        for i in obj:
            i.status=True
            KK_tea.dict1['KK Regular Tea']+=1
class KK_flavoured_tea(KK_tea):
    boxes=0
    def __init__(self,flavour,price,tea_bag):
        KK_flavoured_tea.boxes+=1
        super().__init__(price,tea_bag)
        self.flavour=flavour
        self.tea=f"KK {flavour} Tea"
        if self.tea not in KK_tea.dict1:
            KK_tea.dict1[self.tea]=0
    @classmethod   
    def update_sold_status_flavoured(cls,*obj):
        
        for i in obj:
            i.status=True
            
            KK_tea.dict1[i.tea]+=1
           
    
            
        
        
        
t1 = KK_tea(250)
print("-----------------1-----------------")
t1.product_detail()
print("-----------------2-----------------")
KK_tea.total_sales()
print("-----------------3-----------------")
t2 = KK_tea(470, 100)
t3 = KK_tea(360, 75)
KK_tea.update_sold_status_regular(t1, t2, t3)
print("-----------------4-----------------")
t3.product_detail()
print("-----------------5-----------------")
KK_tea.total_sales()
print("-----------------6-----------------")
t4 = KK_flavoured_tea("Jasmine", 260, 50)
t5 = KK_flavoured_tea("Honey Lemon", 270, 45)
t6 = KK_flavoured_tea("Honey Lemon", 270, 45)
print("-----------------7-----------------")
t4.product_detail()
print("-----------------8-----------------")
t6.product_detail()
print("-----------------9-----------------")
KK_flavoured_tea.update_sold_status_flavoured(t4, t5, t6)
print("-----------------10-----------------")
KK_tea.total_sales()
