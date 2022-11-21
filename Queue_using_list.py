class QueueList:
    def __init__(self):
        self.item = []
        self.head = 0
        self.tail = 0
        self.size = 3

    def enqueue(self, data):
        if self.size == self.tail:
            print("Queue is full")
        else:
            self.item.append(data)
            self.tail += 1

    def dequeue(self):
        if self.tail == 0:
            print("Queue Empty")
        else:
            value = self.item.pop(0)
            self.tail -= 1
            print(value)

    def traverse(self):
            print(self.item)


obj = QueueList()
obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(30)
obj.dequeue()
obj.traverse()