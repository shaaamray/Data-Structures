class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def traverse(self):
        if self.top is None:
            print("Stack is empty")
        else:
            while self.top.next is not None:
                print(self.top.data)
                self.top = self.top.next
            print(self.top.data)

    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.size += 1

    def pop(self):
        if self.top is None:
            print("Already Empty")
            return
        else:
            if self.top.next is not None:
                value = self.top.data
                self.top = self.top.next
                print("Popped out", value)
            else:
                self.top = None
            self.size -= 1

    def peek(self):
        if self.top is not None:
            print("Top value is ;", self.top.data)
        else:
            print("Stack is empty")

    def length(self):
        if self.size == 0:
            print("Empty stack")
        else:
            print("Stack length is :", self.size)


def brackets(expression):
    bracket_stack = Stack()
    last = " "
    for i in expression:
        if i in ('{', '[', '('):
            bracket_stack.push(i)
        if i in ('}', ']', ')'):
            last = bracket_stack.pop()
            if last =='{' and i =='}':
                continue
            elif last =='[' and i ==']':
                continue
            elif last =='(' and i ==')':
                continue
            else:
                return False
    if bracket_stack.size > 0:
        return False
    else:
        return True

obj = Stack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.pop()
obj.peek()
obj.traverse()
obj.length()