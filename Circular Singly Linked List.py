class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class circular_singly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def traverse(self):
        n = self.head
        if self.head is not None:
            while self.tail:
                print(n.data)
                n = n.next
                if n == self.head:
                    break
        else:
            print("Circular list is empty")

    def add_at_beginning(self, data):
        value = Node(data)
        if self.head:
            value.next = self.head

            self.tail.next = value
            self.head = value
        else:
            self.head = value
            self.tail = value

    def add_at_end(self, data):
        value = Node(data)

        if self.tail:
            self.tail.next = value
            value.next = self.head
            self.tail = value
        else:
            self.tail = value
            self.head = value

    def add_at_before_any(self, data, cmp_val):
        value = Node(data)

        if self.head is None:
            self.head = value
            self.tail = value
        else:
            n = self.head
            while n is not self.tail:
                if n.next.data == cmp_val:
                    value.next = n.next
                    n.next = value
                    return
                else:
                    n = n.next

    def add_at_after_any(self, data, cmp_val):
        value = Node(data)
        if self.head is None:
            self.head = value
            self.tail = value
        else:
            n = self.head
            while self.tail:
                if n.data == cmp_val:
                    value.next = n.next
                    n.next = value
                    break
                else:
                    n = n.next

    def delete_at_end(self):
        n = self.head
        while self.tail:
            if n.next == self.tail:
                n.next = self.head
                self.tail = n
                break
            else:
                n = n.next

    def delete_at_beginning(self):
        if self.head is None:
            return
        else:
            n = self.head
            if self.tail.next == n:
                self.tail.next = n.next
                self.head = n.next

    def delete_any(self, cmp_val):
        if self.head is None:
            return
        elif self.head.data == cmp_val:
            self.tail.next = self.head.next
            self.head = self.head.next
        else:
            m = self.head
            n = self.head
            while n is not self.tail:
                if n.next.data == cmp_val:
                    m.next = n.next.next
                    break
                n = n.next
                m = m.next

obj = circular_singly_linked_list()
obj.add_at_beginning(10)
obj.add_at_beginning(20)
obj.add_at_end(5)
obj.add_at_before_any(15, 10)
obj.add_at_before_any(7, 10)
obj.add_at_after_any(300, 10)
obj.delete_at_end()
obj.delete_at_beginning()
obj.delete_any(10)
obj.delete_any(15)
obj.traverse()