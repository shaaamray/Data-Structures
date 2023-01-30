#the code below is for Minheap, we can do it for Maxheap also by altering the logic

class MinHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def arrange(self, val):
        while val// 2 > 0:
            if self.heap[val] < self.heap[val//2]:
                self.heap[val], self.heap[val // 2] = self.heap[val // 2], self.heap[val]
            val //= 2

    #here heapify occurs from bottom to up
    #the child compares it value with the parent, if it is smaller then it swaps

    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.arrange(self.size)

    #traveling from top to bottom in heap is called percolate down

    def delete_at_root(self):
        store = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.rearrange(1)
        return store

    def rearrange(self, val):
        while val*2 <= self.size:
            smallest_child = self.minchild(val)
            if self.heap[smallest_child] < self.heap[val]:
                self.heap[val], self.heap[smallest_child] = self.heap[smallest_child], self.heap[val]
            val = smallest_child
    
    def minchild(self, val):
        if val * 2+1 > self.size:
            return val*2
        elif self.heap[val*2] < self.heap[val*2+1]:
            return val*2
        else:
            return val*2+1

    def delete_at_any(self, val):
        store = self.heap[val]
        self.heap[val] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.rearrange(val)
        return store

    def heap_sort(self):
        sorted_array = []
        for i in range(self.size):
            item = self.delete_at_root()
            sorted_array.append(item)
        return sorted_array

    

h = MinHeap()

for i in (4, 8, 7, 2, 9, 10, 5, 1, 3, 6):
    h.insert(i)
#heap insert
print(h.heap)
#heap delete at root
n = h.delete_at_root()
print(n)
print(h.heap)
#heap delete at any
m = h.delete_at_any(2)
print(m)
print(h.heap)

z = MinHeap()

unsorted_list = [4, 8, 7, 2, 9, 10, 5, 1, 3, 6]
for i in unsorted_list:
    z.insert(i)
print("Unsorted List: {}".format(unsorted_list))

print("Sorted List: {}".format(z.heap_sort()))
