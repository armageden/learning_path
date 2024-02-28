class FinalT6A:
    def __init__(self, x, p):
        self.temp, self.sum, self.y = 4, 0, 1
        self.temp += 1
        self.y = self.temp - p
        self.sum = self.temp + x
        print(x, self.y, self.sum)
    def methodA(self):
        x = 0
        y = 0
        y = y + self.y
        x = self.y + 2 + self.temp
        self.sum = x + y + self.methodB(self.temp, y)
        print(x, y, self.sum)
    def methodB(self, temp, n):
        x = 0
        temp += 1
        self.y = self.y + temp
        x = x + 3 + n
        self.sum = self.sum + x + self.y
        print(x, self.y, self.sum)
        return self.sum

q1 = FinalT6A(2,1)
q1.methodA()
q1.methodA()
 