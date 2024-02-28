class Scope:
    def __init__(self):
        self.x, self.y = 1, 100        
    def met1(self):
        x = 3
        x = self.x + 1
        self.y = self.y + self.x + 1
        x = self.y + self.met2() + self.y
        print(x, self.y)         
    def met2(self):
        y = 0
        print(self.x, y)
        self.x = self.x + y
        self.y = self.y + 200
        return self.x + y

q2 = Scope()
q2.met1()
q2.met2()
q2.met1()
q2.met2()
