#task 1
class MinHeap:
    def __init__(self, par):
        self.farhan[par]
        cnt=par

    def insert(self, val):
        if cnt >=0:
            self.farhan[cnt] = val
            cnt += 1
            
        else:
            print("Heap is full")
        return cnt
    def swim(self, targ):
        if  self.farhan[targ] < self.farhan[(targ)//2]:
            self.farhan[targ], self.farhan[(targ-1)//2] = self.farhan[(targ-1)//2], self.farhan[targ]
            self.swim((targ)//2)         
        self.farhan[i], self.farhan[j] = self.farhan[j], self.farhan[i]
        return self.farhan


    