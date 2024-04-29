# task 4
class Cakes:
    order_list = {}
    feedback_list={}

    def __init__(self, flavor, weight):
        self.flavor = flavor
        self.weight = weight
        self.sweetness = "Moderate sugar"
        self.cream_type = "Whipped Cream"
        self.price_per_kg = 1200
        self.calculate_price()
        self.add_to_order_list()

    def calculate_price(self):
        self.price = (self.weight / 1000) * self.price_per_kg

    def add_to_order_list(self):
        key = f"{self.flavor} Cake {self.weight}gm"
        if key in self.order_list:
            self.order_list[key] += 1
        else:
            self.order_list[key] = 1

    def add_customization(self, sweetness="Zero", cream_type="Butter Cream"):
        self.sweetness = sweetness
        self.cream_type = cream_type
        self.calculate_price()

    def cake_details(self):
        print(f"Flavor: {self.flavor} Cake, Weight: {self.weight} gm")
        print(f"Sweetness: {self.sweetness}, Cream Type: {self.cream_type}")
        print(f"Price: {self.price} Taka")

    @classmethod
    def give_feedbacks(cls, flavor, feedback):
        print("Thanks for your valuable feedback!")
        cls.discount_feedback(flavor)
        if flavor in cls.order_list:
            if cls.feedback_list[flavor]!=None:
                cls.feedback_list[flavor]+=feedback
            else:
                cls.feedback_list[flavor]=feedback

    @classmethod
    def discount_feedback(cls, flavor):
        if "Cheese Cake" in flavor:
            print("You will get 10% discount for your next purchase!")

    @classmethod
    def show_feedbacks(cls):
        print(cls.feedback_list)


class Cheese_Cakes(Cakes):
    def __init__(self, flavor, weight, cake_type="baked"):
        super().__init__(flavor, weight)
        self.cake_type = cake_type
        self.price_per_kg = 1500
        self.calculate_price()

    def add_customization(self):
        print("Sorry! No customization available for cheese cakes.")

    def cake_details(self):
        print(f"Flavor: {self.flavor} Cheese Cake, Weight: {self.weight} gm")
        print(f"Sweetness: {self.sweetness}, Cream Type: Cream Cheese")
        print(f"Cake Type:{self.cake_type.capitalize()}, Price: {self.price} Taka")


# Driver Code 


order_1=Cakes("Chocolate",500)
order_2=Cakes("Vanilla",800)
print("(1)**********************************")
order_1.cake_details()
print("(1.1)**********************************")
print(Cakes.order_list)
print("(2)**********************************")
order_2.add_customization("Zero","Butter Cream")
order_2.cake_details()
print("(3)**********************************")
Cakes.give_feedbacks("Chocolate Cake","Very Delicious")
Cakes.give_feedbacks("Chocolate Cake","Yummy")
print("(4)**********************************")
Cakes.show_feedbacks()
print("(5)**********************************")
ch_order1=Cheese_Cakes("Red velvet",700)
ch_order1.cake_details()
print("(6)**********************************")
ch_order1.add_customization()
print("(7)**********************************")
ch_order2=Cheese_Cakes("Blue Berry",900,"No Bake")
ch_order2.cake_details()
print("(8)**********************************")
print(Cakes.order_list)
print("(9)**********************************")
Cheese_Cakes.give_feedbacks("Red velvet Cheese Cake","Average")
Cheese_Cakes.give_feedbacks("Blue Berry Cheese Cake","Liked it")
print("(10)**********************************")
Cakes.show_feedbacks()
