class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList: #chain of nodes
    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head is None:
            print('No list')
        else:
            value = self.head
            while value is not None:
                print(value.data)
                value = value.next

v1 = SinglyLinkedList()
v1.head= Node('eggs')
v2 = Node('ham')
v3 = Node('burger')

v1.head.next = v2
v2.next = v3
v1.traverse()