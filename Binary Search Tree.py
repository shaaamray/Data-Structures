class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root_node = None

    def insert(self, data):
        node = Node(data)
        if self.root_node is None:
            self.root_node = node
        else:
            current = self.root_node
            parent = None
            while True:
                parent = current
                if node.data < parent.data:
                    current = current.left
                    if current is None:
                        parent.left = node
                        return self.root_node
                else:
                    current = current.right
                    if current is None:
                        parent.right = node
                        return self.root_node

    def search(self, data):
        current = self.root_node
        while True:
            if current is None:
                print("Node do not exist")
                return None
            elif current.data == data:
                print("Item found", data)
                return data
            elif data < current.data:
                current = current.left
            else:
                current = current.right

    def inorder(self, data):
        n = data
        if n is None:
            return
        self.inorder(n.left)
        print(n.data)
        self.inorder(n.right)

    def parent_finder(self, data):
        parent = None
        current = self.root_node
        if current is None:
            return parent, None
        while True:
            if current.data == data:
                return parent, current
            elif data < current.data:
                parent = current
                current = current.left
            else:
                parent = current
                current = current.right
        return parent, current

    def delete(self, data):
        parent, node = self.parent_finder(data)
        child = 0
        if node.left and node.right:
            child = 2
        elif node.left or node.right:
            child = 1
        else:
            child = 0

        if child == 0:
            if parent:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.root_node = None

        elif child == 1:
            next_node = None
            if node.left:
                next_node = node.left
            else:
                next_node = node.right
            if parent:
                if parent.left == node:
                    parent.left = next_node
                else:
                    parent.right = next_node
            else:
                self.root_node = next_node

        else:
            parent_min = node
            mini = node.right
            while mini.left:
                parent_min = mini
                mini = mini.left
            node.data = mini.data

            if parent_min.left == mini:
                parent_min.left = None
            else:
                parent_min.right = mini.right

tree = Tree()
a = tree.insert(9)
a = tree.insert(3)
a = tree.insert(7)
a = tree.insert(2)
a = tree.insert(4)
a = tree.insert(8)
a = tree.insert(12)
a = tree.insert(13)
a = tree.insert(11)
tree.inorder(a)
tree.search(10)
tree.delete(9)
print("")
tree.inorder(a)
