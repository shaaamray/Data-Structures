class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):
        node = Node(data)

        if self.tail is None:
            self.tail = node
            self.head = node
        elif self.head == self.tail:
            self.tail.next = node
            node.prev = self.head
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.count += 1

    def dequeue(self):
        self.head = self.head.next
        self.head.prev = None
        self.count -= 1

    def traverse(self):
        while self.count > 0:
            print(self.head.data)
            self.head = self.head.next
            self.count -= 1

    def size(self):
        print("Queue size is :", self.count)

obj = Queue()
obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(30)
obj.dequeue()
obj.size()
obj.traverse()
