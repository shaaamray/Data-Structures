class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class doubly_linked_list:
    def __init__(self):
        self.head = None #first node of doubly linked list
        self.tail = None #last node of doubly linked list
        self.count = 0  #number of items of nodes in the doubly linked list

    def traverse(self):
        if self.head is None:
            print("List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next

    def add_at_beginning(self, data):
        value = Node(data, None, None)

        if self.head is None:
            self.head = value
            self.tail = value
        else:
            value.next = self.head
            self.head.prev = value
            value.prev = None
            self.head = value
        self.count += 1

    def add_at_end_using_tail(self, data):
        value = Node(data, None, None)

        if self.head is None:
            self.head = value
            self.tail = None
        else:
            n = self.tail
            if n.next is None:
                n.next = value
                value.prev = n
                self.tail = value
        self.count += 1

    def add_at_end_using_head(self, data):
        value = Node(data, None, None)

        if self.head is None:
            self.head = value
            self.tail = None
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = value
            value.prev = n
            self.tail = value
        self.count += 1

    def add_at_any(self, data, cmp_val):
        value = Node(data, None, None)
        if self.head is None:
            self.head = value
            self.tail = value
        else:
            n = self.head # n = current
            m = self.head #m = previous, ei duitar majkhane bosbe new node
            while n:
                if n.data == cmp_val:
                    n.prev = value
                    value.prev = m
                    value.next = n
                    m.next = value
                m = n
                n = n.next
        self.count += 1

    def search(self, match):
        n = self.head
        while n.next is not None:
            if n.data == match:
                print("Searched value is present")
                return
            n = n.next
        print("Searched value is absent")
        return

    def delete_at_beginning(self):
        if self.head is None:
            return
        else:
            n = self.head
            m = self.head.next
            m.prev = n.prev
            m.next = n.next.next
            self.head = m
        self.count -= 1

    def delete_at_end(self):
        if self.head is None:
            return
        else:
            n = self.tail
            m = self.tail.prev
            m.next = n.next
            self.tail = m
        self.count -= 1

    def delete_at_any(self, cmp_val):
        if self.head is None:
            return
        else:
            m = self.head
            n = self.head
            o = self.head
            while n:
                if n.data == cmp_val:
                    m.next = n.next
                    o.prev = n.prev
                n = n.next
        self.count -= 1

    def list_length(self):
        print("List length is", self.count)

obj = doubly_linked_list()
obj.add_at_beginning(10)
obj.add_at_beginning(20)
obj.add_at_beginning(30)
obj.add_at_end_using_head(5)
obj.add_at_end_using_tail(3)
obj.add_at_any(15, 10)
obj.search(70)
obj.delete_at_beginning()
obj.delete_at_end()
obj.delete_at_any(15)
obj.list_length()
obj.traverse()