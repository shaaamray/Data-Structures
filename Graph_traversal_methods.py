# 4 type of traversal methods in Graph
# Inorder (Top most left, root of it, right of it)
# Preorder (Root, left subtree, right subtree)
# Postorder (Left subtree, right subtree, root)
# Level order (level by level)


from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

def inorder(self):
    n = self
    if n is None:
        return
    inorder(n.left_child)
    print(n.data)
    inorder(n.right_child)

def preorder(self):
    n = self
    if n is None:
        return
    print(n.data)
    preorder(n.left_child)
    preorder(n.right_child)

def postorder(self):
    n = self
    if n is None:
        return
    postorder(n.left_child)
    postorder(n.right_child)
    print(n.data)

def levelorder(self):
    mylist = []
    n = self
    queue = deque([n])
    while len(queue) > 0:
        node = queue.popleft()
        mylist.append(node.data)
        if node.left_child:
            queue.append(node.left_child)
        if node.right_child:
            queue.append(node.right_child)
    print(mylist)

n1 = Node("Root node")
n2 = Node("Left node")
n3 = Node("Right node")
n4 = Node("Grand left node")
n5 = Node("Grand right node")


n1.left_child = n2
n1.right_child = n3
n2.left_child = n4
n2.right_child = n5

inorder(n1)
print("")
preorder(n1)
print("")
postorder(n1)
print("")
levelorder(n1)
