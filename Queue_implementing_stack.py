class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, data):
        self.stack1.append(data)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def traverse(self):
        print(self.stack1)

    def traverse2(self):
        self.stack2.reverse()
        print(self.stack2)

obj = Queue()
obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(30)

obj.traverse()
obj.dequeue()
obj.traverse2()