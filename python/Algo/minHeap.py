class MinHeap:
    def __init__(self, far):
        self.H_arr = [0] * far
        self.wei = 0

    def insert(self, value):
        if self.wei >= len(self.H_arr):
            raise Exception("Heap is full")
        self.H_arr[self.wei] = value
        self.swim(self.wei)
        self.wei += 1

    def swim(self, k):
        while k > 0 and self.H_arr[k] < self.H_arr[(k - 1) // 2]:
            strt = (k - 1) // 2
            self.H_arr[k], self.H_arr[strt] = self.H_arr[strt], self.H_arr[k]
            k = strt

    def extractMin(self):
        if self.wei == 0:
            return None
        min_val = self.H_arr[0]
        self.H_arr[0] = self.H_arr[self.wei - 1]
        self.wei -= 1
        self.sink(0)
        return min_val

    def sink(self, targt):
        while 2 * targt  < self.wei:
            left = 2 * targt 
            right = 2 * targt + 1
            lil = left
            if right < self.wei and self.H_arr[right] < self.H_arr[left]:
                lil = right
            if self.H_arr[targt] <= self.H_arr[lil]:
                break
            self.H_arr[targt], self.H_arr[lil] = self.H_arr[lil], self.H_arr[targt]
            targt = lil

    def sort(self):
        n = self.wei
        for i in range(n - 1, 0, -1):
            self.H_arr[0], self.H_arr[i] = self.H_arr[i], self.H_arr[0]
            self.wei -= 1
            self.sink(0)
        start, end = 0, n - 1
        while start < end:
            self.H_arr[start], self.H_arr[end] = self.H_arr[end], self.H_arr[start]
            start += 1
            end -= 1
        self.wei = n

print("===== Task 1: MinHeap =====")
min_heap = MinHeap(5)
min_heap.insert(5)
min_heap.insert(3)
min_heap.insert(8)
min_heap.insert(1)
min_heap.insert(2)

print("Extract Min:", [min_heap.extractMin() for _ in range(5)]) 

# Test Heapsort
min_heap = MinHeap(5)
min_heap.insert(5)
min_heap.insert(3)
min_heap.insert(8)
min_heap.insert(1)
min_heap.insert(2)
min_heap.sort()
print("Sorted Array (Ascending):", min_heap) 