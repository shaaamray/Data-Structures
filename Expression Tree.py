class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Stack:
    def __init__(self):
        self.stacklist = []

    def push(self, data):
        self.stacklist.append(data)

    def pop(self):
        return self.stacklist.pop()

exp = "3 2 + 5 3 - *".split()
stack = Stack()

for i in exp:
    if i in "+-*/":
        node = Node(i)
        node.right = stack.pop()
        node.left = stack.pop()
    else:
        node = Node(int(i))
    stack.push(node)

def calc(node):
    if node.data == "+":
        return calc(node.left) + calc(node.right)
    elif node.data == "-":
        return calc(node.left) - calc(node.right)
    elif node.data == "*":
        return calc(node.left) * calc(node.right)
    elif node.data == "/":
        return calc(node.left) / calc(node.right)
    else:
        return node.data

root = stack.pop()
ans = calc(root)
print(ans)