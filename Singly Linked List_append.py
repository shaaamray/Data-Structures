class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
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
    def addatBegin(self, data):
        fnode = Node(data)
        fnode.next = self.head
        self.head = fnode

    def addatEnd(self, data):
        endNode = Node(data)
        if self.head is None:
            self.head = endNode
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = endNode
            endNode.next = None
    # def addatMiddle(self, data):
    #     midNode = Node(data)
    #     if self.head is None:
    #         self.head = midNode
    #     else:
    #         n = self.head
    #         counter = 1
    #         while n.next is not None:
    #             n = n.next
    #             counter += 1
    #         mPos = counter // 2
    #         mPos.next = midNode
    #         midNode.next = mPos+2
    def add_afer(self, data, cmp_val):
        n = self.head
        while n is not None:
            if n.data == cmp_val:
                break
            else:
                n = n.next
        af_node = Node(data)
        af_node.next = n.next
        n.next = af_node

    def add_before(self, data, cmp_val):
        if self.head.data == cmp_val: # this part is for checking whether the given node is first node or not
            bf_node = Node(data)
            bf_node.next = self.head
            self.head = bf_node
        else: # this part is for the rest of nodes
            n = self.head
            while n is not None: # we need to find the previous node of the given node
                if n.next.data == cmp_val:  # if previous.next means current node.data is the given node then previous.node will be our desired node to compare
                    break
                n = n.next # here current node has been shifted to previous node, now despite of placing before we willl place it behind the previous node
            bf_node = Node(data)
            bf_node.next = n.next
            n.next = bf_node


lobj = SinglyLinkedList()
lobj.addatBegin(10)
lobj.addatEnd(5)
lobj.add_before(7, 5)
lobj.add_afer(8, 10)
lobj.traverse()