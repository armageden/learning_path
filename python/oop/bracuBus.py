# task 5
class BracuStudent:
    def __init__(self, name, home):
        self.name = name
        self.home = home
        self.buspass = False

    def show_details(self):
        print(f"Student Name: {self.name}")
        print(f"Lives in {self.home}")
        print(f"Have Bus Pass? {self.buspass}")

    def get_pass(self):
        self.buspass = True


class BracuBus:
    def __init__(self, route, cap=2):
        self.route = route
        self.cap = cap
        self.passenger = []
        self.pass_count = 0

    def board(self, *student):
        for i in student:
            if self.pass_count < self.cap:
                if i.buspass:
                    if i.home == self.route:
                        self.passenger.append(i.name)
                        self.pass_count += 1
                        print(f"{i.name} boarded the bus.")
                    else:
                        print("You got on the wrong bus!")
                else:
                    print("You don't have a bus pass!")
            elif self.pass_count == self.cap:
                print("Bus is full!")

    def show_details(self):
        print(f"Bus Route: {self.route}")
        print(f"Passengers Count: {self.pass_count} (Max: {self.cap})")
        print(f"Passengers On Board: {self.passenger}")


# Driver Code
st1 = BracuStudent("Afif", "Mirpur")
print("1===========================")
st2 = BracuStudent("Shanto", "Motijheel")
st3 = BracuStudent("Taskin", "Mirpur")
st1.show_details()
st2.show_details()
print("2===========================")
st3.show_details()
print("3===========================")
bus1 = BracuBus("Mirpur")
bus2 = BracuBus("Azimpur", 5)
bus1.show_details()
bus2.show_details()
print("4===========================")
st2.get_pass()
st3.get_pass()
print("5===========================")
st2.show_details()
st3.show_details()
print("6===========================")
bus1.board()
print("7===========================")
bus1.board(st1, st2)
print("8===========================")
st1.get_pass()
st2.home = "Mirpur"
st1.show_details()
st2.show_details()
print("9===========================")
bus1.board(st1, st2, st3)
print("10===========================")
bus1.show_details()
