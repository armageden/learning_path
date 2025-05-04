class MaxHeap:
    def __init__(self, wei):
        self.H_arr = [0] * wei  
        self.how_BIG = 0

    def insert(self, value):
        if self.how_BIG >= len(self.H_arr):
            raise Exception("Heap is full")
        self.H_arr[self.how_BIG] = value
        self.swim(self.how_BIG)
        self.how_BIG += 1

    def swim(self, k):
        while k > 0 and self.H_arr[k] > self.H_arr[(k - 1) // 2]:
            abba = (k - 1) // 2
            self.H_arr[k], self.H_arr[abba] = self.H_arr[abba], self.H_arr[k]
            k = abba

    def extractMax(self):
        if self.how_BIG == 0:
            return None
        max_val = self.H_arr[0]
        self.H_arr[0] = self.H_arr[self.how_BIG - 1]
        self.how_BIG -= 1
        self.sink(0)
        return max_val

    def sink(self, k):
        while 2 * k + 1 < self.how_BIG:
            left = 2 * k + 1
            right = 2 * k + 2
            BIGGg = left
            if right < self.how_BIG and self.H_arr[right] > self.H_arr[left]:
                BIGGg = right
            if self.H_arr[k] >= self.H_arr[BIGGg]:
                break
            self.H_arr[k], self.H_arr[BIGGg] = self.H_arr[BIGGg], self.H_arr[k]
            k = BIGGg

    def sort(self):

        result = [0] * self.how_BIG  
        temphow_BIG = self.how_BIG
        for i in range(temphow_BIG):
            result[i] = self.extractMax()  
        for i in range(temphow_BIG):


            self.insert(result[i])  
        return result  
    