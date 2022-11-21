class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class slinked_list:
    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head is None:
            print("Empty List")
        else:
            value = self.head
            while value is not None:
                print(value.data)
                value = value.next

    def add(self, data):
        first_node = Node(data)
        first_node.next = self.head
        self.head = first_node
    def add_end(self, data):
        last_node = Node(data)
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = last_node
        last_node.next = None

    def delete_at_beginning(self):
        if self.head is None:
            print('Linked List is Empty')
        else:
            n = self.head
            self.head = n.next

    def delete_at_end(self):
        n = self.head
        while n.next.next is not None:
            n = n.next
        n.next = None
        
    def delete_at_any_position(self, cmp_val):
        if self.head.data == cmp_val:
            self.head = self.head.next
        else:
            n = self.head
            while n.next is not None:
                if n.next.data == cmp_val:
                    break
                n = n.next
            n.next = n.next.next


obj = slinked_list()
obj.add(10)
obj.add(20)
obj.add(30)
obj.add(10)
obj.add_end(500)
obj.delete_at_beginning()
obj.delete_at_beginning()
obj.delete_at_end()
obj.add(30)
obj.add(40)
obj.add(50)
obj.delete_at_any_position(30)
obj.traverse()