class myList:
    def __init__(self,*num):
        self.l1=[]
        self.sum=0
        self.avg=0
        for i in num:
            self.l1.append(i)
    def merge(self,*num):
        for i in num:
            self.l1.append(i)
    def sum(self):
        for i in self.l1:
            self.sum+=i
        print(f"Sum: {self.sum}")
    def average(self):
        for i in self.l1:
            self.sum+=i
            self.avg=self.sum/len(self.l1)
        print(f"Average: {self.avg}")
            
# Driver Code
l1 =  myList(2,3,4,5,6) #you might need a list inside your class to store the values
l1.sum()
l1.merge(4,5,9)
l1.sum()
l1.average()
print("-----------------------------")
l2 =  myList()
l2.average()
l2.merge(1,2,4,8)
l2.sum()

