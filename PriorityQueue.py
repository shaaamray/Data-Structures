class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.queue = []

    #for inserting in priority queue we have 2 scenarios
    #-->if the queue is empty value is inserted
    #-->if not empty, check for the position where the priority satisfies rules

    def insert(self, node):
        if len(self.queue) == 0:
            self.queue.append(node)
        else:
            for i in range(0, len(self.queue)):
                if node.priority >= self.queue[i].priority:
                    if i == len(self.queue)-1:
                        self.queue.insert(i+1, node)
                    else:
                        continue
                else:
                    self.queue.insert(i, node)
                    return True

    def show(self):
        for i in self.queue:
            print(str(i.data)+"-"+str(i.priority))

    def delete(self):
        store = self.queue.pop(0)
        print("Data deleted --> "+str(store.data) +" - "+str(store.priority))
        return store    

z = PriorityQueue()
z.insert(Node("Life", 10))
z.insert(Node("Career", 8))
z.insert(Node("Love", 2))
z.insert(Node("Passion", 6))
z.insert(Node("Responsibility", 3))
z.show()
z.delete()